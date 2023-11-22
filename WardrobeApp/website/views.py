from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func, select, desc
from website import date_time
from .models import Pants, Shirt, Shoes, User, Todays_Outfit, Random_Clothes, User_Feedback
from . import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/today', methods = ('GET', 'POST'))
@login_required
def today():
    
    pants_list = Pants.query.filter_by(user_id=current_user.id)
    shoes_list = Shoes.query.filter_by(user_id=current_user.id)
    shirts_list = Shirt.query.filter_by(user_id=current_user.id)

    if request.method == 'POST':
        shirt_today = request.form.get('shirt_today')
        pants_today = request.form.get('pants_today')
        shoes_today = request.form.get('shoes_today')
        where_to = request.form.get('where_to')
        user_id = current_user.id
        date = date_time
        todays_outfit = Todays_Outfit(shirt_id=shirt_today, pants_id=pants_today, shoes_id=shoes_today, where_to=where_to, date=date, user_id=user_id)
        all_outfits = Todays_Outfit.query.filter_by(shirt_id=shirt_today, pants_id=pants_today, shoes_id=shoes_today, where_to=where_to).all()
        
        if not all_outfits:
            db.session.add(todays_outfit)
            db.session.commit()
            # Updating the databse to add the date of the day the clothes are being worn (on the today)
            find_shirt = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
            for shirt_x in find_shirt:
                update_shirt = shirt_x.shirt_id
                shirt_in_database = Shirt.query.filter_by(shirt_id=update_shirt)
                for shirt_y in shirt_in_database:
                    shirt_y.last_time_worn = date
                    shirt_y.times_worn += 1
                    db.session.add(shirt_y)
                    db.session.commit()

            find_pants = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
            for pants_x in find_pants:
                update_pants = pants_x.pants_id
                pants_in_database = Pants.query.filter_by(pants_id=update_pants)
                for pants_y in pants_in_database:
                    pants_y.last_time_worn = date
                    pants_y.times_worn += 1
                    db.session.add(pants_y)
                    db.session.commit()

            find_shoes = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
            for shoe_x in find_shoes:
                update_shoes = shoe_x.shoes_id
                shoes_in_database = Shoes.query.filter_by(shoes_id=update_shoes)
                for shoe_y in shoes_in_database:
                    shoe_y.last_time_worn = date
                    shoe_y.times_worn += 1
                    db.session.add(shoe_y)
                    db.session.commit()

            flash('Success!', category='successs')
            return redirect(url_for('views.calendar'))
        else:
            shirt_today = request.form.get('shirt_today')
            pants_today = request.form.get('pants_today')
            shoes_today = request.form.get('shoes_today')
            where_to = request.form.get('where_to')
            user_id = current_user.id
            date = date_time
            random_clothes = Random_Clothes(shirt_id=shirt_today, pants_id=pants_today, shoes_id=shoes_today, where_to=where_to, user_id=user_id, date=date)
            db.session.add(random_clothes)
            db.session.commit() 
            return redirect(url_for('views.wornbefore'))              
    return render_template("today.html", user=current_user, date_time=date_time, pants_list=pants_list, shoes_list=shoes_list, shirts_list=shirts_list)


