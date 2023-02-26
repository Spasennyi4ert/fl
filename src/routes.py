from src import app

@app.route("/")
def index():
    return "index"
