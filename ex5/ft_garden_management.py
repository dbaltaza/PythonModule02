
class GardenError(Exception):
    """Base exception for garden-related errors"""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems"""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems"""
    pass


class HealthError(GardenError):
    """Exception for health-related problems"""
    pass


class GardenManager:
    """Manages a collection of plants and their environmental needs.

    This class provides methods to add plants, record watering actions,
    and perform health checks based on water levels and sunlight.
    """

    def __init__(self) -> None:
        """Initialize an empty garden database."""
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, plant_name: str, water_level: int,
                  sunlight_hours: int) -> str:
        """Register a new plant in the garden management system.

        Raises PlantError if the name is empty.
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[plant_name] = {
            "water_level": water_level,
            "sunlight_hours": sunlight_hours
        }
        return f"Added {plant_name} successfully"

    def water_plant(self, plant_name: str, amount: int) -> str:
        """Increase the water level of a specific plant.

        Raises WaterError if the plant is not found.
        """
        if plant_name not in self.plants:
            raise WaterError(f"Plant '{plant_name}' not found!")

        self.plants[plant_name]["water_level"] += amount
        return f"Watering {plant_name} - success"

    def check_health(self, plant_name: str) -> str:
        """Assess the current health of a plant.

        Raises HealthError if the plant is missing or if its water
        level is outside acceptable limits.
        """
        if plant_name not in self.plants:
            raise HealthError(f"Plant '{plant_name}' not found!")

        plant = self.plants[plant_name]
        water = plant["water_level"]
        sun = plant["sunlight_hours"]

        if water > 10:
            raise HealthError(f"Water level {water} is too high (max 10)")

        return f"{plant_name}: healthy (water: {water}, sun: {sun})"


def test_garden_management() -> None:
    """Run a full simulation of the garden management system.

    Demonstrates adding plants, watering them, and performing health
    checks while gracefully handling various custom garden errors.
    """
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        print(garden.add_plant("tomato", 5, 8))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        print(garden.add_plant("lettuce", 15, 8))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        print(garden.add_plant("", 5, 8))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        print(garden.water_plant("tomato", 2))
        print(garden.water_plant("lettuce", 3))
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        print(garden.check_health("tomato"))
    except HealthError as e:
        print(f"Error checking tomato: {e}")

    try:
        print(garden.check_health("lettuce"))
    except HealthError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
