import sys
import argparse

from colorama import init
from os import name as osname, system as wsys
from typing import TypeVar, Optional, Callable, Union

T = TypeVar("T")
Number = Union[int, float]

def input_value(
    prompt: str,
    cast: Callable[[str], T] = str,
    min_value: Number | None = None,
    max_value: Number | None = None,
    allow_empty: bool = False
) -> Optional[T]:
    while True:
        print(f"{prompt} (q to quit).\n")
        raw = input(f"({cast.__qualname__}) > ").strip()

        if raw.lower() == 'q':
            return None
        if not raw and allow_empty:
            return None
        try:
            value = cast(raw)
        except ValueError:
            print(f"Valeur invalide ({cast.__name__} attendu).")
            continue

        if isinstance(value, (int, float)):
            if min_value is not None and value < min_value:
                print(f"La valeur doit être ≥ {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"La valeur doit être ≤ {max_value}.")
                continue
        return value
    
def clear_screen():
    if osname == 'nt':
        wsys('cls')
    else:
        print("\033[H\033[J", end="")