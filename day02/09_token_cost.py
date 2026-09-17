"""Day 2 mini project - LLM token cost report.

Everything from files 01-08 comes together here:
  dicts (.get chaining)   -> 05
  loops + accumulator     -> 07
  comprehensions          -> 08
  f-string alignment      -> 01
  conditionals            -> 06
  functions               -> 02
"""

# ============================================================
# Given data - do not change
# ============================================================
# Example prices in US dollars per 1,000,000 tokens.
PRICING = {
    "haiku":  {"in": 0.25,  "out": 1.25},
    "sonnet": {"in": 3.00,  "out": 15.00},
    "opus":   {"in": 15.00, "out": 75.00},
}

# Eight API responses. Some are messy on purpose:
#   r3 has empty text        r5 has an empty usage dict
#   r7 is a model we have no price for
RESPONSES = [
    {"id": "r1", "model": "haiku",  "text": "ok",           "usage": {"input_tokens": 120,  "output_tokens": 45}},
    {"id": "r2", "model": "sonnet", "text": "summary...",   "usage": {"input_tokens": 3400, "output_tokens": 820}},
    {"id": "r3", "model": "haiku",  "text": "",             "usage": {"input_tokens": 90,   "output_tokens": 0}},
    {"id": "r4", "model": "opus",   "text": "long answer",  "usage": {"input_tokens": 8200, "output_tokens": 1950}},
    {"id": "r5", "model": "sonnet", "text": "retry",        "usage": {}},
    {"id": "r6", "model": "haiku",  "text": "fine",         "usage": {"input_tokens": 200,  "output_tokens": 60}},
    {"id": "r7", "model": "gemini", "text": "other vendor", "usage": {"input_tokens": 500,  "output_tokens": 100}},
    {"id": "r8", "model": "sonnet", "text": "done",         "usage": {"input_tokens": 1500, "output_tokens": 300}},
]


# ============================================================
# Step 1 - read usage safely
# ============================================================
def usage_of(r):
    """Return (input_tokens, output_tokens) for one response.

    r5 has an empty usage dict. This must NOT crash.
    """
    u = r.get("usage", {})
    return u.get("input_tokens", 0), u.get("output_tokens", 0)


# ============================================================
# Step 2 - price one response
# ============================================================
def cost_of(r):
    """Return the dollar cost of one response, or None if we have no price.

    r7 uses a model that is not in PRICING - return None for it.
    Do NOT return 0: zero cost and unknown cost are different facts.
    """
    price = PRICING.get(r.get("model"))
    if price is None:
        return None

    tokens_in, tokens_out = usage_of(r)
    return (tokens_in / 1_000_000) * price["in"] + (tokens_out / 1_000_000) * price["out"]


# ============================================================
# Step 3 - the table
# ============================================================
# Header. The widths here must match the data rows below, or nothing lines up.
print(f"{'ID':<5}{'MODEL':<9}{'IN':>8}{'OUT':>8}{'COST':>11}  STATUS")
print("-" * 52)

for r in RESPONSES:
    tokens_in, tokens_out = usage_of(r)
    cost = cost_of(r)

    # The order of these checks IS the exercise.
    if cost is None:
        cost_text = "-"
        status = "unknown model"
    else:
        cost_text = f"${cost:.6f}"
        status = "no output" if tokens_out == 0 else "ok"

    # Empty text wins over everything else - it is the more useful fact.
    if not r["text"]:
        status = "empty text"

    print(f"{r['id']:<5}{r['model']:<9}{tokens_in:>8,}{tokens_out:>8,}{cost_text:>11}  {status}")


# ============================================================
# Step 4 - totals
# ============================================================
# Only the responses we can actually price. r7 drops out here.
priced = [r for r in RESPONSES if cost_of(r) is not None]

total_cost = sum(cost_of(r) for r in priced)
total_in = sum(usage_of(r)[0] for r in priced)
total_out = sum(usage_of(r)[1] for r in priced)

print("-" * 52)
print(f"{'TOTAL':<14}{total_in:>8,}{total_out:>8,}{'$' + format(total_cost, '.6f'):>11}")
print()


# ============================================================
# Step 5 - cost by model
# ============================================================
# The counting pattern from 05_dicts.py, adding a cost instead of a 1.
by_model = {}
for r in priced:
    model = r["model"]
    by_model[model] = by_model.get(model, 0.0) + cost_of(r)

print("BY MODEL")
for model, cost in sorted(by_model.items(), key=lambda kv: kv[1], reverse=True):
    share = cost / total_cost * 100
    bar = "#" * int(share / 2)
    print(f"  {model:<9}${cost:.6f}  {share:>5.1f}%  {bar}")

print()


# ============================================================
# Step 6 - three facts a client would ask for
# ============================================================
skipped = len(RESPONSES) - len(priced)
no_output = len([r for r in priced if usage_of(r)[1] == 0])
per_1000 = total_cost / len(priced) * 1000

print(f"skipped (no pricing): {skipped}")
print(f"calls with no output: {no_output}")
print(f"cost per 1,000 calls: ${per_1000:.2f}")