@views.route('/today/wornbefore', methods = ('GET', 'POST'))
@login_required
def wornbefore():
    worn_this_outfit_before = Random_Clothes.query.filter_by(user_id=current_user.id).order_by(desc(Random_Clothes.temp_random_id)).limit(1)
    for x in worn_this_outfit_before:
        shirt_id = x.shirt_id
        pants_id = x.pants_id
        shoes_id = x.shoes_id
        where_to = x.where_to

    last_shirt_from_database = Shirt.query.filter_by(user_id=current_user.id, shirt_id=shirt_id)
    last_pants_from_database = Pants.query.filter_by(user_id=current_user.id, pants_id=pants_id)
    last_shoes_from_database = Shoes.query.filter_by(user_id=current_user.id, shoes_id=shoes_id)

    if request.method == 'POST':
        shirt_today = request.form.get('shirt_today')
        pants_today = request.form.get('pants_today')
        shoes_today = request.form.get('shoes_today')
        where_to = request.form.get('where_to')
        user_id = current_user.id
        date = date_time
        todays_outfit = Todays_Outfit(shirt_id=shirt_today, pants_id=pants_today, shoes_id=shoes_today, where_to=where_to, date=date, user_id=user_id)
        db.session.add(todays_outfit)
        db.session.commit()
    
        # Updating the databse to add the date of the day the clothes are being worn (on the today)
        find_shirt = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for shirt_x in find_shirt:
            update_shirt = shirt_x.shirt_id
            shirt_in_database = Shirt.query.filter_by(shirt_id=update_shirt)
            for shirt_y in shirt_in_database:
                shirt_y.last_time_worn = date_time
                shirt_y.times_worn += 1
                db.session.add(shirt_y)
                db.session.commit()

        find_pants = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for pants_x in find_pants:
            update_pants = pants_x.pants_id
            pants_in_database = Pants.query.filter_by(pants_id=update_pants)
            for pants_y in pants_in_database:
                pants_y.last_time_worn = date_time
                pants_y.times_worn += 1
                db.session.add(pants_y)
                db.session.commit()

        find_shoes = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for shoe_x in find_shoes:
            update_shoes = shoe_x.shoes_id
            shoes_in_database = Shoes.query.filter_by(shoes_id=update_shoes)
            for shoe_y in shoes_in_database:
                shoe_y.last_time_worn = date_time
                shoe_y.times_worn += 1
                db.session.add(shoe_y)
                db.session.commit()
        flash('Success!', category='successs')
        return redirect(url_for('views.calendar'))
    
    return render_template("wornBefore.html", user=current_user, worn_this_outfit_before=worn_this_outfit_before, last_shirt_from_database=last_shirt_from_database, last_pants_from_database=last_pants_from_database, last_shoes_from_database=last_shoes_from_database, where_to=where_to, date=date_time)

