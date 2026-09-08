import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def project():
    projects = load_projects()
    return render_template("projects.html", projects=projects)

@app.route("/certificates")
def certificates():
    certificates = [
            {"title": "Certificate name", "description": "Insert certificate description"},
            {"title": "Certificate name", "description": "Insert certificate description"},
            {"title": "Certificate name", "description": "Insert certificate description"},
        ]
    return render_template("certificates.html", certificates=certificates)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

def load_projects():
    with open("data/projects.json") as f:
        return json.load(f)

if __name__ == "__main__":
    app.run(debug=True)
