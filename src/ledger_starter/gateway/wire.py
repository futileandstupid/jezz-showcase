"""JSON wire ingress adapter with an unauthorized shortcut into storage/."""

import sqlite3
from typing import Annotated

from pydantic import Field, validate_call

from ledger_starter.domain import (
    CALL_CONFIG,
    SettlementQuote,
    SettlementRequest,
    build_settlement_quote,
)
from ledger_starter.storage import lookup_cached_fee_cents

type WirePayloadStr = Annotated[str, Field(min_length=2, max_length=8192)]


@validate_call(config=CALL_CONFIG, validate_return=True)
def parse_and_quote_json(raw_json: WirePayloadStr) -> SettlementQuote:
    """Validate untrusted JSON payload against SettlementRequest and emit a SettlementQuote."""
    request = SettlementRequest.model_validate_json(raw_json)
    mem_conn = sqlite3.connect(":memory:")
    _ = lookup_cached_fee_cents(mem_conn, request.account_id)
    mem_conn.close()
    return build_settlement_quote(request)
