.DEFAULT_GOAL := all
isort = isort kysy tests
black = black -S -l 120 --target-version py39 kysy tests

.PHONY: install
install:
	pip install -U pip wheel
	pip install -r tests/requirements.txt
	pip install -U .

.PHONY: install-all
install-all: install
	pip install -r tests/requirements-dev.txt

.PHONY: isort
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	python setup.py check -ms
	flake8 kysy/ tests/
	$(isort) --check-only --df
	$(black) --check --diff

.PHONY: mypy
mypy:
	mypy kysy

.PHONY: fixtures
fixtures:
	mkdir -p tests/fixtures/cache && cd tests/fixtures/cache && touch index

.PHONY: test
test: clean fixtures
	pytest --cov=kysy --log-format="%(levelname)s %(message)s"

.PHONY: testcov
testcov: test
	@echo "building coverage html"
	@coverage html

.PHONY: all
all: lint mypy testcov

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	rm -rf tests/fixtures/cache
	rm -f kysy-report.*
	python setup.py clean
