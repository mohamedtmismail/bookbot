# bookbot
BookBot is a small command line utility that generates simple statistics about a text file. 
It was built as a learning exercise as a part of [Boot.dev](https://www.boot.dev)

## Features

* Counts the total number of words in a given text file
* Counts how often each character appears (case-insensitive)
* Outputs a neatly formatted report to the console

## Usage

1. Ensure you have Python 3 installed.
2. Run the program and pass the path to a text file:

```bash
python3 main.py path/to/book.txt
```

The script will read the file, analyze it and print a report showing the word count and each character frequency.

## Project Structure

```
main.py   - entry point that handles user input and printing the final report
stats.py  - helper functions for counting words and characters
```

Feel free to explore the code and modify it to your liking. It's a great project to start learning about Python functions, loops and basic text processing.
