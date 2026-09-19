# 02_arguments.py
# Topic: function arguments - positional, keyword, defaults, *args, **kwargs

# ---------- Practice: positional vs keyword arguments ----------


def send(message, channel, urgent):
    """Print a message in a fixed format."""
    flag = "URGENT" if urgent else "normal"
    print(f"[{channel}] ({flag}) {message}")


# Positional - order matters
send("Server down", "ops", True)

# Keyword - order does not matter, names do
send(channel="ops", urgent=True, message="Server down")

# Mixing is allowed, but positional args must come first
send("Server down", channel="ops", urgent=True)


# ---------- Practice: default arguments ----------


def call_model(prompt, model="haiku", temperature=0.0, stream=False):
    """Pretend to call an LLM. Defaults let us skip args we don't care about."""
    return f"model={model} temp={temperature} stream={stream} prompt={prompt!r}"


print(call_model("Hi"))
print(call_model("Hi", model="opus"))
print(call_model("Hi", temperature=0.7))


# ---------- Practice: the mutable default argument bug ----------


def add_tag_broken(tag, tags=[]):
    """BROKEN: the default list is created ONCE, when the function is
    defined - not each time it is called. Every call that skips 'tags'
    shares and mutates the SAME list.
    """
    tags.append(tag)
    return tags


print(add_tag_broken("python"))  # ['python']
print(add_tag_broken("ai"))  # ['python', 'ai']  <- unexpected!
print(add_tag_broken("freelance"))  # ['python', 'ai', 'freelance']  <- keeps growing


def add_tag(tag, tags=None):
    """FIXED: use None as the default, create a fresh list inside the
    function body each time.
    """
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


print(add_tag("python"))  # ['python']
print(add_tag("ai"))  # ['ai']  <- fresh list every time


# ---------- Practice: *args (extra positional arguments -> tuple) ----------


def totals(*numbers):
    """*numbers collects any number of positional args into a tuple."""
    print(type(numbers), numbers)
    return sum(numbers)


print(totals(1, 2, 3))  # (1,2,3) tuple, then 6
print(totals())  # () empty tuple, then 0


# ---------- Practice: **kwargs (extra keyword arguments -> dict) ----------


def describe(**fields):
    """**fields collects any number of keyword args into a dict."""
    print(type(fields), fields)
    return fields


describe(name="Imasha", role="freelancer")


# ---------- Practice: full parameter ordering ----------
# order: positional, *args, keyword-only, **kwargs


def report(title, *rows, sep="-", **meta):
    print(f"{title} | rows={rows} | sep={sep} | meta={meta}")


report("Usage", "a", "b", sep="=", owner="imasha")
# Usage | rows=('a', 'b') | sep== | meta={'owner': 'imasha'}


# ---------- Practice: unpacking at the call site ----------

nums = [10, 20, 30]
print(totals(*nums))  # same as totals(10, 20, 30)

opts = {"model": "opus", "stream": True}
print(call_model("hi", **opts))  # same as call_model("hi", model="opus", stream=True)


# ======================================================================
# TASKS
# ======================================================================


# Task 5
# greet(name, greeting="Hello") -> "<greeting>, <name>!"
def greet(name, greeting="Hello"):
    """Return a greeting. Uses 'Hello' unless a different greeting is given."""
    return f"{greeting}, {name}!"


print("Task 5:", greet("Imasha"))  # Hello, Imasha!
print("Task 5:", greet("Imasha", greeting="Hi"))  # Hi, Imasha!


# Task 6
# Predict what add_tag_broken("java") would print if called RIGHT HERE,
# after everything above already ran.
# My prediction: ['python', 'ai', 'freelance', 'java']
# (the same shared list from before, with "java" appended on top)
print("Task 6:", add_tag_broken("java"))
# Confirmed: ['python', 'ai', 'freelance', 'java']


# Task 7
# Own corrected version - proves no state is shared between calls.
def add_label(label, labels=None):
    """Fixed version: fresh list every call, nothing carries over."""
    if labels is None:
        labels = []
    labels.append(label)
    return labels


print("Task 7:", add_label("urgent"))  # ['urgent']
print("Task 7:", add_label("draft"))  # ['draft']  <- proves it did NOT keep growing


# Task 8
# biggest(*numbers) -> largest number, or None if no numbers were passed.
def biggest(*numbers):
    """Return the largest number, or None for an empty call.

    max([]) raises ValueError, so we guard against zero args first
    instead of letting the crash happen.
    """
    if not numbers:
        return None
    return max(numbers)


print("Task 8:", biggest(3, 9, 1))  # 9
print("Task 8:", biggest())  # None


# Task 9
# settings(**options) -> ["key = value", ...] list, built with a comprehension.
def settings(**options):
    """Return a list of 'key = value' strings from any keyword arguments."""
    return [f"{key} = {value}" for key, value in options.items()]


print("Task 9:", settings(host="local", port=8000))
# ['host = local', 'port = 8000']
