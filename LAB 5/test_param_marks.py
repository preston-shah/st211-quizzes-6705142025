import pytest

@pytest.mark.parametrize("value,expected", [
    pytest.param(2, 4, id="two_squared"),
    pytest.param(3, 9, id="three_squared"),
    pytest.param(5, 20, id="known_bug",
                 marks=pytest.mark.xfail),   # 5**2=25 not 20 -- bug not fixed yet
])
def test_square(value, expected):
    assert value ** 2 == expected