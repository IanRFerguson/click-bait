# Click Bait

[Read the Medium article](https://medium.com/@ianfergusonrva/click-bait-e00a843f3d6f)

## Setup

Just run `uv sync` to pull in the required dependencies! The Python source code is all directly executable from the `src/` directory:

```
tree ./src   
./src
├── 00__example.py
├── 01__example.py
└── 02__example.py

1 directory, 3 files
```

```python
uv run ./src/00__example.py

uv run ./src/00__example.py --name=buddy
```