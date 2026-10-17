"""
visualization_boilerplate.py

Module proxy ensuring standard Python import compatibility for visualization-boilerplate.py.
Re-exports all public constants, functions, and style palettes.
"""

import importlib.util
import sys
from pathlib import Path

_target_path = Path(__file__).parent / "visualization-boilerplate.py"
if not _target_path.exists():
    _target_path = Path(__file__).parent / "boilerplates" / "visualization-boilerplate.py"

_spec = importlib.util.spec_from_file_location("_visualization_boilerplate_impl", _target_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Unable to load visualization boilerplate from {_target_path}")

_mod = importlib.util.module_from_spec(_spec)
sys.modules["_visualization_boilerplate_impl"] = _mod
_spec.loader.exec_module(_mod)

# Export all non-private attributes
for _attr in dir(_mod):
    if not _attr.startswith("__"):
        globals()[_attr] = getattr(_mod, _attr)
