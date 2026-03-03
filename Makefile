# Makefile

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
	
re-install:
	uv build
	uv tool install dist/*.whl

push-fix-lint:
	git add -A
	git commit -m 'fix linter errors'
	git push
