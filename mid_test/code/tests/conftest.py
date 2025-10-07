# test/conftest.py  (use tests/ if your folder is named tests/)
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # project root (where main.py lives)
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
