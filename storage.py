import json
from pathlib import Path


DATA_FILE = Path("study_data.json")


def load_sessions():
    if not DATA_FILE.exists():
        save_sessions([])
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("There was a problem reading the data file.")
        return []


def save_sessions(sessions):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(sessions, file, indent=4)

    except OSError:
        print("There was a problem saving the data.")