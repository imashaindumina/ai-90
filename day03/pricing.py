PRICES = {"opus": 0.015, "haiku": 0.0008}


def cost(tokens: int, model: str) -> float:
    return tokens / 1000 * PRICES.get(model, 0.0)


if __name__ == "__main__":
    print(cost(1500, "opus"))
