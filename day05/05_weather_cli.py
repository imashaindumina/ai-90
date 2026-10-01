"""Simple weather CLI - fetches current weather for a city."""

import requests
from dotenv import load_dotenv

load_dotenv()

CITIES = {
    "colombo": (6.9271, 79.8612),
    "kandy": (7.2906, 80.6337),
    "galle": (6.0535, 80.2210),
    "matara": (5.9549, 80.5550),
}


def get_weather(city: str) -> dict | None:
    """Fetch current weather for a known city name."""
    city = city.strip().lower()

    if city not in CITIES:
        print(f"'{city}' is not a known city.")
        return None

    lat, lon = CITIES[city]

    try:
        resp = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,wind_speed_10m",
            },
            timeout=10,
        )
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")
        return None
    except requests.exceptions.Timeout:
        print("Server took too long to respond.")
        return None
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
        return None

    data = resp.json()
    return data["current"]


def print_weather(city: str) -> None:
    """Print a formatted weather report for a friendly error."""
    current = get_weather(city)
    if current is None:
        return

    temp = current["temperature_2m"]
    wind = current["wind_speed_10m"]
    print(f"{city.title()}: {temp}°C, Wind {wind} km/h")


def main() -> None:
    for city in CITIES:
        print_weather(city)


if __name__ == "__main__":
    main()
