import pytest
from app import app


@pytest.mark.parametrize("number", ["123", "-123", "0"])
def test_valid_signed_integers(number):
    with app.test_client() as client:
        response = client.post("/", data={"number1": number, "number2": number})
        assert response.status_code == 200


@pytest.mark.parametrize("number", ["abc", "12.3", "+123", ""])
def test_invalid_signed_integers(number):
    with app.test_client() as client:
        response = client.post("/", data={"number1": number, "number2": number})
        assert response.status_code != 200
