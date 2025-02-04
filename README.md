# Quiz App

A simple Python-based quiz application that utilizes the OpenTrivia Database (OpenTDB) API 
to fetch 10 random trivia questions and presents them using a Tkinter GUI. It tracks the score and displays a 
green light for correct answers and a red light for incorrect ones.

## Features
- Loads 10 random questions from OpenTrivia Database (OpenTDB) AP
- Handles user interactions through a tkinter GUI
- Tracks scores and provides feedback
- Implements an interactive quiz logic

## Project Structure

```
├── data.py             # Manages quiz data and question sets
├── main.py             # Entry point for the application
├── question_model.py   # Defines the Question class
├── quiz_brain.py       # Handles quiz logic and score tracking
├── ui.py               # User interface implementation
```

## Requirements
- Python 3.x
- Tkinter (for GUI functionality)

## Usage
```sh
python main.py
```


