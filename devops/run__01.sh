#!/bin/python3
set -e

# Start with a clean slate
rm ./assets/*.txt || true

uv run src/01__example.py --input-file ./assets/my_brothers.json

uv run src/01__example.py \
    --input-file ./assets/my_brothers.json \
    --include-city

echo "---------------------------------"
tree ./assets
echo "---------------------------------"

uv run src/01__example.py \
    --input-file ./assets/my_brothers.json \
    --include-city \
    --write-output

echo "---------------------------------"
tree ./assets
echo "---------------------------------"