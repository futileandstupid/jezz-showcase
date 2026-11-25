"""Property-based conservation, rebate bounds, and closed-schema suite for ledger-starter."""

import json

import pytest
from hypothesis import given
from hypothesis import strategies as st
from pydantic import ValidationError

from ledger_starter.domain import (
    SettlementRequest,
    build_settlement_quote,
    compute_volume_rebate,
    net_after_fee,
)
from ledger_starter.gateway import parse_and_quote_json


@given(
    gross_cents=st.integers(min_value=1, max_value=1_000_000_000),
    fee_bps=st.integers(min_value=0, max_value=10_000),
    rebate_bps=st.integers(min_value=0, max_value=5_000),
)
def test_property_settlement_and_rebate_conservation(
    gross_cents: int,
    fee_bps: int,
    rebate_bps: int,
) -> None:
    """Every valid quote conserves gross_cents and bounds volume rebates within 0..=fee_cents."""
    req = SettlementRequest(account_id="acct_001", gross_cents=gross_cents, fee_bps=fee_bps)
    quote = build_settlement_quote(req)
    rebate = compute_volume_rebate(quote.fee_cents, rebate_bps)
    assert 0 <= quote.net_cents <= gross_cents
    assert quote.fee_cents + quote.net_cents == gross_cents
    assert net_after_fee(gross_cents, fee_bps) == quote.net_cents
    assert 0 <= rebate <= quote.fee_cents


def test_wire_gateway_accepts_canonical_payload_and_rejects_unknown_fields() -> None:
    """Closed wire schema accepts valid JSON and rejects unpermitted extra keys."""
    valid_json = json.dumps({"account_id": "acct_primary", "gross_cents": 10_000, "fee_bps": 250})
    quote = parse_and_quote_json(valid_json)
    assert quote.fee_cents == 250
    assert quote.net_cents == 9_750

    spoofed_json = json.dumps(
        {"account_id": "acct_primary", "gross_cents": 10_000, "fee_bps": 250, "admin": True}
    )
    with pytest.raises(ValidationError):
        parse_and_quote_json(spoofed_json)
