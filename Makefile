.PHONY: install update clean copy-local

install:
	poetry install

update:
	poetry run update_data

clean:
	rm -f data/daily_energy_mix_latest.json

# copy-local:
# 	cp public/data/daily_energy_mix_latest.json ../dailygrid.dev/src/data/daily_energy_mix_latest.json