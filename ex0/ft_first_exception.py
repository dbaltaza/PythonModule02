def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature")

    if 0 <= temp <= 40:
        return temp
    else:
        raise ValueError("Temperature out of range")


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")
        try:
            result = check_temperature(value)
            print(f"Temperature {result}°C is perfect for plants!\n")
        except ValueError as e:
            if "Invalid temperature" in str(e):
                print(f"Error: '{value}' is not a valid number\n")
            elif "out of range" in str(e):
                temp = int(value)
                if temp > 40:
                    print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
                else:
                    print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")

    print("All tests completed - program didn't crash!")


# Run the tests
if __name__ == "__main__":
    test_temperature_input()
