"""Day 05 - requests basics: GET requests, the response object, and JSON parsing."""

import requests

# ---- 1. First GET request ----
resp = requests.get("https://api.github.com/zen")
print("status_code:", resp.status_code)
print("text:", resp.text)

print("-" * 60)

# ---- 2. Response object attributes ----
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("status_code:", resp.status_code)
print("ok:", resp.ok)
print("url:", resp.url)
print("content-type header:", resp.headers["Content-Type"])

print("-" * 60)

# ---- 3. Parsing a JSON response into a dict ----
data = resp.json()
print(type(data))
print(data["title"])
print(data["body"])

print("-" * 60)

# ---- 3.1 Getting values from nested data safely ----
weather = {
    "current": {
        "temperature_2m": 29.4,
        "wind_speed_10m": 11.2,
    },
    "current_units": {"temperature_2m": "°C"},
}

temp = weather["current"]["temperature_2m"]
print("temp (direct access):", temp)

# .get() is safer - if a key is missing, this returns None instead of crashing
temp_safe = weather.get("current", {}).get("temperature_2m")
print("temp (safe access):", temp_safe)

missing_safe = weather.get("current", {}).get("humidity")   # key doesn't exist
print("missing key with .get():", missing_safe)              # None, no crash

print("-" * 60)

# ---- 3.2 Real API example - parsing a live JSON response (Open-Meteo) ----
# resp.json() is a shortcut for json.loads(resp.text) - it turns the response
# body text into a Python dict/list. No API key needed - Open-Meteo is free public data.
resp3 = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 6.9271,
        "longitude": 79.8612,
        "current": "temperature_2m,wind_speed_10m",
    },
)
data3 = resp3.json()
print(type(data3))
print("Colombo temperature:", data3["current"]["temperature_2m"])
print("Colombo wind speed:", data3["current"]["wind_speed_10m"])

# Important: if the server returns something that isn't valid JSON (e.g. an HTML
# error page instead of JSON), resp.json() raises requests.exceptions.JSONDecodeError.
# That's why real code checks resp.status_code / resp.ok BEFORE calling .json() -
# this try/except + status-check pattern is covered properly in section 05.

print("-" * 60)

# ---- 4. A different API has a different JSON shape - always check the structure first ----
resp2 = requests.get("https://api.adviceslip.com/advice")
data2 = resp2.json()
print(type(data2))
print(data2["slip"]["advice"])
