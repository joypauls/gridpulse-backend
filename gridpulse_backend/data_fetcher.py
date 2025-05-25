from gridpulse_backend.eia_client import EIAClient


def get_latest_energy_mix() -> dict:
    client = EIAClient()
    data = client.fetch_us_hourly_generation()
    series = data["response"]["data"][0]

    return {
        "timestamp": series["period"],
        "values": series["value"],
    }
