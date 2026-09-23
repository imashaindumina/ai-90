"""Day 04 - CSV: csv.writer/reader, csv.DictWriter/DictReader + Tasks 16-19."""

import csv
from pathlib import Path

script_dir = Path(__file__).parent
data_folder = script_dir / "data"
data_folder.mkdir(exist_ok=True)

# ==================== PRACTICE ====================

# ---------- 1. csv.writer - write rows (lists) to a csv file ----------
people_file = data_folder / "people.csv"
with open(people_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])  # header row
    writer.writerow(["Imasha", 24])
    writer.writerow(["Kasun", 30])

# ---------- 2. csv.reader - read rows back as lists ----------
with open(people_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # every value comes back as a string, even 24

# ---------- 3. csv.DictWriter - write rows as dicts, using fieldnames ----------
fieldnames = ["name", "age"]
with open(people_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Imasha", "age": 24})
    writer.writerow({"name": "Kasun", "age": 30})

# ---------- 4. csv.DictReader - read rows back as dicts ----------
with open(people_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], "-", row["age"])

# ---------- 5. CSV values are always strings - convert numbers yourself ----------
with open(people_file, "r") as f:
    reader = csv.DictReader(f)
    ages = [int(row["age"]) for row in reader]
print("ages:", ages)
print("total age:", sum(ages))


# ==================== TASKS 16-19 ====================

# ---- Task 16: write student records (name, score) to students.csv using csv.writer ----
students_file = data_folder / "students.csv"
students = [
    ["name", "score"],
    ["Nimal", 78],
    ["Saman", 85],
    ["Kamala", 62],
    ["Ruwan", 91],
]
with open(students_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

# ---- Task 17: read students.csv back using csv.reader, print each row ----
with open(students_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("row:", row)

# ---- Task 18: use DictReader, convert score to int, compute the average score ----
with open(students_file, "r") as f:
    reader = csv.DictReader(f)
    scores = [int(row["score"]) for row in reader]
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score:.1f}")

# ---- Task 19: write students who scored above average to passed_students.csv ----
passed_file = data_folder / "passed_students.csv"
with open(students_file, "r") as f:
    reader = csv.DictReader(f)
    passed = [row for row in reader if int(row["score"]) > average_score]

with open(passed_file, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(passed)

print("Passed students:", [p["name"] for p in passed])
