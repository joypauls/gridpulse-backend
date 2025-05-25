from gridpulse_backend.data_fetcher import get_latest_energy_mix
from gridpulse_backend.data_writer import write_json


def main():
    data = get_latest_energy_mix()
    write_json(data)


if __name__ == "__main__":
    main()
