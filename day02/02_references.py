# Task 1

a = [1, 2, 3]
b = a
b.append(4)
print("Task 1 - a is:", a)
print("Task 1 - b is:", b)

# Task 2

a = [1, 2, 3]
b = a.copy()
b.append(4)
print("Task 2 - a:", a, "| b:", b)

# Task 3

a = [1, 2, 3]
b = a
c = a.copy()

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
print(a == c)

# Task 4

a = [1, 2, 3]
b = a
b.append(4)
print(f"Task 4 a={a},b={b}")

# Task 5

x = 5
y = x
y += 1
print(f"Task 5 x={x},y={y}")

# Task 6


def sort_scores(scores):
    """Sorts and returns the scores."""
    scores.sort()
    return scores


client_data = [90, 30, 75]
result = sort_scores(client_data)
print(f"Task 6 results ={result}")
print(f"Task 6 client data ={client_data}")
