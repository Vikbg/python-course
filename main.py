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

def user_await():
    input("Please press Enter...")

def test_lesson_print():
    clear_screen()
    print("Ok today you will learn your fist thing in python")
    print("Show somthing on the screen!\n")
    user_await()
    user_input = input_value(prompt="To do this, you just need to type print(), and something in it between commas \
                             like print(\"Hello, World!\")", cast=str)
    if user_input:
        if user_input.strip().lower() == "print(\"Hello, World!\")".strip().lower():
            print("Congratualation !")
            
def test_lesson_types():
    clear_screen()
    print("Today you will learn th python types.")
    user_await()
    print("In Python, there's lot of types but the most commons are str, int, float and bool.")
    user_await()
    print("The int type is for integers so signed complete numbers like -100, -45, 0, 3, 4566")
    
    
if __name__ == "__main__":
    test_lesson_print()