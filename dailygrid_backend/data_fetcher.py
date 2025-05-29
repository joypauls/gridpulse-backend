from dailygrid_backend.eia_client import EIAClient
from dailygrid_backend.utils import get_yesterday_string, get_minus_n_days_string


def get_latest_seven_day_energy_mix() -> dict:
    client = EIAClient()

    yesterday = get_yesterday_string()
    start = get_minus_n_days_string(14)
    data = client.fetch_daily_generation(start_date=start, end_date=yesterday)
    response = data["response"]

    # return {
    #     "timestamp": series["period"],
    #     "values": series["value"],
    # }
    return response
