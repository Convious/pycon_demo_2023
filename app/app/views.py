from random import randint
from typing import TYPE_CHECKING

from django.http import JsonResponse

from app.services import slow_sum, call_random_sleeper

if TYPE_CHECKING:
    from django.http import Request


def cpu_bound(request: "Request") -> JsonResponse:
    number = randint(100_000, 10_000_000)
    result = slow_sum(number)
    return JsonResponse({
        "input": number,
        "result": result,
    })


def io_bound(request: "Request") -> JsonResponse:
    result = call_random_sleeper()
    return JsonResponse({
        "result": result,
    })
