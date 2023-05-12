import requests
from django.conf import settings


def slow_sum(number: int) -> int:
    acc = 0
    for i in range(number):
        acc += i + 1
    return acc


def call_random_sleeper() -> int:
    resp = requests.get(settings.RANDOM_SLEEPER_API_ENDPOINT)
    resp.raise_for_status()
    return resp.json()["sleep_time"]
