from .helpers import greet

def handler(name: str) -> None:
    print(greet(name))