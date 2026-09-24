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

# ---- 4. A different API has a different JSON shape - always check the structure first ----
resp2 = requests.get("https://api.adviceslip.com/advice")
data2 = resp2.json()
print(type(data2))
print(data2["slip"]["advice"])
