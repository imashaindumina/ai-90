"""Day 2 - loops."""

# ============================================================
# Practice - for over a list gives you the VALUES
# ============================================================
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # apple / banana / cherry

# `fruit` is the item itself, NOT its position.
# This is the single most common beginner mistake in Python.


# ============================================================
# Practice - range makes numbers, not a list you can see
# ============================================================
print(range(5))  # range(0, 5)  - lazy
print(list(range(5)))  # [0, 1, 2, 3, 4]

for i in range(3):
    print(i)  # 0 / 1 / 2

# range(stop)              -> 0 up to stop-1
# range(start, stop)       -> start up to stop-1
# range(start, stop, step) -> every step-th number
print(list(range(2, 10)))  # [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]

# the stop value is NEVER included - range(5) has no 5 in it


# ============================================================
# Practice - enumerate when you need the position too
# ============================================================
for index, fruit in enumerate(fruits):
    print(index, fruit)  # 0 apple / 1 banana / 2 cherry

# start counting from 1 instead of 0
for number, fruit in enumerate(fruits, start=1):
    print(f"{number}. {fruit}")  # 1. apple / 2. banana / 3. cherry

# do NOT do this - it works, but it is noisy and easy to get wrong
for i in range(len(fruits)):
    print(i, fruits[i])


# ============================================================
# Practice - zip walks two lists side by side
# ============================================================
names = ["kasun", "nimal", "sunil"]
scores = [90, 75, 60]

for name, score in zip(names, scores):
    print(f"{name:<8} {score}")

# zip stops at the SHORTER list - no error, it just ends early
short = [1, 2]
print(list(zip(names, short)))  # [('kasun', 1), ('nimal', 2)]


# ============================================================
# Practice - looping over a dict
# ============================================================
usage = {"prompt": 120, "completion": 45, "total": 165}

for key in usage:  # keys by default
    print(key)

for key, value in usage.items():  # key AND value - use this one
    print(f"{key:<12}: {value}")

for value in usage.values():
    print(value)


# ============================================================
# Practice - the accumulator pattern
# ============================================================
# Start with an empty container, add to it one item at a time.
# You will write this shape hundreds of times.

total = 0
for score in scores:
    total = total + score  # or: total += score
print(total)  # 225

long_fruits = []
for fruit in fruits:
    if len(fruit) > 5:
        long_fruits.append(fruit)
print(long_fruits)  # ['banana', 'cherry']

lookup = {}
for name, score in zip(names, scores):
    lookup[name] = score
print(lookup)  # {'kasun': 90, 'nimal': 75, 'sunil': 60}


# ============================================================
# Practice - while repeats until a condition turns False
# ============================================================
countdown = 3
while countdown > 0:
    print(countdown)  # 3 / 2 / 1
    countdown -= 1  # WITHOUT this line: infinite loop
print("go")

# Use `for` when you know how many times.
# Use `while` when you do not - retries, waiting, "until the user quits".


# ============================================================
# Practice - break stops the loop, continue skips one turn
# ============================================================
for n in [4, 8, 15, 16, 23, 42]:
    if n > 15:
        print("first one over 15:", n)  # 16
        break  # leave the loop entirely

for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 != 0:
        continue  # skip odd numbers, go to the next n
    print(n)  # 2 / 4 / 6


# ============================================================
# Practice - modifying a list while looping over it is a trap
# ============================================================
nums = [1, 2, 2, 3]
copy = nums.copy()  # loop over a COPY, edit the original
for n in copy:
    if n == 2:
        nums.remove(n)
print(nums)  # [1, 3]

# Looping over `nums` itself while removing from it skips items,
# because the list shrinks under the loop's feet.


# ============================================================
# Task A - total and average without sum()
# ============================================================
marks = [72, 85, 64, 91, 78]

total_marks = 0
for mark in marks:
    total_marks += mark

average = total_marks / len(marks)

print("Total:", total_marks)  # Total: 390
print(f"Average: {average:.2f}")  # Average: 78.00


# ============================================================
# Task B - numbered list
# ============================================================
tasks = ["setup", "python basics", "functions", "file io"]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")


# ============================================================
# Task C - build a dict from two lists
# ============================================================
models = ["haiku", "sonnet", "opus"]
prices = [0.25, 3.00, 15.00]

pricing = {}
for model, price in zip(models, prices):
    pricing[model] = price

for model, price in pricing.items():
    print(f"{model:<8}: ${price:.2f}")  # haiku   : $0.25


# ============================================================
# Task D - while loop with a budget
# ============================================================
budget = 100
cost_per_call = 30
calls = 0

# `>=` is the whole exercise. With `>` the budget would go negative,
# because we would make a call we cannot actually afford.
while budget >= cost_per_call:
    budget -= cost_per_call
    calls += 1
    print(budget)  # 70 / 40 / 10

print(f"{calls} calls")  # 3 calls


# ============================================================
# Task E - break and continue together
# ============================================================
responses = [
    {"text": "ok", "tokens": 12},
    {"text": "", "tokens": 0},
    {"text": "fine", "tokens": 40},
    {"text": "long answer", "tokens": 950},
    {"text": "never reached", "tokens": 5},
]

for response in responses:
    text = response["text"]
    tokens = response["tokens"]

    if not text:
        continue  # empty text - skip this one, keep going

    if tokens > 500:
        print("limit hit at:", text)  # limit hit at: long answer
        break  # stop the whole loop

    print(f"{text} ({tokens} tokens)")  # ok (12 tokens) / fine (40 tokens)
