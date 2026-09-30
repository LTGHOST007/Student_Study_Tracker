def get_valid_text(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("This field cannot be empty.")


def get_valid_minutes(message):
    while True:
        try:
            minutes = int(input(message))

            if minutes <= 0:
                print("Study time must be greater than 0.")
            else:
                return minutes

        except ValueError:
            print("Please enter a whole number.")