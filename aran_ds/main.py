from flask import Flask,render_template,request

app = Flask(__name__)


# Home(Aran DS)
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/index", methods=["post"])
def index_post():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)