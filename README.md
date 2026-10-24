News Aggregator & Topic Tracker

A Python project that retrieves news articles through a REST API and allows users to search, filter, save, and manage their favorite articles using JSON file storage.

Features

- Fetch news articles from an API
- Search news by topic
- Filter articles by website or source
- View article information
- Save favorite articles to a JSON file
- Prevent duplicate favorites
- Display saved favorites
- Remove favorites from saved data
- Handle missing data and common errors

Technologies Used

- Python
- Requests
- REST API
- JSON
- File handling
- Lists and dictionaries
- Loops, functions, and conditional statements
- Exception handling

Requirements

- Python 3
- Internet connection
- The "requests" library

Installation

Install the required library:

pip install requests

How to Run

Run the Python file:

python news_data.py

Follow the menu instructions to fetch news, search for topics, filter articles, and manage your favorites.

Data Storage

Favorite articles are stored locally in "favourites.json".

The program can create this file automatically when favorites are saved. You do not need to create it manually.

Learning Objectives

This project demonstrates how to work with REST APIs, process JSON responses, filter data, prevent duplicate records, and update JSON files.

Future Improvements

- Add date-based filtering
- Add pagination for news results
- Improve error handling
- Add more search and sorting options

Author

Kavikshay

License

This project is available under the MIT License. See the "LICENSE" file for details.
