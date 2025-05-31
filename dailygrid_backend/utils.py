from datetime import datetime, timedelta
import pytz


def get_now_central_string() -> str:
    return datetime.now(pytz.timezone("US/Central")).strftime("%Y-%m-%d %H:%M")


def get_today_string() -> str:
    """Returns today's date in YYYY-MM-DD format."""
    return datetime.now(pytz.timezone("US/Central")).strftime("%Y-%m-%d")


def get_minus_n_days_string(n: int) -> str:
    """Returns the date n days ago in YYYY-MM-DD format."""
    return (datetime.now(pytz.timezone("US/Central")) - timedelta(days=n)).strftime(
        "%Y-%m-%d"
    )


def get_yesterday_string() -> str:
    """Returns yesterday's date in YYYY-MM-DD format."""
    return get_minus_n_days_string(1)
