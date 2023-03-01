from src import app
from flask import render_template, request, session, redirect, url_for
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

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html',
                           title="Страница не найдена",
                           menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f"Профиль пользователя: {username}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for('profile',
                                username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "me" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html',
                           title="Авторизация",
                           menu=menu)


