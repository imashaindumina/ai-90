"""Day 04 - text files: open()/with, write_text()/read_text(), append mode, mkdir/rename/unlink + Tasks 6-10."""

from pathlib import Path

script_dir = Path(__file__).parent
notes_folder = script_dir / "notes"
notes_folder.mkdir(exist_ok=True)
notes_file = notes_folder / "notes.txt"

# ==================== PRACTICE ====================

# ---------- 1. with open() - write then read ----------
with open(notes_file, "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

with open(notes_file, "r") as f:
    content = f.read()
print(content)

# ---------- 2. write_text() / read_text() - shortcut, always overwrites ----------
notes_file.write_text("Only line - previous content is gone\n")
print(notes_file.read_text())

# ---------- 3. append mode - "a" adds without erasing existing content ----------
with open(notes_file, "a") as f:
    f.write("Appended line\n")
print(notes_file.read_text())

# ---------- 4. mkdir(exist_ok=True) vs mkdir(parents=True, exist_ok=True) ----------
(script_dir / "notes").mkdir(exist_ok=True)  # no error if it already exists
(script_dir / "notes" / "sub").mkdir(
    parents=True, exist_ok=True
)  # creates any missing parent folders too

# ---------- 5. rename() - Windows raises an error if the destination already exists ----------
backup_file = notes_folder / "notes_backup.txt"
if backup_file.exists():
    backup_file.unlink()  # remove old backup first so rename() does not fail
notes_file.rename(backup_file)

# ---------- 6. unlink() - permanent delete, always check exists() first ----------
temp_file = notes_folder / "temp.txt"
temp_file.write_text("temporary\n")
if temp_file.exists():
    temp_file.unlink()
print("temp.txt deleted:", not temp_file.exists())


# ==================== TASKS 6-10 ====================

# ---- Task 6: create a "logs" folder, write log.txt with 3 lines using write_text() ----
logs_folder = script_dir / "logs"
logs_folder.mkdir(exist_ok=True)
log_file = logs_folder / "log.txt"
log_file.write_text("Started\nProcessing\nDone\n")

# ---- Task 7: read log.txt back and print each line separately ----
lines = log_file.read_text().splitlines()
for line in lines:
    print("log:", line)

# ---- Task 8: append a new line to log.txt without erasing what is already there ----
with open(log_file, "a") as f:
    f.write("Appended by Task 8\n")

# ---- Task 9: count how many lines are in log.txt now ----
line_count = len(log_file.read_text().splitlines())
print(f"log.txt has {line_count} lines")

# ---- Task 10: rename log.txt to log_backup.txt safely, then delete the original if it still exists ----
log_backup = logs_folder / "log_backup.txt"
if log_backup.exists():
    log_backup.unlink()
log_file.rename(log_backup)
print("log.txt exists:", log_file.exists())
print("log_backup.txt exists:", log_backup.exists())
