# Anime Recommendation Script

This Python script recommends an anime based on user input such as genre, minimum score, and starting date. It utilizes the [Jikan API](https://jikan.docs.apiary.io/) to fetch anime data.

## Features

- **User Input**: Users can input their preferred genre, minimum score, and starting date for anime selection.
- **API Integration**: Utilizes the Jikan API to fetch anime data based on user preferences.
- **Random Selection**: Randomly selects an anime from the fetched data to recommend to the user.

## How to Use

1. **Clone the Repository**: Clone or download this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed on your machine. You'll also need to install the `requests` module, which can be installed via pip: pip install requests
3. **Run the Script**: Execute the `main.py` script using Python: python main.py
4. **Input**: Follow the prompts to input the desired genre, minimum score, and starting date.
5. **Recommendation**: The script will recommend an anime based on your input.

## Example
Please provide a valid genre: Action
Please provide a minimum score: 7
Please provide a starting date (YYYY-MM-DD): 2022-01-01
You should watch One Piece!

## Dependencies

- Python 3.x
- requests module
