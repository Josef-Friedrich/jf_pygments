# Run all recipes
all: upgrade format lint type_check

# Install the dependencies (alias of upgrade)
install: upgrade

# Install the editable package based on the provided local file path
install_editable: install
	uv pip install --editable .

# Upgrade the dependencies
upgrade:
	uv sync --upgrade

# Upgrade the dependencies (alias of upgrade)
update: upgrade

# Build Python packages into source distributions and wheels
build:
	uv build

# Upload distributions to an index
publish:
	uv build
	uv publish

# Run ruff format
format:
	uv tool run ruff check --select I --fix .
	uv tool run ruff format

# Run ruff check
lint:
	uv tool run ruff check --fix

# Perform type checking using mypy
type_check:
	uv run mypy src/jf_pygments
