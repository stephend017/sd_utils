import pytest
from examples.models.user import User


def test_model():
    m = User(name="required")

    assert m.name == "required"
    assert m.email is None


def test_model_requirement():
    with pytest.raises(ValueError):
        _ = User()
