from storage import load_sessions


def show_summary():
    sessions = load_sessions()

    print("\n--- Study Summary ---")

    if len(sessions) == 0:
        print("No study sessions found.")
        return

    total_minutes = 0

    for session in sessions:
        total_minutes = total_minutes + session["minutes"]

    print("Total study sessions:", len(sessions))
    print("Total study time:", total_minutes, "minutes")

    subject_time = {}

    for session in sessions:
        subject = session["subject"]
        minutes = session["minutes"]

        if subject in subject_time:
            subject_time[subject] = subject_time[subject] + minutes
        else:
            subject_time[subject] = minutes

    print("\nSubject-wise study time:")

    for subject in subject_time:
        print(subject, ":", subject_time[subject], "minutes")