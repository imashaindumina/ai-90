"""Day 2 — dictionaries, tuples and sets."""

# ============================================================
# Practice — creating and reading
# ============================================================
user = {
    "name": "imasha",
    "country": "LK",
    "tokens_used": 1523,
    "active": True,
}

print(user["name"])  # imasha
print(len(user))  # 4
print("name" in user)  # True

# [] raises KeyError when the key is missing
# print(user["email"])                  # KeyError: 'email'

print(user.get("email"))  # None      — no crash
print(user.get("email", "not set"))  # not set   — with a default

# RULE: key is certain -> []       key might be missing -> .get()


# ============================================================
# Practice — modifying
# ============================================================
user["email"] = "a@b.com"  # add or overwrite
user["tokens_used"] += 100  # update a value
del user["active"]  # remove (KeyError if missing)
user.pop("country", None)  # remove safely

user.update({"plan": "pro", "country": "LK"})  # several at once
print(user)


# ============================================================
# Practice — three ways to loop
# ============================================================
for key in user:  # keys only
    print(key, end=" ")
print()

for value in user.values():  # values only
    print(value, end=" ")
print()

for key, value in user.items():  # both — you will use this most
    print(f"{key:<14}: {value}")


# ============================================================
# Practice — tuples and sets
# ============================================================
point = (3, 4)  # tuple: cannot be changed
# point[0] = 5                          # TypeError

x, y = point  # unpacking
print(x, y)  # 3 4

tags = {"ai", "ai", "python", "rag"}  # set: unique values only
print(tags)  # 'ai' stored once

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # {2, 3}        in both
print(a | b)  # {1, 2, 3, 4}  all of them
print(a - b)  # {1}           only in a


# ============================================================
# Task 15 — a dictionary about you
# ============================================================
me = {
    "name": "imasha",
    "city": "Colombo",
    "skills": ["python", "git"],
}

for key, value in me.items():
    print(f"{key:<8}: {value}")
# name    : imasha
# city    : Colombo
# skills  : ['python', 'git']


# ============================================================
# Task 16 — read a key that may not exist
# ============================================================
print(me.get("email", "not provided"))  # not provided
print(me.get("name", "not provided"))  # imasha


# ============================================================
# Task 17 — nested data from an API
# ============================================================
resp = {
    "id": "msg_01",
    "model": "claude-opus",
    "content": [{"type": "text", "text": "hello"}],
    "usage": {"input_tokens": 12, "output_tokens": 5},
}

# direct access — fine when you are sure the keys exist
print(resp["usage"]["output_tokens"])  # 5
print(resp["content"][0]["text"])  # hello

# safe access — the pattern you will use every day from Day 6 onwards
print(resp.get("usage", {}).get("output_tokens", 0))  # 5

broken = {}
print(broken.get("usage", {}).get("output_tokens", 0))  # 0  — no crash

# The {} default is the trick: it gives the SECOND .get() something to
# work on. A None default would crash with AttributeError.


# ============================================================
# Task 18 — count how often each word appears
# ============================================================
words = ["ai", "rag", "ai", "python", "ai"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {'ai': 3, 'rag': 1, 'python': 1}

# read as: take the current count (0 if new), add one, store it back

# sort by count, highest first
for word, n in sorted(counts.items(), key=lambda kv: -kv[1]):
    print(f"{word:<8}: {n}")
