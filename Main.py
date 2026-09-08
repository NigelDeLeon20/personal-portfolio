from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def project():
    return render_template("projects.html")

@app.route("/certificates")
def certificates():
    return render_template("certificates.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)
