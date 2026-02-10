class GardenError(Exception):
    """Base class for all exceptions related to the garden guardian."""
    pass


class PlantError(GardenError):
    """Exception raised for errors specific to plant health or status."""
    pass


class WaterError(GardenError):
    """Exception raised for errors in the irrigation or water supply."""
    pass


def ft_checker() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_checker()
