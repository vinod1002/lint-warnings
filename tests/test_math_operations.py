from src.sample import my_function
import pytest
from src.sample import my_function

def test_my_function(capsys):
    my_function()
    captured = capsys.readouterr()
    assert "Hello, linting!" in captured.out
