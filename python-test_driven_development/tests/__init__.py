"""Test package initialization."""
import importlib

globals()['6-max_integer_test'] = importlib.import_module(
    '.6-max_integer_test', __name__
)
