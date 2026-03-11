from flask import Flask, render_template, request
import os
import spacy
import PyPDF2

app = Flask(__name__)

# load spacy
nlp = spacy.load("en_core_web_sm")

recipes = {}
folder = "static/recipes"

# read all pdf files
for file in os.listdir(folder):

    if file.endswith(".pdf"):

        path = os.path.join(folder, file)

        pdf = open(path, "rb")
        reader = PyPDF2.PdfReader(pdf)

        text = ""

        for page in reader.pages:
            text += page.extract_text()

        recipes[file] = text.lower()


@app.route("/", methods=["GET", "POST"])
def home():

    # show all recipes by default
    results = list(recipes.keys())

    if request.method == "POST":

        query = request.form["search"].lower()
        results = []

        for recipe, text in recipes.items():
            if query in text:
                results.append(recipe)

    return render_template("index.html", results=results)



if __name__ == "__main__":
    app.run(debug=True)