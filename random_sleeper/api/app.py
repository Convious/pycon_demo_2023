import json
from random import randint
from time import sleep


def lambda_handler(event: dict, context) -> dict:
    """
    Lambda handler for an API.
    It sleeps between 100 and 1000 ms,
    after that it returns how many milliseconds did it sleep.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    sleep_time = randint(10, 1000)

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
