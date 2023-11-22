# This document does nothing for the site. I will be looking at how to structure python code in this doc

# 1. Find out where the User is headed (Work, School, Going Out, etc.)

# 2. Randomize clothes from database
#   -Using the IDs of the clothes from the database, have a randomizer function pick one of the IDs
#   -Continue to pick until it has found a combination that has not been used before

#   -In order to do this properly, we need to access each table and see where they would wear the clothes
#   -This is why we are asking where they are headed.
#   -The code should only randomize clothes that have the "yes" value in the wear_to_blank sections of the clothes

#   - Below is code in simple human terms to figure out to disect above
#   - We will assume that the IDs of the user will already be linked to the lists
def clothes_checker():
    shirt_check = "N/A"
    random_shirt = Shirt.query.filter_by(user_id=current_user.id).order_by(func.rand())
    for shirt in random_shirt:
        if where_to == "Work":
            if shirt.wear_to_work == "Yes":
                shirt_check = "Good"
                good_shirt_id = shirt.shirt_id
                break
            else:
                continue
        elif where_to == "School":
            if shirt.wear_to_school == "Yes":
                shirt_check = "Good"
                good_shirt_id = shirt.shirt_id
                break
            else:
                continue
        elif where_to == "Errands":
            if shirt.wear_to_errands == "Yes":
                shirt_check = "Good"
                good_shirt_id = shirt.shirt_id
                break
            else:
                continue
        elif where_to == "Going Out":
            if shirt.wear_to_going_out == "Yes":
                shirt_check = "Good"
                good_shirt_id = shirt.shirt_id
                break
            else:
                continue
        elif where_to == "Exercise":
            if shirt.wear_to_exercise == "Yes":
                shirt_check = "Good"
                good_shirt_id = shirt.shirt_id
                break
            else:
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
                continue
        elif where_to == "School":
            if pants.wear_to_school == "Yes":
                pants_check = "Good"
                good_pants_id = pants.pants_id
                break
            else:
                continue
        elif where_to == "Errands":
            if pants.wear_to_errands == "Yes":
                pants_check = "Good"
                good_pants_id = pants.pants_id
                break
            else:
                continue
        elif where_to == "Going Out":
            if pants.wear_to_going_out == "Yes":
                pants_check = "Good"
                good_pants_id = pants.pants_id
                break
            else:
                continue
        elif where_to == "Exercise":
            if pants.wear_to_exercise == "Yes":
                pants_check = "Good"
                good_pants_id = pants.pants_id
                break
            else:
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
                continue
        elif where_to == "School":
            if shoes.wear_to_school == "Yes":
                shoes_check = "Good"
                good_shoes_id = shoes.shoes_id
                break
            else:
                continue
        elif where_to == "Errands":
            if shoes.wear_to_errands == "Yes":
                shoes_check = "Good"
                good_shoes_id = shoes.shoes_id
                break
            else:
                continue
        elif where_to == "Going Out":
            if shoes.wear_to_going_out == "Yes":
                shoes_check = "Good"
                good_shoes_id = shoes.shoes_id
                break
            else:
                continue
        elif where_to == "Exercise":
            if shoes.wear_to_exercise == "Yes":
                shoes_check = "Good"
                good_shoes_id = shoes.shoes_id
                break
            else:
                continue