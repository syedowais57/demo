from .helpers import greet
from .dependency_demo import format_user_message


def handler(name: str) -> None:
    # Slight change so there is a new diff
    greeting = greet(name)
    print(greeting)

    # This will call the buggy helper
    message = format_user_message(name)
    print(message)
