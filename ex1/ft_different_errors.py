
def garden_operations() -> None:
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
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden = {}
        _ = garden["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        raise ValueError("test")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()


if __name__ == "__main__":
    test_error_types()
