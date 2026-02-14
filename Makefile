ruff:
	@ruff check --fix .
	@ruff format .

package:
	@echo "Building package..."
	@uv run pyinstaller \
		--log-level ERROR \
		--onefile \
		--name pg-click-bait \
		src/02__example.py