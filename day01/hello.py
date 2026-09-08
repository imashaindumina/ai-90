"""Environment report — verifies the Python setup is correct.

Run this after setting up a new project to confirm you are using
the project's virtual environment and not a system-wide Python.
"""

import sys
import platform
from pathlib import Path


def environment_report() -> dict:
    """Collect facts about the Python interpreter running this script."""

    # A venv changes sys.prefix but keeps sys.base_prefix pointing at
    # the original Python install. If they differ, we are inside a venv.
    in_venv = sys.prefix != sys.base_prefix

    return {
        "python": platform.python_version(),  # e.g. "3.12.0"
        "os": f"{platform.system()} {platform.release()}",
        "venv_active": in_venv,  # True / False
        "interpreter": sys.executable,  # full path to python.exe
        "project": Path.cwd().name,  # current folder name
    }


def main() -> None:
    """Print the report in a readable block."""

    report = environment_report()

    print("=" * 46)
    print("  ENVIRONMENT REPORT")
    print("=" * 46)

    # .items() gives us each key/value pair from the dict
    for key, value in report.items():
        # :<12 pads the key to 12 characters so the colons line up
        print(f"  {key:<12} : {value}")

    print("=" * 46)

    if report["venv_active"]:
        print("  OK  - virtual environment is active")
    else:
        print("  !!  - venv not active. Run: .venv\\Scripts\\Activate.ps1")


# Only run main() when this file is executed directly,
# not when it is imported by another file.
if __name__ == "__main__":
    main()
