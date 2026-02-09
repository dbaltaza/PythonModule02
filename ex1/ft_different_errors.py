def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        _ = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as _:
            pass
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden = {"rose": "red", "tulip": "yellow"}
        print(garden["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        int("xyz")
        garden = {}
        print(garden["nope"])
    except (ValueError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def test_error_types() -> None:
    garden_operations()


if __name__ == "__main__":
    test_error_types()
