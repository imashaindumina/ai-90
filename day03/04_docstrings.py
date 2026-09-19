# 04_docstrings.py
# Topic: docstrings - documenting what a function does

# ---------- Practice: short one-line docstring ----------
# Good enough for a simple, self-explanatory function.


def is_valid_email(email: str) -> bool:
    """Check whether email contains @ and a dot."""
    return "@" in email and "." in email


print(is_valid_email("a@b.com"))  # True
print(is_valid_email("nope"))  # False


# ---------- Practice: full docstring (Args / Returns) ----------
# Use this longer style when the function takes several arguments, or
# does something that isn't obvious from the name and type hints alone.


def call_cost(call: dict, prices: dict) -> float:
    """Calculate the dollar cost of one API call.

    Args:
        call: a dict with "model", "input", "output" keys.
        prices: maps a model name to {"input": x, "output": y}.

    Returns:
        The cost in dollars. 0.0 if the model is unknown.
    """
    model = call.get("model")
    rate = prices.get(model)

    if rate is None:
        return 0.0
    input_cost = call.get("input", 0) * rate.get("input", 0)
    output_cost = call.get("output", 0) * rate.get("output", 0)
    return input_cost + output_cost


PRICES = {
    "haiku": {"input": 0.001, "output": 0.005},
}

print(call_cost({"model": "haiku", "input": 100, "output": 50}, PRICES))
# 100*0.001 + 50*0.005 = 0.1 + 0.25 = 0.35
print(call_cost({"model": "unknown-model", "input": 100, "output": 50}, PRICES))
# 0.0  <- unknown model, safely handled


# ---------- Practice: reading a docstring back ----------
# A docstring is not a comment - Python actually stores it on the function.

print(call_cost.__doc__)
# prints the whole docstring text back

help(is_valid_email)
# shows the function signature + docstring, like looking up documentation


# ======================================================================
# TASKS
# ======================================================================


# Task 14
def double(n):
    """Return n doubled."""
    return n * 2


print("Task 14:", double(5))  # 10


# Task 15
def apply_discount(price, percent):
    """Return the price after taking off a percentage discount.

    Args:
        price: the original price.
        percent: the discount percentage to remove (e.g. 20 for 20%).

    Returns:
        The discounted price.
    """
    return price - (price * percent / 100)


print("Task 15:", apply_discount(100, 20))  # 80.0


# Task 16
print("Task 16:", apply_discount.__doc__)
