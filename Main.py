import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = load_projects()
    certificates = load_certificates()
    experience = load_experience()
    skills = load_skills()
    return render_template("index.html", projects=projects, certificates=certificates, skills=skills, experience=experience)

def load_projects():
    with open("data/projects.json") as f:
        return json.load(f)

def load_certificates():
    with open("data/certificates.json") as f:
        return json.load(f)

def load_experience():
    with open("data/experience.json") as f:
        return json.load(f)

def load_skills():
    with open("data/skills.json") as f:
        return json.load(f)

if __name__ == "__main__":
    app.run(debug=True)
