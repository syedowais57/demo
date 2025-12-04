from .helpers import greet
from .dependency_demo import format_user_message  # NEW: imported dependency


def handler(name: str) -> None:
    # Change behavior a bit so the diff is clear
    greeting = greet(name).upper()
    print(greeting)

    # Use the dependency function (this file is NOT changed in this PR)
    processed = format_user_message(name)
    print(processed)