@views.route('/random', methods = ('GET', 'POST'))
@login_required
def random():
    shirts_list = Shirt.query.filter_by(user_id=current_user.id)
    pants_list = Pants.query.filter_by(user_id=current_user.id)
    shoes_list = Shoes.query.filter_by(user_id=current_user.id)
    
    
    # I think we have to put the result into a database table (Table X and then redirect 
    # the user to another page. We can then use a for loop to get the attributes of the 
    # chosen combination. Maybe after it is added to the "Todays Outfit" table (when 
    # you click yes to adding it to the calender), we will delete it from Table X
    

    where_to = request.form.get('where_to')


    counter = 0
    
    while True:
        counter += 1
        shirt_check = "N/A"
        random_shirt = Shirt.query.filter_by(user_id=current_user.id).order_by(func.rand())
        for shirt in random_shirt:
            if where_to == "Work":
                if shirt.wear_to_work == "Yes":
                    shirt_check = "Good"
                    good_shirt_id = shirt.shirt_id
                    break
                else:
                    shirt_check = "Bad"
                    continue
            elif where_to == "School":
                if shirt.wear_to_school == "Yes":
                    shirt_check = "Good"
                    good_shirt_id = shirt.shirt_id
                    break
                else:
                    shirt_check = "Bad"
                    continue
            elif where_to == "Errands":
                if shirt.wear_to_errands == "Yes":
                    shirt_check = "Good"
                    good_shirt_id = shirt.shirt_id
                    break
                else:
                    shirt_check = "Bad"
                    continue
            elif where_to == "Going Out":
                if shirt.wear_to_going_out == "Yes":
                    shirt_check = "Good"
                    good_shirt_id = shirt.shirt_id
                    break
                else:
                    shirt_check = "Bad"
                    continue
            elif where_to == "Exercise":
                if shirt.wear_to_exercise == "Yes":
                    shirt_check = "Good"
                    good_shirt_id = shirt.shirt_id
                    break
                else:
                    shirt_check = "Bad"
                    continue
        
        pants_check = "N/A"
        random_pants = Pants.query.filter_by(user_id=current_user.id).order_by(func.rand())
        for pants in random_pants:
            if where_to == "Work":
                if pants.wear_to_work == "Yes":
                    pants_check = "Good"
                    good_pants_id = pants.pants_id
                    break
                else:
                    pants_check = "Bad"
                    continue
            elif where_to == "School":
                if pants.wear_to_school == "Yes":
                    pants_check = "Good"
                    good_pants_id = pants.pants_id
                    break
                else:
                    pants_check = "Bad"
                    continue
            elif where_to == "Errands":
                if pants.wear_to_errands == "Yes":
                    pants_check = "Good"
                    good_pants_id = pants.pants_id
                    break
                else:
                    pants_check = "Bad"
                    continue
            elif where_to == "Going Out":
                if pants.wear_to_going_out == "Yes":
                    pants_check = "Good"
                    good_pants_id = pants.pants_id
                    break
                else:
                    pants_check = "Bad"
                    continue
            elif where_to == "Exercise":
                if pants.wear_to_exercise == "Yes":
                    pants_check = "Good"
                    good_pants_id = pants.pants_id
                    break
                else:
                    pants_check = "Bad"
                    continue

        
        shoes_check = "N/A"
        random_shoes = Shoes.query.filter_by(user_id=current_user.id).order_by(func.rand())
        for shoes in random_shoes:
            if where_to == "Work":
                if shoes.wear_to_work == "Yes":
                    shoes_check = "Good"
                    good_shoes_id = shoes.shoes_id
                    break
                else:
                    shoes_check = "Bad"
                    continue
            elif where_to == "School":
                if shoes.wear_to_school == "Yes":
                    shoes_check = "Good"
                    good_shoes_id = shoes.shoes_id
                    break
                else:
                    shoes_check = "Bad"
                    continue
            elif where_to == "Errands":
                if shoes.wear_to_errands == "Yes":
                    shoes_check = "Good"
                    good_shoes_id = shoes.shoes_id
                    break
                else:
                    shoes_check = "Bad"
                    continue
            elif where_to == "Going Out":
                if shoes.wear_to_going_out == "Yes":
                    shoes_check = "Good"
                    good_shoes_id = shoes.shoes_id
                    break
                else:
                    shoes_check = "Bad"
                    continue
            elif where_to == "Exercise":
                if shoes.wear_to_exercise == "Yes":
                    shoes_check = "Good"
                    good_shoes_id = shoes.shoes_id
                    break
                else:
                    shoes_check = "Bad"
                    continue



        if shirt_check == "Good" and pants_check == "Good" and shoes_check == "Good":
            if request.method == 'POST':
                
                all_existing_combinations = Todays_Outfit.query.filter_by(shirt_id=good_shirt_id,pants_id=good_pants_id,shoes_id=good_shoes_id, where_to=where_to).all()

                if not all_existing_combinations:
                    shirt_id = good_shirt_id
                    pants_id = good_pants_id
                    shoes_id = good_shoes_id
                    user_id = current_user.id
                    where_to_in_database = where_to
                    date = date_time
                    random_clothes = Random_Clothes(shirt_id=shirt_id, pants_id=pants_id, shoes_id=shoes_id, user_id=user_id, where_to=where_to_in_database, date=date)
                    db.session.add(random_clothes)
                    db.session.commit()
                    return redirect(url_for('views.randomconfirm'))
                elif counter == 100:
                    flash("It looks like you might have worn every combination you possibly can to this destination!", category='error')
                else:
                    continue
        
        elif shirt_check == "Bad" or pants_check == "Bad" or shoes_check == "Bad":
            flash('It looks like you you do not have full combination of clothes set to go to this destination. Add clothes now!', category='error')
        
        return render_template("random.html", user=current_user, date_time=date_time, pants_list=pants_list, shoes_list=shoes_list, shirts_list=shirts_list, random_shirt=random_shirt, random_pants=random_pants, random_shoes=random_shoes)

