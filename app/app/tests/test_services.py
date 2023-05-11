import responses
from django.conf import settings

from app.services import slow_sum, call_random_sleeper


def test_slow_sum():
    assert slow_sum(1) == 1
    assert slow_sum(10) == 55


@responses.activate
def test_call_random_sleeper():
    resp = responses.Response(
        method="GET",
        url=settings.RANDOM_SLEEPER_API_ENDPOINT,
        json={"sleep_time": 42},
    )
    responses.add(resp)
    assert call_random_sleeper() == 42
