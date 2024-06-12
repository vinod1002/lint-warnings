import pytest
from src.my_module.py import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

if __name__ == "__main__":
    pytest.main()
