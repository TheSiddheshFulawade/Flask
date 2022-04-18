from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route("/") 
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/companies")
def companies():
    return render_template("companies.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about us.html")

@app.route("/resumebuilder")
def resumebuilder():
    return render_template("resumebuilder.html")

@app.route("/sampleresume")
def sampleresume():
    return render_template("sampleresume.html")

@app.route("/sign-in student")
def signinstudent():
    return render_template("signin student.html")

@app.route("/sign-in recruiter")
def signinrecruiter():
    return render_template("signin recruiter.html")

@app.route("/sign-up student")
def signupstudent():
    return render_template("signup student.html")

@app.route("/sign-up recruiter")
def signuprecruiter():
    return render_template("signup recruiter.html")


if __name__ == "__main__":
    app.run(debug=True)
