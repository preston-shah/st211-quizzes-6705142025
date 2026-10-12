import pytest

@pytest.mark.parametrize("user", [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
])
def test_user_has_name(user):
    assert "name" in user