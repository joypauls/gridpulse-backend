import requests
import logging
from gridpulse_backend.config import EIA_API_KEY, EIA_BASE_URL


class EIAClient:
    def __init__(self, api_key: str = EIA_API_KEY):
        self.api_key = api_key
        self.base_url = EIA_BASE_URL
        self.session = requests.Session()

    def fetch_us_hourly_generation(self) -> dict:
        try:
            response = self.session.get(
                self.base_url,
                params={
                    "api_key": self.api_key,
                    "frequency": "hourly",
                    "data[]": ["value"],
                    "facets[region]": ["US"],
                    "sort[0][column]": "period",
                    "sort[0][direction]": "desc",
                    "offset": 0,
                    "length": 1,
                },
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.error(f"EIA API error: {e}")
            raise
