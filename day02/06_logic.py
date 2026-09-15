"""Day 2 - conditionals."""

# ============================================================
# Practice - if / elif / else
# ============================================================
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"

print(grade)  # B

# elif stops at the FIRST match, so order matters.
# Put `score >= 50` first and everything above 50 becomes C.


# ============================================================
# Practice - comparison operators
# ============================================================
print(5 == 5)  # True   equal
print(5 != 3)  # True   not equal
print(5 > 3, 5 < 3)  # True False
print(5 >= 5, 5 <= 4)  # True False

print(0 < score < 100)  # True   - chaining works in Python
print(score > 0 and score < 100)  # True   - same thing, longer


# ============================================================
# Practice - and / or / not
# ============================================================
age = 20
country = "LK"

print(age >= 18 and country == "LK")  # True   - BOTH must be true
print(age >= 60 or country == "LK")  # True   - ONE is enough
print(not (age >= 60))  # True   - flips it

# `or` as a default value
name = ""
print(name or "unknown")  # unknown


# ============================================================
# Practice - truthiness
# ============================================================
# FALSY: False, None, 0, 0.0, "", [], {}, set()
# Everything else is TRUTHY.

print(bool(None), bool(""), bool(0), bool([]))  # all False
print(bool("abc"), bool(5), bool([1]), bool(" "))  # all True

items = []
if not items:
    print("empty")  # no need for len(items) == 0

# careful: [""] and [0] are TRUTHY - the list is not empty
print(bool([""]), bool([0]))  # True True


# ============================================================
# Practice - None is not the same as falsy
# ============================================================
tokens = 0

if not tokens:
    print("wrong - 0 is real data")

if tokens is None:
    print("right - but 0 is not None, so this does not print")

# `not x`     -> catches None, "", 0, [], {} ...
# `x is None` -> catches ONLY None


# ============================================================
# Practice - one-line if (ternary)
# ============================================================
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# good for simple choices, bad for anything complex


# ============================================================
# Practice - guard clauses beat nesting
# ============================================================
user = {"profile": {"email": "a@b.com"}}

# deeply nested - hard to read
if user is not None:
    if "profile" in user:
        if "email" in user["profile"]:
            print(user["profile"]["email"])

# flat - handle the bad cases first, then get on with it
profile = user.get("profile")
if profile is None:
    print("no profile")
elif profile.get("email") is None:
    print("no email")
else:
    print(profile["email"])


# ============================================================
# Task A - grade one score
# ============================================================
mark = 83

if mark >= 90:
    result = "A"
elif mark >= 75:
    result = "B"
elif mark >= 50:
    result = "C"
else:
    result = "F"

print("Task A:", result)  # Task A: B


# ============================================================
# Task B - safe division
# ============================================================
def safe_divide(a, b):
    """Divide a by b, or report that b is zero.

    We test `b == 0`, not `not b`.
    `not b` is also True for "", [], {} and None - values that are not
    zero at all. `b == 0` asks exactly the question we care about.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("Task B:", safe_divide(10, 0))  # Task B: Cannot divide by zero
print("Task B:", safe_divide(10, 2))  # Task B: 5.0


# ============================================================
# Task C - login check
# ============================================================
def check_login(username, password, is_banned):
    """Allow the login only when all three conditions hold."""
    if username and len(password) >= 6 and not is_banned:
        return "welcome"
    return "denied"


print("Task C:", check_login("imasha", "secret", False))  # welcome
print("Task C:", check_login("imasha", "abc", False))  # denied - too short
print("Task C:", check_login("", "secret", False))  # denied - no username
print("Task C:", check_login("imasha", "secret", True))  # denied - banned


# ============================================================
# Task D - validate one user record
# ============================================================
def describe_user(u):
    """Turn one user dict into a single human-readable line.

    The order of the checks is the whole exercise:
    `.get("tokens")` returns None when the key is missing, and 0 when the
    key is there with a real value of zero. Those two are different facts,
    so `is None` has to be checked BEFORE any truthiness test.
    """
    if not u.get("name"):
        return "missing name"

    count = u.get("tokens")
    if count is None:
        return "tokens not reported"
    if count == 0:
        return "used 0 tokens"
    return f"used {count} tokens"


print("Task D:", describe_user({"name": "kasun", "tokens": 0}))  # used 0 tokens
print("Task D:", describe_user({"name": "nimal"}))  # tokens not reported
print("Task D:", describe_user({"name": "", "tokens": 500}))  # missing name
print("Task D:", describe_user({"name": "imasha", "tokens": 500}))  # used 500 tokens


# ============================================================
# Task E - ternary practice
# ============================================================
tokens = 1523

print("Task E:", "high" if tokens > 1000 else "low")  # Task E: high
