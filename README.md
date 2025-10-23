# Project Name

A short description of the project.

---

## Structure

- `src/` – Reusable Python modules and business logic  
- `notebooks/` – Jupyter notebooks (exploration and experiments)  
- `data/` – **Not tracked** (raw and processed data)  
- `tests/` – Unit tests using pytest  
- `configs/` – YAML/JSON configuration files  
- `results/` – Outputs (figures, tables, models) – **Not tracked**  
- `docs/` – Documentation  

---

## Quick Start

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

We use **pytest** for unit testing.

### 1) Install dev dependencies
```bash
pip install -r requirements.txt
# or, if you keep dev deps separately:
# pip install -r requirements-dev.txt
```

### 2) Make imports work with src layout
If you use the `src/` layout, create a `pytest.ini` at the project root:

```ini
# pytest.ini
[pytest]
pythonpath = .
```

### 3) Run the tests
Run tests from the project root:

```bash
pytest -q
# or
python -m pytest -q
```

> 💡 Avoid running files directly (e.g. `python tests/test_main.py`),  
> because it can break imports with the `src` layout.

### 4) Example test
```python
# tests/test_main.py
from src.main import hello

def test_hello():
    assert hello("Fatih") == "Hello, Fatih!"
```

### 5) Optional: Coverage report
```bash
pip install pytest-cov
pytest --cov=src --cov-report=term-missing
```

### 6) VS Code integration
Create a `.env` file in your workspace root:

```
PYTHONPATH=${workspaceFolder}
```

Then open **Testing** view → select **pytest** as the test framework →  
set the test root folder to your project directory.

---

## Example Run

```bash
python src/main.py
# Output:
# Hello, world!
```

---

## License

Specify your license here, for example:  
**MIT License © 2025 Your Name**