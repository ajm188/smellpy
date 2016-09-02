.PHONY: all dev venv clean test run

all: dev test

dev: venv
	venv/bin/pip install -r requirements-dev.txt
	@echo ""
	@echo "========================================"
	@echo "Don't forget to source venv/bin/activate"

venv:
	test -s venv || { virtualenv -p python3.4 venv; }
	venv/bin/pip install -r requirements.txt

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf docs/build
	rm -rf .tox
	rm -rf *.egg-info
	rm -rf venv
	rm -rf build
	rm -rf dist

test: dev
	tox

run:
