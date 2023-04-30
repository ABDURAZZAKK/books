import pytest
from datetime import date


@pytest.mark.parametrize(
    "first_name, second_name, birth_at, user, validity",
    [
        (
            "f_name",
            "s_name",
            date(2002, 8, 5),
            {"password": "Test123Q", "email": "test@test.com"},
            201,
        ),
        (
            "f_name",
            "s_name",
            date(2002, 8, 5),
            {"password": "", "email": "test1@test.com"},
            400,
        ),
    ],
)
@pytest.mark.django_db
def test_create_author(
    db, api_client, first_name, second_name, birth_at, user, validity
):
    response = api_client.post(
        "/authors/",
        format="json",
        data={
            "first_name": first_name,
            "second_name": second_name,
            "birth_at": birth_at,
            "user": user,
        },
    )

    assert response.status_code == validity
