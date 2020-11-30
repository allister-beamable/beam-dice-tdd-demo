.PHONY: all clean
.PHONY: behave test
.PHONY: run


all: behave test

behave:
	behave

test:
	python -m pytest

run:
	FLASK_ENV=development FLASK_APP=beamdice flask run

clean:
	@echo "Nothing to clean"
