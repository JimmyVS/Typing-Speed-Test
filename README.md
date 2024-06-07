# Typing-Speed-Test

## Description:

This Python application is a simple typing speed test game. It displays words from a text file and challenges the user to type them correctly within a 60-second time limit. The user's score is calculated based on the number of characters typed correctly per second (CPS).

## How to Use:
### Prerequisites:

- Make sure you have Python 3 installed on your system. You can check by running python3 --version in your terminal.
- Install the required libraries: tkinter, random, and linecache. You can install them using the command pip install tkinter random linecache.
### Download and Run:

- Clone or download this repository.
- Open a terminal or command prompt and navigate to the downloaded folder.
- Run the application using the command python typing_speed_test.py (replace with the actual file name if different).

## How it Works:

- The application starts with a welcome message and displays the remaining time (60 seconds).
- When you press Enter, the test begins.
- A random word is selected from a text file named "words.txt".
- The word is displayed on the screen.
- You need to type the displayed word correctly within the time limit.
- The application keeps track of your score based on the number of characters typed correctly.
- After 60 seconds, the test ends and your CPS (Characters Per Second) is displayed.

## Customization:

You can modify the "words.txt" file to include your own list of words for the typing test.
Adjust the time limit by changing the initial value of the timeLeft variable in the code.
