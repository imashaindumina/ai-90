"""Day 05 - query parameters, headers, and POST requests."""

import requests

# ---- 4.1 Query parameters - params dict builds the ?key=value part of the URL ----
resp = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
)
print("url:", resp.url)
posts = resp.json()
print("posts by userId=1:", len(posts))

print("-" * 60)

# ---- 4.2 Headers - the usual way to attach an API key (Bearer token pattern) ----
# This is the syntax you'll use once you have a real API key (section 06 - .env).
fake_api_key = "demo-key-123"
headers = {"Authorization": f"Bearer {fake_api_key}"}
resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)
print("status_code with headers sent:", resp.status_code)

print("-" * 60)

# ---- 4.3 POST request - sending data instead of fetching it ----
resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Hello from Python", "body": "My first POST request", "userId": 1},
)
print("status_code:", resp.status_code)  # 201 = Created
print("response:", resp.json())  # the fake API echoes it back with a new id
