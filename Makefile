.PHONY: install update clean

install:
	poetry install

update:
	poetry run update_data

clean:
	rm -f data/us-latest.json
