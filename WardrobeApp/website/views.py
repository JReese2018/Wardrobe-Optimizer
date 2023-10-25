from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from website import date_time
from .models import Pants, User
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/today')
@login_required
def today():
    return render_template("today.html", user=current_user, date_time=date_time)

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

@views.route('/addnewpants', methods = ('GET', 'POST'))
@login_required
def addnewpants():
    user = User.query.filter_by(id=current_user.id).first()
    if request.method == 'POST':
        brand = request.form['brand']
        primary_color = request.form['primary_color']
        secondary_color = request.form['secondary_color']
        type = request.form['type']
        times_worn = 0
        last_time_worn = "N/A"
        worn_to_most = "N/A"
        user_id = user # Find out how to put current user id here
        pants = Pants(brand=brand, primary_color=primary_color, secondary_color=secondary_color, type=type, times_worn=times_worn, last_time_worn=last_time_worn, worn_to_most=worn_to_most, user_id=user_id)
        db.session.add(pants)
        db.session.commit()

        return redirect(url_for('views.pants'))


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
