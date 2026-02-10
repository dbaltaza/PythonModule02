
def water_plants(plant_list: list[str] | tuple[str, ...]) -> None:
    """Simulate the plant watering process with guaranteed cleanup.

    Uses a finally block to ensure the watering system is always
    closed, preventing water waste or system pressure issues even if
    an invalid plant entry is encountered.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Run tests for the watering system's error handling.

    Verifies that the system behaves correctly with valid plant lists
    and ensures cleanup occurs when encountering a 'None' value.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    good_list = ("tomato", "lettuce", "carrots",)
    try:
        water_plants(good_list)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_list = ("tomato", None)
    try:
        water_plants(bad_list)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
