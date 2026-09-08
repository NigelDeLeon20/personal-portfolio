import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    projects = load_projects()
    certificates = load_certificates()
    return render_template("index.html", projects=projects, certificates=certificates)

def load_projects():
    with open("data/projects.json") as f:
        return json.load(f)

def load_certificates():
    with open("data/certificates.json") as f:
        return json.load(f)

if __name__ == "__main__":
    app.run(debug=True)
