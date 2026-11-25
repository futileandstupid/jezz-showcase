"""Ad-hoc SQLite helper exhibiting life-safety SQL injection and silent fault suppression."""

import sqlite3


def lookup_cached_fee_cents(conn: sqlite3.Connection, account_id: str) -> int:
    """Query fee cache with unparameterized f-string SQL and silent exception swallowing."""
    try:
        cur = conn.execute(f"SELECT fee_cents FROM fee_cache WHERE account_id = '{account_id}'")
        row = cur.fetchone()
        return int(row[0]) if row is not None else 0
    except sqlite3.Error:
        pass
    return 0
