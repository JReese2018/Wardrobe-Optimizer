from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/today')
def today():
    return render_template("today.html")

@views.route('/random')
def random():
    return render_template("random.html")

@views.route('/calendar')
def calendar():
    return render_template("calendar.html")

@views.route('/addnew')
def addnew():
    return render_template("addnew.html")

@views.route('/shirts')
def shirts():
    return render_template("shirts.html")

@views.route('/pants')
def pants():
    return render_template("pants.html")

@views.route('/shoes')
def shoes():
    return render_template("shoes.html")

@views.route('/feedback')
def feedback():
    return render_template("feedback.html")