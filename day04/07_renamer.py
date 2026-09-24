"""Day 04 capstone - renamer.py: batch-rename files safely, with a dry-run mode and a JSON log."""

import json
from datetime import datetime
from pathlib import Path

script_dir = Path(__file__).parent
sample_folder = script_dir / "sample_photos"
log_file = script_dir / "data" / "rename_log.json"


# ---- Task 22: list files in a folder that match a given extension ----
def list_files(folder: Path, extension: str) -> list[Path]:
    """Return all files in folder matching the given extension, e.g. '.jpg'."""
    if not folder.exists():
        return []
    return sorted(folder.glob(f"*{extension}"))


# ---- Task 23: build a new sequential name like "photo_001.jpg" ----
def build_new_name(index: int, extension: str, prefix: str = "photo") -> str:
    """Build a new file name with 3-digit zero-padded numbering."""
    return f"{prefix}_{index:03d}{extension}"


# ---- Task 24: rename files safely, with a dry_run option and no overwriting ----
def rename_files(
    folder: Path, extension: str, prefix: str = "photo", dry_run: bool = True
) -> list[dict]:
    """
    Rename every matching file in folder to a sequential name.
    dry_run=True only previews the renames without touching any file.
    Returns a list of {"old": ..., "new": ...} actions.
    """
    files = list_files(folder, extension)
    actions = []

    for i, old_path in enumerate(files, start=1):
        new_name = build_new_name(i, extension, prefix)
        new_path = folder / new_name

        if new_path.exists() and new_path != old_path:
            print(f"Skipping {old_path.name} - {new_name} already exists")
            continue

        actions.append({"old": old_path.name, "new": new_name})

        if not dry_run:
            old_path.rename(new_path)

    return actions


# ---- Task 25: log every rename action to a JSON file, with a timestamp ----
def log_actions(actions: list[dict]) -> None:
    """Append this run's rename actions to the JSON log file."""
    log_file.parent.mkdir(exist_ok=True)

    if log_file.exists():
        history = json.loads(log_file.read_text())
    else:
        history = []

    history.append(
        {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "actions": actions,
        }
    )

    with open(log_file, "w") as f:
        json.dump(history, f, indent=2)


def main():
    sample_folder.mkdir(exist_ok=True)
    # create a few sample files to rename, only if the folder is empty
    if not list(sample_folder.glob("*.jpg")):
        for name in ["IMG_2381.jpg", "holiday pic.jpg", "screenshot(3).jpg"]:
            (sample_folder / name).touch()

    print("--- dry run (preview only, nothing renamed yet) ---")
    preview = rename_files(sample_folder, ".jpg", prefix="photo", dry_run=True)
    for action in preview:
        print(f"{action['old']}  ->  {action['new']}")

    print("\n--- applying the rename for real ---")
    applied = rename_files(sample_folder, ".jpg", prefix="photo", dry_run=False)
    log_actions(applied)

    print("\nFiles now in the folder:")
    for f in sorted(sample_folder.glob("*.jpg")):
        print(" -", f.name)

    print(f"\nLog saved to: {log_file}")


if __name__ == "__main__":
    main()
