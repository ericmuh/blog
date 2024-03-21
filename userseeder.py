import json
import os
import django
from django.contrib.auth.hashers import make_password
# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog.settings")

# Initialize Django
django.setup()
# Create a fixture for the users
def create_fixture(users, output_file):
    fixture_data = []
    for user_data in users:
        user = {
            "model": "auth.user",
            "pk": user_data["pk"],
            "fields": {
                "username": user_data["username"],
                "email": user_data["email"],
                "password": make_password(user_data["password"]),
                "is_staff": False,
                "is_superuser": False,
                "is_active": True,
                "date_joined": user_data["date_joined"],
            },
        }
        fixture_data.append(user)

    with open(output_file, "w") as f:
        json.dump(fixture_data, f, indent=2)


if __name__ == "__main__":
    users = [
        {
            "pk": 1,
            "username": "user1",
            "email": "user1@example.com",
            "password": "password1",
            "date_joined": "2024-03-21T00:00:00Z",
        },
        {
            "pk": 2,
            "username": "user2",
            "email": "user2@example.com",
            "password": "password2",
            "date_joined": "2024-03-22T00:00:00Z",
        },
    ]

    create_fixture(users, "users.json")
