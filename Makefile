install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --force-reinstall dist/hexlet_code-0.5.0-py3-none-any.whl

lint:
	poetry run flake8 brain_games