@views.route('/random/confirm', methods = ('GET', 'POST'))
@login_required
def randomconfirm():
    random_outfit = Random_Clothes.query.filter_by(user_id=current_user.id).order_by(desc(Random_Clothes.temp_random_id)).limit(1)
    for x in random_outfit:
        shirt_id = x.shirt_id
        pants_id = x.pants_id
        shoes_id = x.shoes_id
        where_to = x.where_to

    random_shirt_from_database = Shirt.query.filter_by(user_id=current_user.id, shirt_id=shirt_id)
    random_pants_from_database = Pants.query.filter_by(user_id=current_user.id, pants_id=pants_id)
    random_shoes_from_database = Shoes.query.filter_by(user_id=current_user.id, shoes_id=shoes_id)
    
    if request.method == 'POST':
        shirt_today = request.form.get('shirt_today')
        pants_today = request.form.get('pants_today')
        shoes_today = request.form.get('shoes_today')
        where_to_in_database = where_to
        user_id = current_user.id
        date = date_time
        todays_outfit = Todays_Outfit(shirt_id=shirt_today, pants_id=pants_today, shoes_id=shoes_today, where_to=where_to_in_database, date=date, user_id=user_id)
        db.session.add(todays_outfit)
        db.session.commit()

        # Updating the databse to add the date of the day the clothes are being worn (on the today)
        find_shirt = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for shirt_x in find_shirt:
            update_shirt = shirt_x.shirt_id
            shirt_in_database = Shirt.query.filter_by(shirt_id=update_shirt)
            for shirt_y in shirt_in_database:
                shirt_y.last_time_worn = date
                shirt_y.times_worn += 1
                db.session.add(shirt_y)
                db.session.commit()

        find_pants = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for pants_x in find_pants:
            update_pants = pants_x.pants_id
            pants_in_database = Pants.query.filter_by(pants_id=update_pants)
            for pants_y in pants_in_database:
                pants_y.last_time_worn = date
                pants_y.times_worn += 1
                db.session.add(pants_y)
                db.session.commit()

        find_shoes = Todays_Outfit.query.filter_by(user_id=current_user.id).order_by(desc(Todays_Outfit.outfit_id)).limit(1)
        for shoe_x in find_shoes:
            update_shoes = shoe_x.shoes_id
            shoes_in_database = Shoes.query.filter_by(shoes_id=update_shoes)
            for shoe_y in shoes_in_database:
                shoe_y.last_time_worn = date
                shoe_y.times_worn += 1
                db.session.add(shoe_y)
                db.session.commit()

        flash('Success!', category='successs')
        return redirect(url_for('views.calendar'))
    
    
    return render_template("randomConfirm.html", user=current_user, random_outfit=random_outfit, shirt_id=shirt_id, pants_id=pants_id, shoes_id=shoes_id, random_shirt_from_database=random_shirt_from_database, random_pants_from_database=random_pants_from_database, random_shoes_from_database=random_shoes_from_database)

@views.route('/calendar')
@login_required
def calendar():

    all_outfits = Todays_Outfit.query.filter_by(user_id=current_user.id)
    shirts = Shirt.query.filter_by(user_id=current_user.id)  
    pants = Pants.query.filter_by(user_id=current_user.id)
    shoes = Shoes.query.filter_by(user_id=current_user.id)      

    dates_of_outfits = []
    where_to = []
    shirt_names = []
    pants_names = []
    shoe_names = []

    for x in all_outfits:
        current_date = x.date
        if current_date:
            dates_of_outfits.append(current_date)

        where_to_for_outfit = x.where_to
        if where_to_for_outfit:
            where_to.append(where_to_for_outfit)

        shirt_id = x.shirt_id
        find_shirt = Shirt.query.filter_by(shirt_id=shirt_id)
        for y in find_shirt:
            shirt_name = y.shirt_name
        if find_shirt:
            shirt_names.append(shirt_name)
        
        pants_id = x.pants_id
        find_pants = Pants.query.filter_by(pants_id=pants_id)
        for y in find_pants:
            pants_name = y.pants_name
        if find_pants:
            pants_names.append(pants_name)

        
        shoes_id = x.shoes_id
        find_shoes = Shoes.query.filter_by(shoes_id=shoes_id)
        for y in find_shoes:
            shoe_name = y.shoe_name        
        if find_shoes:
            shoe_names.append(shoe_name)

        


    return render_template("calendar.html", user=current_user, all_outfits=all_outfits, shirts=shirts, pants=pants, shoes=shoes, dates_of_outfits=dates_of_outfits, where_to=where_to, shirt_names=shirt_names, pants_names=pants_names, shoe_names=shoe_names, zip=zip)

@views.route('/addnew')
@login_required
def addnew():
    # Count how many of each in either category
    pants_list = Pants.query.filter_by(user_id=current_user.id)
    amount_of_pants = pants_list.count()

    shirts_list = Shirt.query.filter_by(user_id=current_user.id)
    amount_of_shirts = shirts_list.count()

    shoes_list = Shoes.query.filter_by(user_id=current_user.id)
    amount_of_shoes = shoes_list.count()
    return render_template("addnew.html", user=current_user, amount_of_pants=amount_of_pants, amount_of_shirts=amount_of_shirts, amount_of_shoes=amount_of_shoes)

