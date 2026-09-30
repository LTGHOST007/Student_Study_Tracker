from study import add_session, view_sessions, delete_session

from report import show_summary

from storage import load_sessions


def show_menu():
	print("\n==============================")
	print("      STUDENT STUDY TRACKER")
	print("==============================")
	print("1. Add Study Session")
	print("2. View Study Sessions")
	print("3. Study Summary")
	print("4. Delete Study Session")
	print("5. Exit")
	print("==============================")

def main():
	load_sessions()

	while True:
		show_menu()
		choice = input("Enter your choice: ")

		if choice == "1":
			add_session()
		elif choice == "2":
			view_sessions()
		elif choice == "3":
			show_summary()
		elif choice == "4":
			delete_session()
		elif choice == "5":
			print("Thank you for using Student Study Tracker!")
			break
		else:
			print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
	main()