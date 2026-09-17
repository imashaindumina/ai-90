# ============================================================
# Task A - clean up messy city names
# ============================================================
raw = ["  colombo ", "KANDY", " galle  ", "  MaTaRa"]

# .strip() returns a string, so .title() can be called on the result.
# Chaining reads left to right: take c, strip it, then title-case it.
clean = [c.strip().title() for c in raw]
print("Task A:", clean)                 # ['Colombo', 'Kandy', 'Galle', 'Matara']


# ============================================================
# Task B - filter, do not transform
# ============================================================
marks = [72, 45, 91, 38, 64, 50]

# The `if` sits at the END. There is no `else` - items either survive or
# they are dropped. 6 items in, 4 items out.
passes = [n for n in marks if n >= 50]
print("Task B:", passes)                # [72, 91, 64, 50]


# ============================================================
# Task C - transform every item, drop nothing
# ============================================================
# The `if ... else` sits at the FRONT, before the `for`, and the `else` is
# required. 6 items in, 6 items out - every one of them changed.
labels = ["pass" if n >= 50 else "fail" for n in marks]
print("Task C:", labels)                # ['pass', 'fail', 'pass', 'fail', 'pass', 'pass']

# B and C are the whole lesson. Same list, same condition, different job:
#   drop some items   -> `if` at the end,   no else
#   change every item -> `if/else` at the front


# ============================================================
# Task D - dict from a list of dicts
# ============================================================
users = [
    {"name": "kasun",  "tokens": 120},
    {"name": "nimal",  "tokens": 0},
    {"name": "sunil",  "tokens": 940},
    {"name": "amali",  "tokens": 55},
]

# The `:` makes it a dict. The `if` at the end filters out the small ones.
heavy = {u["name"]: u["tokens"] for u in users if u["tokens"] > 100}
print("Task D:", heavy)                 # {'kasun': 120, 'sunil': 940}


# ============================================================
# Task E - put it together
# ============================================================
# 1. total tokens - no square brackets needed inside sum()
total = sum(u["tokens"] for u in users)
print("Task E:", total)                 # 1115

# 2. everyone who used exactly 0 - note `== 0`, not `not u["tokens"]`
unused = [u["name"] for u in users if u["tokens"] == 0]
print("Task E:", unused)                # ['nimal']

# 3. did anyone go over 500?
print("Task E:", any(u["tokens"] > 500 for u in users))   # True
