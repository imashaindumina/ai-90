from pathlib import Path
import json

script_dir = Path(__file__).parent
data_folder = script_dir / "data"
data_folder.mkdir(exist_ok=True)

person = {"name": "Imasha", "Age": 22, "skills": ["Python", "AI"]}
json_text = json.dumps(person)
print(json_text)
print(type(json_text))

print(json.dumps(person, indent=2))

raw = '{"city":"Colombo","temp":29.4}'
parsed = json.loads(raw)
print(parsed["city"])
print(type(parsed))

person_file = data_folder / "person.json"
with open(person_file, "w") as f:
    json.dump(person, f, indent=2)

with open(person_file, "r") as f:
    loaded = json.load(f)
print(loaded["name"], loaded["skills"])

config = {"api": {"key": "abc123", "timeout": 10}}
timeout = config.get("api", {}.get("timeout"))
retries = config.get("api", {}).get("retries", 3)
print("timeout:", timeout)
print("retries:", retries)

book = {"title": "Automic Habits", "author": "james Clear", "pages": 320}
book_json_text = json.dumps(book, indent=2)
print(book_json_text)


book_file = data_folder / "book.json"
with open(book_file, "w") as f:
    json.dump(book, f, indent=2)

with open(book_file, "r") as f:
    loaded_book = json.load(f)
print("Title:", loaded_book["title"])

loaded_book["read"] = True
with open(book_file, "w") as f:
    json.dump(loaded_book, f, indent=2)
print(book_file.read_text())

rating = loaded_book.get("rating", "Not rated yet")
print("Rating:", rating)

broken_file = data_folder / "broken.json"
broken_file.write_text("{not valid json}")

try:
    with open(broken_file, "r") as f:
        json.load(f)
except json.JSONDecodeError:
    print("broken.json is not valid JSON-skipping it")
