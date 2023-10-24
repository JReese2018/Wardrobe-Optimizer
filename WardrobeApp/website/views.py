from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/today')
@login_required
def today():
    return render_template("today.html", user=current_user)

@views.route('/random')
@login_required
def random():
    return render_template("random.html", user=current_user)

@views.route('/calendar')
@login_required
def calendar():
    return render_template("calendar.html", user=current_user)

@views.route('/addnew')
@login_required
def addnew():
    return render_template("addnew.html", user=current_user)

@views.route('/addnewpants')
@login_required
def addnewpants():
    return render_template("addNewPants.html", user=current_user)

@views.route('/addnewshirt')
@login_required
def addnewshirt():
    return render_template("addNewShirt.html", user=current_user)

@views.route('/addnewshoes')
@login_required
def addnewshoes():
    return render_template("addNewShoes.html", user=current_user)

@views.route('/shirts')
@login_required
def shirts():
    return render_template("shirts.html", user=current_user)

@views.route('/pants')
@login_required
def pants():
    return render_template("pants.html", user=current_user)

@views.route('/shoes')
@login_required
def shoes():
    return render_template("shoes.html", user=current_user)

@views.route('/feedback')
def feedback():
    return render_template("feedback.html", user=current_user)
