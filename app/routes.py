import flask
from app import app,db
from flask import json, render_template, request, Response, flash, redirect
from app.models import User, Course, Enrollment
from app.forms import LoginForm, RegisterForm

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("You are logged in!","success")
        return redirect('/index')

    return render_template("login.html", title="Login", form=form , login=True)

@app.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash("Registration succesful!","success")
        return redirect('/login')
    return render_template("register.html",title="Register", form=form ,register=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)

@app.route("/enrollment",methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')

    data = {
        "id": id,
        "title": title,
        "term": term,
    }

    return render_template("enrollment.html", enrollment=True, data=data)

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response(json.dumps(jdata),mimetype="application/json")

@app.route('/user')
def user():
    # User(user_id=1, first_name="Issac", last_name="Newton", email="newton@uta.com", password="1234").save()
    # User(user_id=2, first_name="Nikola", last_name="Tesla", email="tesla@uta.com", password="1234").save()

    users = User.objects.all()
    return render_template("user.html",users=users)
