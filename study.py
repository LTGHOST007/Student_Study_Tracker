from storage import load_sessions, save_sessions
from validator import get_valid_text, get_valid_minutes


def add_session():
    sessions = load_sessions()

    print("\n--- Add Study Session ---")

    subject = get_valid_text("Enter subject: ")
    topic = get_valid_text("Enter topic: ")
    minutes = get_valid_minutes("Enter study time in minutes: ")

    new_session = {
        "id": len(sessions) + 1,
        "subject": subject,
        "topic": topic,
        "minutes": minutes
    }

    sessions.append(new_session)
    save_sessions(sessions)

    print("Study session added.")


def view_sessions():
    sessions = load_sessions()

    print("\n--- Study Sessions ---")

    if not sessions:
        print("No sessions available.")
        return

    for session in sessions:
        print(
            "ID:", session["id"],
            "| Subject:", session["subject"],
            "| Topic:", session["topic"],
            "| Time:", session["minutes"], "minutes"
        )


def delete_session():
    sessions = load_sessions()

    if not sessions:
        print("There are no sessions to delete.")
        return

    view_sessions()

    try:
        session_id = int(input("Enter the session ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for session in sessions:
        if session["id"] == session_id:
            sessions.remove(session)
            save_sessions(sessions)
            print("Study session deleted.")
            return

    print("Session ID was not found.")