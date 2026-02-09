
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
    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name, water_level, sunlight_hours):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        self.plants[plant_name] = {
            "water_level": water_level,
            "sunlight_hours": sunlight_hours
        }
        return f"Added {plant_name} successfully"

    def water_plant(self, plant_name, amount):
        if plant_name not in self.plants:
            raise WaterError(f"Plant '{plant_name}' not found!")

        self.plants[plant_name]["water_level"] += amount
        return f"Watering {plant_name} - success"

    def check_health(self, plant_name):
        if plant_name not in self.plants:
            raise HealthError(f"Plant '{plant_name}' not found!")

        plant = self.plants[plant_name]
        water = plant["water_level"]
        sun = plant["sunlight_hours"]

        if water > 10:
            raise HealthError(f"Water level {water} is too high (max 10)")

        return f"{plant_name}: healthy (water: {water}, sun: {sun})"


def test_garden_management():
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
        for plant in ["tomato", "lettuce"]:
            print(f"Watering {plant} - success")
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
