import json
from random import randint
from time import sleep


def lambda_handler(event: dict, context) -> dict:
    sleep_time = randint(100, 1000)

    print(f"I'm about to sleep for {sleep_time} ms")

    sleep(milliseconds_to_seconds(sleep_time))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "sleep_time": sleep_time,
        }),
    }


def milliseconds_to_seconds(sleep_time: int) -> float:
    return round(sleep_time / 1000, 3)
