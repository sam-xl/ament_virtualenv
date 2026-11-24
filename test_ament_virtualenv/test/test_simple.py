import sys
import importlib

import pytest


# 1: Test if we're in a virtual environment at all.
def test_in_venv():
    base_prefix = (
        getattr(sys, "base_prefix", None)
        or getattr(sys, "real_prefix", None)
        or sys.prefix
    )
    assert sys.prefix != base_prefix, "Python virtual environment not activated."


# 2: Test the Python version.
def test_python_version():
    assert sys.version_info.major == 3, "Wrong Python version."


# 3: Test if proper requirements have been installed
def test_proper_requirements():
    six = importlib.import_module("six")
    assert six.__version__ == "1.0.0", (
        f"Requirements not provided correctly (expected 'six==1.0.0', found {six.__version__})"
    )
