"""Day 04 - os/shutil: shutil.copy(), shutil.move(), shutil.rmtree(), os.remove() + Tasks 20-21."""

import os
import shutil
from pathlib import Path

script_dir = Path(__file__).parent
data_folder = script_dir / "data"
data_folder.mkdir(exist_ok=True)

# ==================== PRACTICE ====================

# ---------- 1. shutil.copy() - copy a file (original stays where it is) ----------
source_file = data_folder / "students.csv"
if not source_file.exists():
    source_file.write_text("name,score\nNimal,78\nSaman,85\n")

copy_file = data_folder / "students_copy.csv"
shutil.copy(source_file, copy_file)
print("copy exists:", copy_file.exists())
print("original still exists:", source_file.exists())

# ---------- 2. shutil.move() - move/rename a file (original is gone after) ----------
archive_folder = script_dir / "archive"
archive_folder.mkdir(exist_ok=True)
moved_file = archive_folder / "students_copy.csv"
shutil.move(copy_file, moved_file)
print("moved file exists:", moved_file.exists())
print(
    "old location exists now:", copy_file.exists()
)  # False - it moved, it did not copy

# ---------- 3. os.remove() - delete a single file (same as Path.unlink()) ----------
temp_file = data_folder / "temp.txt"
temp_file.write_text("temporary\n")
os.remove(temp_file)
print("temp.txt deleted:", not temp_file.exists())

# ---------- 4. shutil.rmtree() - delete a folder and everything inside it ----------
scratch_folder = script_dir / "scratch"
scratch_folder.mkdir(exist_ok=True)
(scratch_folder / "a.txt").write_text("a")
(scratch_folder / "b.txt").write_text("b")
shutil.rmtree(scratch_folder)
print("scratch folder deleted:", not scratch_folder.exists())


# ==================== TASKS 20-21 ====================

# ---- Task 20: copy students.csv to backup_students.csv, confirm both files exist ----
backup_file = data_folder / "backup_students.csv"
shutil.copy(source_file, backup_file)
print("students.csv exists:", source_file.exists())
print("backup_students.csv exists:", backup_file.exists())

# ---- Task 21: move backup_students.csv into the archive folder, then remove students_copy.csv from archive ----
shutil.move(backup_file, archive_folder / "backup_students.csv")
print("backup moved to archive:", (archive_folder / "backup_students.csv").exists())

leftover_file = archive_folder / "students_copy.csv"
if leftover_file.exists():
    os.remove(leftover_file)
print("leftover copy removed:", not leftover_file.exists())
