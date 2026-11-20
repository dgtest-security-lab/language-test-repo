# Main Python application
import datetime
import json


def greet_user(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the GitHub Language Test Repository."


def get_current_date():
    """Return the current date."""
    return datetime.datetime.now().strftime("%Y-%m-%d")


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def main():
    user = {
        "name": "GitHub Tester",
        "language": "Python",
        "active": True
    }

    print(greet_user(user["name"]))
    print("Current date:", get_current_date())
    print("Sum of 10 and 20:", calculate_sum(10, 20))

    print("\nUser information:")
    print(json.dumps(user, indent=4))


if __name__ == "__main__":
    main()
