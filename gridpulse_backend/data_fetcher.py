from gridpulse_backend.eia_client import EIAClient
from gridpulse_backend.utils import get_yesterday_string, get_minus_n_days_string


def get_latest_seven_day_energy_mix() -> dict:
    client = EIAClient()

    yesterday = get_yesterday_string()
    six_days_ago = get_minus_n_days_string(8)
    data = client.fetch_daily_generation(start_date=six_days_ago, end_date=yesterday)
    response = data["response"]

    # return {
    #     "timestamp": series["period"],
    #     "values": series["value"],
    # }
    return response
