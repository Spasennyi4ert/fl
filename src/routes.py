from src import app
from flask import render_template, request
from .entities.books import menu

@app.route("/")
def index():
    return render_template('index.html', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', menu=menu)

@app.route("/feedback", methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        print(request.form)

    return render_template('feedback.html',
                           title='Отзывы',
                           menu=menu)