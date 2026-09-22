"""Day 04 - pathlib basics: path parts, exists/stat, iterdir/glob/rglob + Tasks 1-5."""

from pathlib import Path

# ==================== PRACTICE ====================

# ---------- 1. Create a Path and inspect its parts ----------
report = Path("demo_folder/report.pdf")
print(report.name)  # report.pdf
print(report.stem)  # report
print(report.suffix)  # .pdf
print(report.parent)  # demo_folder

# ---------- 2. Check if the path exists ----------
if not report.exists():
    print(f"File not found: {report}")
else:
    print(f"{report} is {report.stat().st_size} bytes")

# ---------- 3. iterdir(), glob(), rglob() - listing a folder ----------
downloads = Path.home() / "Downloads"

if downloads.exists():
    for item in downloads.iterdir():
        print("item:", item.name)

    for f in downloads.iterdir():
        if f.is_file():
            print("file:", f.name)

    for f in downloads.glob("*.pdf"):
        print("pdf:", f.name)

    for f in downloads.rglob("*.pdf"):
        print("pdf (recursive):", f)
else:
    print(f"{downloads} does not exist")


# ==================== TASKS 1-5 ====================

# ---- Task 1: print Path.home(), then join it with "code/day04" and print that too ----
print(Path.home())
print(Path.home() / "code" / "day04")

# ---- Task 2: print name, stem, suffix, parent for the path below ----
p2 = Path("C:/data/report_2026.csv")
print(p2.name)
print(p2.stem)
print(p2.suffix)
print(p2.parent)

# ---- Task 3: count how many files are in the Downloads folder ----
downloads = Path.home() / "Downloads"
files = [f for f in downloads.iterdir() if f.is_file()]
print(f"Files: {len(files)}")

# ---- Task 4: check if there are any .pdf files in Downloads, print them ----
pdfs = list(downloads.glob("*.pdf"))
if not pdfs:
    print("No PDF files found")
else:
    for pdf in pdfs:
        print(pdf.name)

# ---- Task 5: count files in Downloads by extension ----
counts: dict[str, int] = {}
for f in downloads.iterdir():
    if f.is_file():
        ext = f.suffix.lower() or "(no ext)"
        counts[ext] = counts.get(ext, 0) + 1
for ext, n in sorted(counts.items()):
    print(f"{ext} : {n}")
