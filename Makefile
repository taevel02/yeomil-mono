.PHONY: dev lint format test build run download nerd

dev:
	uv sync --all-groups

lint:
	uv run ruff format --check && uv run ruff check && uv run pyrefly check

format:
	uv run ruff format .

test:
	uv run pytest

build:
	uv build

download:
	uv run python download_upstream.py

run:
	@if [ ! -d "upstream/geist-font" ] || [ ! -d "upstream/pretendard" ]; then \
		echo "Upstream font resources not found. Downloading..."; \
		$(MAKE) download; \
	fi
	uv run yeomil-mono

nerd:
	./scripts/build-nerd-fonts.sh
