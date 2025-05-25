from datetime import datetime, timezone, timedelta


# def now_utc_iso() -> str:
#     return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H")


def get_today_string() -> str:
    """Returns today's date in YYYY-MM-DD format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def get_minus_n_days_string(n: int) -> str:
    """Returns the date n days ago in YYYY-MM-DD format."""
    return (datetime.now(timezone.utc) - timedelta(days=n)).strftime("%Y-%m-%d")


def get_yesterday_string() -> str:
    """Returns yesterday's date in YYYY-MM-DD format."""
    return get_minus_n_days_string(1)
