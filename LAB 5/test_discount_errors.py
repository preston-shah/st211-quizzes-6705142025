import pytest
from discount import apply_discount

@pytest.mark.parametrize("bad_percent", [-1, -50, 101, 200])
def test_invalid_percent_raises(bad_percent):
    with pytest.raises(ValueError):   # each bad value must raise ValueError
        apply_discount(100, bad_percent)