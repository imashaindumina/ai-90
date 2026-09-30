"""Day 05 - error handling for network requests: raise_for_status(), timeout, and exception types."""

import time
import requests

# ---- 5.1 raise_for_status() - clean error checking ----

# Case 1: a request that succeeds
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    resp.raise_for_status()  # raises HTTPError if status is 400+
    data = resp.json()
    print("success:", data["title"])
except requests.exceptions.HTTPError as e:
    print(f"Server error: {e}")
except requests.exceptions.ConnectionError:
    print("No internet connection, or server unreachable")
except requests.exceptions.Timeout:
    print("Server took too long to reply")
except requests.exceptions.JSONDecodeError:
    print("Response wasn't valid JSON")

print("-" * 60)

# Case 2: a request that returns 404 - raise_for_status() catches it as HTTPError
try:
    resp = requests.get("https://jsonplaceholder.typicode.com/posts/99999", timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("success:", data["title"])
except requests.exceptions.HTTPError as e:
    print(f"Server error: {e}")
except requests.exceptions.ConnectionError:
    print("No internet connection, or server unreachable")
except requests.exceptions.Timeout:
    print("Server took too long to reply")
except requests.exceptions.JSONDecodeError:
    print("Response wasn't valid JSON")

print("-" * 60)

# Case 3: intentionally trigger a ConnectionError - a domain that doesn't exist
try:
    resp = requests.get("https://this-domain-does-not-exist-xyz123.com", timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print("success:", data)
except requests.exceptions.HTTPError as e:
    print(f"Server error: {e}")
except requests.exceptions.ConnectionError:
    print("No internet connection, or server unreachable")
except requests.exceptions.Timeout:
    print("Server took too long to reply")
except requests.exceptions.JSONDecodeError:
    print("Response wasn't valid JSON")

print("-" * 60)

# Case 4: intentionally trigger a Timeout - httpbin delays reply by 5s, we only wait 1s
try:
    resp = requests.get("https://httpbin.org/delay/5", timeout=1)
    resp.raise_for_status()
    data = resp.json()
    print("success:", data)
except requests.exceptions.HTTPError as e:
    print(f"Server error: {e}")
except requests.exceptions.ConnectionError:
    print("No internet connection, or server unreachable")
except requests.exceptions.Timeout:
    print("Server took too long to reply")
except requests.exceptions.JSONDecodeError:
    print("Response wasn't valid JSON")

print("=" * 60)

# ---- 5.2 Retry pattern - exponential backoff on transient errors ----


def get_with_retry(url, tries=3):
    """Retry a GET request on connection/timeout errors, with exponential backoff."""
    for attempt in range(tries):
        try:
            print(f"attempt {attempt + 1}/{tries}...")
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt == tries - 1:
                print("last attempt also failed - giving up")
                raise
            wait = 2**attempt
            print(f"failed ({type(e).__name__}), waiting {wait}s before retry...")
            time.sleep(wait)


# Case 5: retry demo - a domain that doesn't exist, every attempt fails with ConnectionError
try:
    data = get_with_retry("https://this-domain-does-not-exist-xyz123.com", tries=3)
    print("success:", data)
except requests.exceptions.ConnectionError:
    print("all 3 retries exhausted - the error was re-raised, caught here")
