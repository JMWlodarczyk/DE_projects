import json
import requests
from typing import Dict


def get_data() -> Dict:
    """Fetch random user data from the API."""
    try:
        response = requests.get("https://randomuser.me/api/", timeout=5)
        response.raise_for_status()
        return response.json()["results"][0]
    except requests.RequestException as e:
        raise Exception(f"Error fetching data: {e}") from e


def format_data(raw_data: Dict) -> Dict:
    """Format raw user data into a clean dictionary."""
    location = raw_data["location"]
    formatted = {
        "first_name": raw_data["name"]["first"],
        "last_name": raw_data["name"]["last"],
        "gender": raw_data["gender"],
        "address": f"{location['street']['number']} {location['street']['name']}",
        "email": raw_data["email"],
        "postcode": location["postcode"],
        "username": raw_data["login"]["username"],
        "dob": raw_data["dob"]["date"],
        "phone": raw_data["phone"],
        "registered_date": raw_data["registered"]["date"],
        "picture": raw_data["picture"]["large"],
    }
    return formatted


def stream_data() -> None:
    """Fetch, format, and print user data."""
    try:
        raw_data = get_data()
        user_data = format_data(raw_data)
        print(json.dumps(user_data, indent=2))
    except Exception as e:
        print(f"Streaming error: {e}")