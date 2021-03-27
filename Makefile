install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/hexlet_code-0.3.0-py3-none-any.whl
