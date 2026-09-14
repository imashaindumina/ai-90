"""Day 2 — lists."""

# ============================================================
# Practice — creating and reading
# ============================================================
models = ["gpt-4", "claude", "gemini"]

print(models[0])                # gpt-4     first
print(models[-1])               # gemini    last
print(models[1:])               # ['claude', 'gemini']
print(len(models))              # 3
print("claude" in models)       # True      membership test
print(models.index("claude"))   # 1         position of a value


# ============================================================
# Practice — modifying
# ============================================================
items = [3, 1, 2]

items.append(4)                 # add one item to the end
print(items)                    # [3, 1, 2, 4]

items.insert(0, 0)              # insert at a position
print(items)                    # [0, 3, 1, 2, 4]

items.remove(0)                 # remove by VALUE, not by index
print(items)                    # [3, 1, 2, 4]

last = items.pop()              # remove last AND return it
print(last, items)              # 4 [3, 1, 2]


# ============================================================
# Practice — the .sort() trap
# ============================================================
nums = [3, 1, 2]

result = nums.sort()            # sorts IN PLACE, returns None
print("nums  :", nums)          # [1, 2, 3]
print("result:", result)        # None  <- never write nums = nums.sort()

nums = [3, 4, 1, 2]
ordered = sorted(nums)          # returns a NEW list
print("nums   :", nums)         # [3, 4, 1, 2]  untouched
print("ordered:", ordered)      # [1, 2, 3, 4]

# Rule: a METHOD (.sort) changes the object.
#       a FUNCTION (sorted) gives you a new one.


# ============================================================
# Task 10 — basic statistics
# ============================================================
nums = [4, 2, 9, 1, 7]

print(f"Sum     : {sum(nums)}")
print(f"Average : {sum(nums) / len(nums):.2f}")
print(f"Max     : {max(nums)}   Min: {min(nums)}")


# ============================================================
# Task 11 — sort WITHOUT changing the original
# ============================================================
nums = [4, 2, 9, 1, 7]
order = sorted(nums)

print("original:", nums)        # [4, 2, 9, 1, 7]  still intact
print("sorted  :", order)       # [1, 2, 4, 7, 9]


# ============================================================
# Task 12 — remove duplicates
# ============================================================
nums = [1, 2, 2, 3, 3, 3, 4]

# set() drops duplicates but loses order -> sorted() puts it back
print(sorted(set(nums)))                # [1, 2, 3, 4]

# dict.fromkeys keeps the ORIGINAL order (Python 3.7+)
print(list(dict.fromkeys(nums)))        # [1, 2, 3, 4]

# works even when the duplicates are not next to each other
mixed = [1, 2, 1, 2, 3]
print(list(dict.fromkeys(mixed)))       # [1, 2, 3]


# ============================================================
# Task 13 — sort by length
# ============================================================
fruits = ["banana", "kiwi", "apple", "fig"]

print(sorted(fruits, key=len))          # ['fig', 'kiwi', 'apple', 'banana']
print(sorted(fruits))                   # alphabetical, for comparison


# ============================================================
# Task 14 — pair two lists together
# ============================================================
names = ["a", "b", "c"]
scores = [90, 75, 60]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# a: 90
# b: 75
# c: 60

# zip() returns a lazy ITERATOR, not a list
zipped = zip(names, scores)
print(zipped)                           # <zip object at 0x...>
print(list(zipped))                     # [('a', 90), ('b', 75), ('c', 60)]
print(list(zipped))                     # []  <- already consumed!

# BONUS — build a dictionary from two lists
print(dict(zip(names, scores)))         # {'a': 90, 'b': 75, 'c': 60}
