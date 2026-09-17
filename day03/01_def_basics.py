"""Day 3 - def basics."""

# ============================================================
# Practice - the shape of a function
# ============================================================
def greet(name):                      # def, name, (parameters), colon
    """Return a greeting."""          # docstring - what it does
    return f"hello, {name}!"          # return - hands a value back


print(greet("imasha"))                # hello, imasha!

# Defining is not calling. `greet` is the function itself;
# `greet("x")` runs it.
print(greet)                          # <function greet at 0x...>


# ============================================================
# Practice - print and return are NOT the same thing
# ============================================================
def add_print(a, b):
    print(a + b)                      # shows it on screen, hands back nothing

def add_return(a, b):
    return a + b                      # hands the value back to the caller


x = add_print(2, 3)                   # prints 5
print(x)                              # None   <- nothing came back

y = add_return(2, 3)                  # prints nothing
print(y)                              # 5      <- the value came back
print(y * 2)                          # 10     <- and you can use it

# A function with no `return` returns None. Always.
# If you want to USE the result, you must `return` it.


# ============================================================
# Practice - a function can return early
# ============================================================
def describe(n):
    if n < 0:
        return "negative"             # stops here, the rest never runs
    if n == 0:
        return "zero"
    return "positive"


print(describe(-5), describe(0), describe(7))   # negative zero positive


# ============================================================
# Practice - naming
# ============================================================
# A function gets an ACTION name.  A parameter gets a THING name.
#
#   def name(name):   <- the parameter hides the function inside the body
#   def greet(name):  <- clear, and the function stays reachable
#
# The same rule protects Python's own names: never call a variable
# `list`, `sum`, `dict`, `str` or `id` - you lose the builtin.


# ============================================================
# Task 1 - greet
# ============================================================
def greet_person(name):
    """Return a greeting for one person."""
    return f"Hello {name}"


print("Task 1:", greet_person("Imasha"))        # Hello Imasha


# ============================================================
# Task 2 - multiply
# ============================================================
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


print("Task 2:", multiply(3, 4))                # 12


# ============================================================
# Task 3 - average, without crashing
# ============================================================
def average(nums):
    """Return the average of a list. An empty list gives 0, not a crash.

    The guard clause runs first, so len(nums) is never 0 by the time we
    divide. Without it an empty list raises ZeroDivisionError.
    """
    if not nums:
        return 0
    return sum(nums) / len(nums)


print("Task 3:", average([10, 20, 30]))         # 20.0
print("Task 3:", average([]))                   # 0


# ============================================================
# Task 4 - find the bug
# ============================================================
# The bug: the original add() used print() instead of return.
#
#   def add(a, b):
#       print(a + b)        <- shows 5 on screen, hands back nothing
#
#   result = add(2, 3)      <- result is None
#   print(result * 2)       <- TypeError: unsupported operand type(s)
#                              for *: 'NoneType' and 'int'
#
# It LOOKS like it works, because 5 does get printed. It only fails on
# the next line, when something tries to use the value.
#
# The fix: return the value instead of printing it.
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


result = add(2, 3)
print("Task 4:", result * 2)                    # 10
