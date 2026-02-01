ruff:
	@ruff check --fix .
	@ruff format .

package:
	@echo "Building package..."
	@uv run pyinstaller --onefile src/02__example.py