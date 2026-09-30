Student Study Tracker

Overview

The Student Study Tracker project is a simple application written in the Python console.

The application allows students to track their study sessions and calculate the amount of time spent studying.

I have used fundamental concepts of the Python programming language to develop this application.
Features
The features included in the application are:

• add study session

• view study sessions
• delete study session
• view total study time
• view subject wise study time
• save data in json file
• validate user input
• handle exceptions
Technologies
The application has been built using the following technologies:
• Python
• JSON
• VS Code

• Git and GitHub
The Student Study Tracker console application does not require any external libraries or frameworks to run.
Python Concepts
The following concepts of the Python programming language have been used in the application:
• variables
• strings
• integers
• lists
• dictionaries
• if/else
• loops
• functions
• modules
• file handling
• json
• try/except
Files
The application consists of the following folders and files:
Folder/Files Description
main.py It contains the main menu and controls the flow of the application.
study_manager.py It allows the users to add, view and delete study sessions.
storage.py It handles the storage of the application data
validator.py It validates the user input
report.py It displays the study summary
tests.py It contains test cases
study_data.json It stores the study sessions
How to Run

To run the application:
1. Install Python.
2. Open the project folder in the VS Code.
3. Open the terminal.
4. Type the following command:
python main.py
5. Select an option from the menu.
Example
In the main menu, select 1 to add the study session.
Enter the following details:
Subject: Python
Topic: Functions
Time (in minutes): 60
After pressing Enter, you will see the following message:
Study session added successfully.
Testing
The application can be tested:
1. By adding a new study session.
2. By viewing the study session.
3. By entering a negative value.
4. By entering a blank value.
5. By deleting a study session.
6. By viewing the study summary.
GitHub
The application can be uploaded to the GitHub repository using the Git tool.
The following commands can be executed to push the code to the GitHub:

git init

git add .

git commit -m "Student Study Tracker"

git branch -M main

git remote add origin YOUR_GITHUB_URL

git push -u origin main