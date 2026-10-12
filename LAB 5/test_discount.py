import pytest
from discount import apply_discount

@pytest.mark.parametrize("price,percent,expected", [
    (100, 0, 100),    # no discount
    (100, 50, 50),    # half price
    (100, 100, 0),    # free
    (200, 25, 150),   # quarter off
    (80, 10, 72),     # 10% off 80 = 72
])
def test_discount_calculation(price, percent, expected):
    assert apply_discount(price, percent) == expected