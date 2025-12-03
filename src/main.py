from .helpers import greet
from .extra_utils import bye   # NEW IMPORT TO TEST DEPENDENCIES

def handler(name: str) -> None:
    print(greet(name).upper())
    print(bye(name))
