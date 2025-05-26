.PHONY: install update clean copy-local

install:
	poetry install

update:
	poetry run update_data

clean:
	rm -f data/daily_energy_mix_latest.json

copy-local:
	cp data/daily_energy_mix_latest.json ../gridpulse.dev/src/data/daily_energy_mix_latest.json