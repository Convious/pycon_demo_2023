from typing import TYPE_CHECKING

import responses
from django.conf import settings

if TYPE_CHECKING:
    from django.test import Client
    from pytest_mock import MockFixture


def test_cpu_bound_endpoint(client: "Client", mocker: "MockFixture") -> None:
    mocker.patch("app.views.randint", return_value=4)
    response = client.get('/api/cpu-bound/')
    assert response.status_code == 200
    assert response.json() == {
        "input": 4,
        "result": 10,
    }


@responses.activate
def test_io_bound_endpoint(client: "Client") -> None:
    resp = responses.Response(
        method="GET",
        url=settings.RANDOM_SLEEPER_API_ENDPOINT,
        json={"sleep_time": 42},
    )
    responses.add(resp)

    response = client.get('/api/io-bound/')
    assert response.status_code == 200
    assert response.json() == {"result": 42}
