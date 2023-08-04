build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

capitalize:
	poetry run capitalize

lint:
	poetry run flake8 some_program

test:
	PYTHONPATH=some_program python3 tests/test_capitalize.py
