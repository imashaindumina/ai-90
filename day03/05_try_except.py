# 05_try_except.py
# Topic: try/except - handling errors gracefully

import json
import os


# ---------- Practice: what happens without a try/except ----------
# Uncomment to see it crash with FileNotFoundError.


def load_config_unsafe(path):
    with open(path) as f:
        return f.read()


# load_config_unsafe("missing.json")  # crashes here


# ---------- Practice: basic try/except ----------


def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return None


print(load_config("missing.json"))
# Config file not found: missing.json
# None


# ---------- Practice: catching multiple specific exceptions ----------
# Prefer specific except types over one bare "except Exception".


def load_config_v2(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        return None
    except json.JSONDecodeError:
        print(f"Config file is not valid JSON: {path}")
        return None


print(load_config_v2("missing.json"))
# Config file not found: missing.json
# None


# ---------- Practice: else clause ----------
# "else" runs only if the try block did NOT raise - keeps try minimal.


def load_config_v3(path):
    try:
        f = open(path)
    except FileNotFoundError:
        print("File not found")
        return None
    else:
        print("File opened successfully")
        content = f.read()
        f.close()
        return content


load_config_v3("missing.json")
# File not found


# ---------- Practice: finally clause ----------
# "finally" always runs - success, failure, or return - good for cleanup.


def load_config_v4(path):
    try:
        f = open(path)
    except FileNotFoundError:
        print("File not found")
        return None
    else:
        content = f.read()
        f.close()
        return content
    finally:
        print("load_config_v4 attempt finished")


load_config_v4("missing.json")
# File not found
# load_config_v4 attempt finished


# ---------- Practice: reading a real file safely ----------
# open("data.txt") resolves against the terminal's current working
# directory, not this script's location. Anchor the path to the
# script's own folder so it works no matter where you run it from.

script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "data.txt")

try:
    with open(data_path, encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("Can't find file")
    content = None
else:
    print("success")
finally:
    print("This is run always")

print("content:", content)


# ---------- Practice: safe_divide - specific except types ----------


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Both arguments must be numbers")
        return None


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero -> None
print(safe_divide(10, "x"))  # Both arguments must be numbers -> None


# ======================================================================
# TASKS
# ======================================================================


# Task 17
def safe_int(text):
    """Convert text to int. Return None if it's not a valid integer."""
    try:
        return int(text)
    except ValueError:
        return None


print("Task 17:", safe_int("42"))  # 42
print("Task 17:", safe_int("abc"))  # None


# Task 18
def safe_get(data, key):
    """Return data[key], or None if the key doesn't exist."""
    try:
        return data[key]
    except KeyError:
        return None


print("Task 18:", safe_get({"a": 1}, "a"))  # 1
print("Task 18:", safe_get({"a": 1}, "b"))  # None


# Task 19
def safe_index(items, i):
    """Return items[i], or None if the index is out of range."""
    try:
        return items[i]
    except IndexError:
        return None


print("Task 19:", safe_index([1, 2, 3], 1))  # 2
print("Task 19:", safe_index([1, 2, 3], 9))  # None


# Task 20
def parse_price(text):
    """Convert text to a float price.

    Prints whether parsing succeeded, and always prints when the
    attempt is finished.
    """
    try:
        price = float(text)
    except ValueError:
        print(f"'{text}' is not a valid price")
        return None
    else:
        print(f"Parsed price: {price}")
        return price
    finally:
        print("parse_price attempt finished")


print("Task 20:", parse_price("19.99"))
print("Task 20:", parse_price("free"))
