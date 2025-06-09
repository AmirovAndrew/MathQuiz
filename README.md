# Math Quiz for Kids

A fun and interactive math quiz application designed for children. Built with Python and its standard Tkinter library, this application provides a colorful and engaging way for kids to practice their arithmetic skills.

The quiz features a kid-friendly design with cheerful colors, playful fonts, and instant visual feedback to make learning a positive experience.

*(To add your own screenshot, take a picture of the running application and save it as `screenshot.png` in this folder.)*

## Features

* **Random Math Problems**: Generates an endless stream of questions across four different operations:
    * Addition (two numbers up to 99)
    * Subtraction (with a guaranteed positive result)
    * Multiplication (with a result less than 150)
    * Division (with no remainder)
* **Kid-Friendly Interface**: A bright, colorful design with a large, playful font ("Comic Sans MS") to keep children engaged.
* **Visual Feedback**: Provides instant visual confirmation with custom icons for correct (e.g., a happy star) and incorrect (e.g., a "try again" symbol) answers.
* **High-Stakes Scoring**: The score increases with each correct answer but resets to zero on any incorrect answer, adding a fun challenge.
* **Session Scoreboard**: A "Scoreboard" button opens a pop-up window that tracks the performance for the entire session, showing each question, the user's answer, and the result.
* **No External Dependencies**: Runs using only Python's standard libraries, making setup incredibly simple.


## Requirements

* Python 3.6 or newer (since Tkinter is included by default).
* Two image files for feedback.


## Setup and Installation

Follow these steps to get the application running on your local machine.

1. **Download the Project Files**:
Save the main Python script (e.g., `quiz_app.py`) to a new folder on your computer.
2. **Add Feedback Images**:
Create or download two small images and place them in the **same folder** as the Python script. The application will look for these specific filenames:
    * `correct.png`: A happy star, a green checkmark, or a smiley face. (Recommended size: 50x50 pixels).
    * `incorrect.png`: A red 'X', a sad face, or a "try again" symbol. (Recommended size: 50x50 pixels).
3. **Verify Your File Structure**:
Your project folder should look like this:

```
your-quiz-folder/
├── quiz_app.py         # The main application script
├── correct.png         # Image for correct answers
└── incorrect.png         # Image for incorrect answers
```


## How to Run the Application

1. Open a terminal or command prompt.
2. Navigate to the directory where you saved your project files.

```bash
cd path/to/your-quiz-folder
```

3. Run the script using Python.

```bash
python quiz_app.py
```

The application window should appear, and you can start the quiz!

