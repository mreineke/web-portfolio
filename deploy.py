from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")

@app.route("/java")
def java():
    return render_template("java.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/swift")
def swift():
    return render_template("swift.html")

@app.route("/webdev")
def webdev():
    return render_template("webdev.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careerday")
def career_day():
    return render_template("careerday.html")

if __name__ == "__main__":
   app.run(debug=True)
