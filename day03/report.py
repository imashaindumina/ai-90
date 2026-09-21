calls = [
    {"model": "opus", "input": 1200, "output": 340},
    {"model": "haiku", "input": 8000, "output": 120},
    {"model": "opus", "input": 450, "output": 900},
]

prices = {
    "opus": {"input": 0.015, "output": 0.075},
    "haiku": {"input": 0.0008, "output": 0.004},
}

total = 0
for i, c in enumerate(calls, start=1):
    p = prices[c["model"]]
    cost = c["input"] / 1000 * p["input"] + c["output"] / 1000 * p["output"]
    total += cost
    print(f"{i}.{c['model']:<6} ${cost:.4f}")

print(f"\ntotal cost: ${total:.4f}")

by_model = {}
for c in calls:
    p = prices[c["model"]]
    cost = c["input"] / 1000 * p["input"] + c["output"] / 1000 * p["output"]
    by_model[c["model"]] = by_model.get(c["model"], 0) + cost

for m, v in by_model.items():
    print(f"{m:<6} ${v:.4f}")
