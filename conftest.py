from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REFERENCE_ROOT = ROOT / "lri-reference"

reference_path = str(REFERENCE_ROOT)
if reference_path not in sys.path:
    sys.path.insert(0, reference_path)
