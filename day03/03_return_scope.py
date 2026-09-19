# 03_return_scope.py
# Topic: return values and variable scope (LEGB rule)

# ---------- Practice: local scope ----------
# A variable created INSIDE a function only exists inside that function.


def make_total():
    subtotal = 100  # local to make_total
    tax = subtotal * 0.1
    return subtotal + tax


print(make_total())  # 110.0

# print(subtotal)            # NameError: 'subtotal' is not defined
# print(tax)                 # NameError - neither name escapes the function


# ---------- Practice: local shadows global (reading) ----------

city = "Colombo"  # global


def show_city():
    city = "Kandy"  # this is a DIFFERENT variable, local to show_city
    print("inside:", city)


show_city()  # inside: Kandy
print("outside:", city)  # outside: Colombo   <- global was never touched


# ---------- Practice: reading a global is fine without 'global' ----------

rate = 250  # global


def price_in_rupees(usd):
    return usd * rate  # just READING rate - no 'global' keyword needed


print(price_in_rupees(10))  # 2500


# ---------- Practice: the classic UnboundLocalError trap ----------


def broken_counter():
    print(count)  # tries to read "count"
    count = count + 1  # ...but this assignment makes count LOCAL
    return count  # everywhere in this function


count = 0  # a global, unrelated to the crash below
# broken_counter()             # UnboundLocalError: cannot access local
# variable 'count' where it is not associated
# with a value


# ---------- Practice: fixing it with 'global' ----------

visits = 0  # global


def log_visit():
    global visits  # tells Python: use the OUTER visits, don't make a local one
    visits += 1
    return visits


print(log_visit())  # 1
print(log_visit())  # 2
print("total visits:", visits)  # 2


# ---------- Practice: LEGB rule (Local, Enclosing, Global, Built-in) ----------

message = "global message"  # Global


def outer():
    message = "enclosing message"  # Enclosing (relative to inner)

    def inner():
        message = "local message"  # Local
        print(message)  # finds it in Local - stops looking

    inner()


outer()  # local message


def outer_no_local():
    message = "enclosing message"

    def inner_no_local():
        print(message)  # no local 'message' here, so Python looks
        # one level out - finds it in Enclosing

    inner_no_local()


outer_no_local()  # enclosing message


# ---------- Practice: return still ends the function immediately ----------


def first_negative(nums):
    """Return the first negative number in the list, or None if there isn't one."""
    for n in nums:
        if n < 0:
            return n  # exits the function AND the loop immediately
    return None  # only reached if the loop never returned


print(first_negative([3, 5, -2, 8]))  # -2
print(first_negative([3, 5, 8]))  # None


# ======================================================================
# TASKS
# ======================================================================


# Task 10
def bank_balance():
    """Return a local balance. This value never exists outside the function."""
    balance = 500
    return balance


print("Task 10:", bank_balance())  # 500
# print(balance)                      # NameError: 'balance' is not defined
#                                      # (balance only exists inside bank_balance)


# Task 11
score = 0  # global


def add_point_broken():
    print(score)  # tries to READ the global score first
    score = score + 1  # ...but this assignment makes score LOCAL
    return score  # for the whole function - so the read above fails


# My prediction: UnboundLocalError, because assigning to "score" anywhere
# in this function makes Python treat it as local for the whole function,
# even on the print(score) line before the assignment.

try:
    add_point_broken()
except UnboundLocalError as e:
    print("Task 11:", type(e).__name__, "-", e)
# Confirmed: UnboundLocalError, as predicted.
# (using try/except here just to stop the crash from stopping the whole
#  file - we'll learn try/except properly in 05_try_except.py)


# Task 12
def add_point():
    """Fixed version: 'global' tells Python to use the real outer score."""
    global score
    score = score + 1
    return score


print("Task 12:", add_point())  # 1
print("Task 12:", add_point())  # 2
print("Task 12: score is now", score)  # 2


# Task 13
total = 0  # global


def running_total(n):
    """Add n to the global total and return the new total."""
    global total
    total += n
    return total


print("Task 13:", running_total(10))  # 10
print("Task 13:", running_total(5))  # 15
print("Task 13:", running_total(20))  # 35
