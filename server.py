from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

#@app.route("/<user>/<int:id_num>")
#def hello_custom(user=None, id_num=None):
#    return render_template("index.html", name=str(user).capitalize(), id_int=id_num)


