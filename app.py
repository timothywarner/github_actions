from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        # Additional logic can be added here
        return render_template("index.html", result="Received")
    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)
