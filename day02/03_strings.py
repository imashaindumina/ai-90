"""Day 2 — strings, f-strings and slicing."""

# ============================================================
# Practice — f-string formatting
# ============================================================
cost = 0.00456789
tokens = 1234567
ratio = 0.8734

print(f"{cost:.4f}")        # 0.0046      — 4 decimal places
print(f"{tokens:,}")        # 1,234,567   — thousands separator
print(f"{ratio:.1%}")       # 87.3%       — percentage
print(f"{42:05d}")          # 00042       — leading zeros
print(f"{'name':<10}|")     # left aligned, width 10
print(f"{'name':>10}|")     # right aligned
print(f"{'name':^10}|")     # centred

x = 42
print(f"{x=}")              # x=42  — prints name AND value, great for debugging


# ============================================================
# Practice — indexing and slicing
# ============================================================
s = "python"
#    0 1 2 3 4 5
#   -6-5-4-3-2-1

print(s[0])        # p       first character
print(s[-1])       # n       last character
print(s[:3])       # pyt     first 3
print(s[3:])       # hon     from index 3 to the end
print(s[::-1])     # nohtyp  reversed  (start:stop:STEP)
print(s[::2])      # pto     every 2nd character


# ============================================================
# Task 5 — clean up a messy string
# ============================================================
messy = "  Hello World  "
print(messy.strip().upper())        # HELLO WORLD

# Methods chain left to right: strip() runs first, then upper()
name = "  Imasha IndUmINa  "
print(name.strip().lower())         # imasha indumina


# ============================================================
# Task 6 — reverse a string
# ============================================================
word = "python"
print(word[::-1])                   # nohtyp


# ============================================================
# Task 7 — split and number the pieces
# ============================================================
data = "imasha,colombo,srilanka"

parts = data.split(",")             # "," is WHERE to cut, not what to keep
print(parts)                        # ['imasha', 'colombo', 'srilanka']

for i, part in enumerate(parts, start=1):
    print(f"{i}. {part}")
# 1. imasha
# 2. colombo
# 3. srilanka


# ============================================================
# Task 8 — format numbers for a report
# ============================================================
cost = 0.00456789
tokens = 1234567

print(f"Cost: ${cost:.4f}")         # Cost: $0.0046
print(f"Tokens: {tokens:,}")        # Tokens: 1,234,567


# ============================================================
# Task 9 — palindrome check
# ============================================================
def is_palindrome(word):
    """Returns True if the word reads the same backwards."""
    w = word.lower()                # lowercase ONCE, use it on both sides
    return w == w[::-1]             # the comparison IS the boolean


print(is_palindrome("malayalam"))   # True
print(is_palindrome("Python"))      # False
print(is_palindrome("Racecar"))     # True  — works because of .lower()
