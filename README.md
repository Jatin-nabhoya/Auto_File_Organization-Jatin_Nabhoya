# File Organizer Project
Overview
This project is a file organization tool that allows users to sort files based on their extensions and their creation dates (year, month, and day). When the main script is run, a GUI pops up, prompting the user to specify the source and destination paths. Upon pressing the submit button, the files in the source folder are organized and moved to the destination folder in a structured manner.

# Features
Sort by Extension: Organizes files into folders based on their file extensions.
Sort by Date: Organizes files into folders based on their creation date (year, month, day).
GUI Interface: User-friendly interface for specifying source and destination paths.

# Requirements
Python 3.x
tkinter for the GUI
os and shutil modules for file operations

# How It Works
Sorting by Extension
The script reads all files in the source directory.
For each file, it determines the file extension.
A new folder is created in the destination directory for each file extension (if it doesn't already exist).
Files are moved to their respective extension folders.

# Sorting by Date
The script reads all files in the source directory.
For each file, it retrieves the file's creation date.
Folders are created in the destination directory structured by year, month, and day.
Files are moved to their respective date folders.

# Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
