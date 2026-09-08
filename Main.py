from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def project():
    projects = [
        {"title1": "Project name",
         "description": "Insert project description",
         "repo_url": "Insert Link"},

        {"title2": "Project name",
         "description": "Insert project description",
         "repo_url": "Insert Link"},

        {"title3": "Project name",
         "description": "Insert project description",
         "repo_url": "Insert Link"},
    ]
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

if __name__ == "__main__":
    app.run(debug=True)
