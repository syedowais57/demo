from .helpers import greet
from .dependency_demo import format_user_message

t
def main() -> None:
    name = "John"
    print(greet(name))
    print(format_user_message(name))
DEFAULT_VALUE = "John"
def handler(name: str) -> None:
    print(greet(name))