@views.route('/addnewpants', methods = ('GET', 'POST'))
@login_required
def addnewpants():
    if request.method == 'POST':
        pants_name = request.form['pants_name']
        brand = request.form['brand']
        primary_color = request.form['primary_color']
        type = request.form['type']
        times_worn = 0
        last_time_worn = "N/A"
        worn_to_most = "N/A"
        wear_to_work = request.form.get('wear_to_work')
        wear_to_school = request.form.get('wear_to_school')
        wear_to_errands = request.form.get('wear_to_errands')
        wear_to_going_out = request.form.get('wear_to_going_out')
        wear_to_exercise = request.form.get('wear_to_exercise')
        user_id = current_user.id
        pants = Pants(brand=brand, primary_color=primary_color, type=type, times_worn=times_worn, last_time_worn=last_time_worn, worn_to_most=worn_to_most, user_id=user_id, wear_to_work=wear_to_work, wear_to_school=wear_to_school, wear_to_errands=wear_to_errands, wear_to_going_out=wear_to_going_out, wear_to_exercise=wear_to_exercise, pants_name=pants_name)
        db.session.add(pants)
        db.session.commit()

        flash('Pants added successfully!', category='successs')
        return redirect(url_for('views.pants'))


    return render_template("addNewPants.html", user=current_user)

@views.route('/addnewshirt', methods = ('GET', 'POST'))
@login_required
def addnewshirt():
    if request.method == 'POST':
        shirt_name = request.form['shirt_name']
        brand = request.form['brand']
        primary_color = request.form['primary_color']
        type = request.form['type']
        times_worn = 0
        last_time_worn = "N/A"
        worn_to_most = "N/A"
        wear_to_work = request.form.get('wear_to_work')
        wear_to_school = request.form.get('wear_to_school')
        wear_to_errands = request.form.get('wear_to_errands')
        wear_to_going_out = request.form.get('wear_to_going_out')
        wear_to_exercise = request.form.get('wear_to_exercise')
        user_id = current_user.id
        shirt = Shirt(brand=brand, primary_color=primary_color, type=type, times_worn=times_worn, last_time_worn=last_time_worn, worn_to_most=worn_to_most, user_id=user_id, wear_to_work=wear_to_work, wear_to_school=wear_to_school, wear_to_errands=wear_to_errands, wear_to_going_out=wear_to_going_out, wear_to_exercise=wear_to_exercise, shirt_name=shirt_name)
        db.session.add(shirt)
        db.session.commit()

        flash('Shirt added successfully!', category='successs')
        return redirect(url_for('views.shirts'))
    return render_template("addNewShirt.html", user=current_user)

@views.route('/addnewshoes', methods = ('GET', 'POST'))
@login_required
def addnewshoes():
    if request.method == 'POST':
        shoe_name = request.form['shoe_name']
        brand = request.form['brand']
        primary_color = request.form['primary_color']
        type = request.form['type']
        times_worn = 0
        last_time_worn = "N/A"
        worn_to_most = "N/A"
        wear_to_work = request.form.get('wear_to_work')
        wear_to_school = request.form.get('wear_to_school')
        wear_to_errands = request.form.get('wear_to_errands')
        wear_to_going_out = request.form.get('wear_to_going_out')
        wear_to_exercise = request.form.get('wear_to_exercise')
        user_id = current_user.id
        shoes = Shoes(brand=brand, primary_color=primary_color, type=type, times_worn=times_worn, last_time_worn=last_time_worn, worn_to_most=worn_to_most, user_id=user_id, wear_to_work=wear_to_work, wear_to_school=wear_to_school, wear_to_errands=wear_to_errands, wear_to_going_out=wear_to_going_out, wear_to_exercise=wear_to_exercise, shoe_name=shoe_name)
        db.session.add(shoes)
        db.session.commit()

        flash('Shoes added successfully!', category='successs')
        return redirect(url_for('views.shoes'))
    return render_template("addNewShoes.html", user=current_user)

@views.route('/shirts')
@login_required
def shirts():
    shirts_list = Shirt.query.filter_by(user_id=current_user.id)
    return render_template("shirts.html", user=current_user, shirts_list=shirts_list)

@views.route('/pants')
@login_required
def pants():
    pants_list = Pants.query.filter_by(user_id=current_user.id)
    return render_template("pants.html", user=current_user, pants_list=pants_list)

@views.route('/shoes')
@login_required
def shoes():
    shoes_list = Shoes.query.filter_by(user_id=current_user.id)
    return render_template("shoes.html", user=current_user, shoes_list=shoes_list)

@views.route('/feedback', methods = ('GET', 'POST'))
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        feedback = request.form['feedback']
        get_feedback = User_Feedback(email=email, feedback=feedback)
        db.session.add(get_feedback)
        db.session.commit()
        flash('Thank you! We will take a look at your feedback as soon as possible.', category='success')
        return redirect(url_for('views.today'))
    
    return render_template("feedback.html", user=current_user)
