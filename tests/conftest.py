import pytest
from authors.models import Author
from users.models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture()
def get_auth_data(db):
    user = User.objects.create_user("test@test.com", "Test123Q")
    author = Author.objects.create(
        first_name="f_name", second_name="s_name", birth_at="2020-02-02", user=user
    )

    return {"email": "test@test.com", "password": "Test123Q"}


@pytest.fixture
def get_token(api_client, get_auth_data):
    response = api_client.post(
        "/auth/token/login/",
        data={"email": get_auth_data["email"], "password": get_auth_data["password"]},
    )

    return response
