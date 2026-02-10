
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name or not isinstance(plant_name, str):
        raise ValueError("Plant name cannot be empty!")
    if not 1 <= water_level <= 10:
        msg = (f"Water level {water_level} is too high (max 10)"
               if water_level > 10
               else f"Water level {water_level} is too low (min 1)")
        raise ValueError(msg)
    if not 2 <= sunlight_hours <= 12:
        msg = (f"Sunlight hours {sunlight_hours} is too low (min 2)"
               if sunlight_hours < 2
               else f"Sunlight hours {sunlight_hours} is too high (max 12)")
        raise ValueError(msg)

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 10, 12), "\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 10, 12), "\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad water value...")
    try:
        print(check_plant_health("tomato", 15, 12), "\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 10, 0), "\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
