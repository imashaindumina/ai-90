import requests

resp = requests.get("https://api.github.com/zen")
print("status_code:",resp.status_code)
print("text:",resp.text)

print("-" *60)

resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("status_code:",resp.status_code)
print("ok",resp.ok)
print("url:",resp.url)
print("content-type header:",resp.headers["Content-Type"])

print("-" *60)

data = resp.json()
print(type(data))
print(data["title"])
print(data["body"])

print("-" *60)

weather = {
    "current":{
       "temperature_2m":29.4,
       "wind_speed_10m":11.2,
   },
   "current_units":{"temperature_2m": "C"},
}
temp = weather["current"]["temperature_2m"]
print("temp (direct access):" ,temp)

temp_safe = weather.get("current",{}).get("temperature_2m")
print("temp (safe access):", temp)

missing_safe = weather.get("current",{}).get("humidity")
print("missing key with .get():",missing_safe)

print("-" *60)

resp3 = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude":6.9271,
        "longitude":79.8612,
        "current":"temperature_2m,wind_speed_10m",
    },
)

data3 = resp3.json()
print(type(data3))
print("COlombo temperature:",data3["current"]["temperature_2m"])
print("Colombo wind speed:",data3["current"]["wind_speed_10m"])

print("-" * 60)

resp2 = requests.get("https://api.adviceslip.com/advice")
data2 = resp2.json()
print(type(data2))
print(data2["slip"]["advice"])
