from src import app
from flask import render_template
from .entities.books import menu

@app.route("/")
def index():
    return render_template('index.html',
                           title="Главная страница",
                           menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='О сайте')