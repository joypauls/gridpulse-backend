from pprint import pprint

from gridpulse_backend.data_fetcher import get_latest_five_day_energy_mix
from gridpulse_backend.data_writer import write_json

# from gridpulse_backend.utils import get_yesterday_string


def main():
    # print(now_utc_iso())

    data = get_latest_five_day_energy_mix()
    # pprint(data)

    write_json(data)


if __name__ == "__main__":
    main()
