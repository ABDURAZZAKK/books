import pytest


@pytest.mark.parametrize(
    "name, description, validity",
    [
        (
            "book1",
            "des",
            201,
        ),
    ],
)
@pytest.mark.django_db
def test_create_book(db, get_token, api_client, name, description, validity):
    token = get_token.data["auth_token"]
    response = api_client.post(
        "/books/",
        format="json",
        headers={"Authorization": f"Token {token}"},
        data={
            "name": name,
            "description": description,
        },
    )

    assert response.status_code == validity
