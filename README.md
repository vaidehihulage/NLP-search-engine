# NLP-search-engine
Smart Recipe Finder is a simple web-based application that allows users to search for recipes using keywords or ingredients. Built with Python, Flask, and basic NLP techniques, it retrieves matching recipes from stored PDF documents and displays them as clickable results, enabling users to quickly access and view the full recipe.

# Smart Recipe Finder 🍲

Smart Recipe Finder is a simple NLP-based recipe search engine that allows users to search for recipes using keywords or ingredients. The system retrieves recipes from PDF documents and displays matching results to the user.

## Features

- Search recipes using dish names or ingredients
- Retrieves results from stored recipe PDF files
- Clickable search results that open the full recipe
- Simple and user-friendly web interface
- Built using Flask and basic NLP techniques

## Technologies Used

- Python
- Flask
- HTML
- CSS
- spaCy (for NLP processing)
- PyPDF2 (for extracting text from PDFs)

## Installation

1. Clone the repository or download the project folder.

2. Navigate to the project directory.

3. Install the required libraries:
pip install flask spacy PyPDF2

4. Download the spaCy model:
python -m spacy download en_core_web_sm


## Running the Application
Run the following command:
python app.py

The server will start and run at:
http://127.0.0.1:5000
Open this URL in your browser.

## How It Works

1. Recipe PDFs are stored inside the **static/recipes** folder.
2. The application extracts text from the PDFs.
3. When a user enters a search query, the system processes it using NLP.
4. The query is matched with recipe text.
5. Matching recipes are displayed as clickable links.
6. Clicking a result opens the recipe PDF.

## Example Searches

- chicken
- paneer
- chocolate cake
- rice
- pasta

## Future Improvements

- Ingredient-based smart matching
- Recipe ranking using TF-IDF
- Image previews for recipes
- User login and saved recipes

## Author

Developed as an NLP project using Python and Flask.
