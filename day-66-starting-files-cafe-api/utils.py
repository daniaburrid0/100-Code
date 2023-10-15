from models import Cafe

def make_dict(db_obj: Cafe) -> dict:
    cafe_dict = {
        "id": db_obj.id,
        "name": db_obj.name,
        "map_url": db_obj.map_url,
        "img_url": db_obj.img_url,
        "location": db_obj.location,
        "seats": db_obj.seats,
        "has_toilet": db_obj.has_toilet,
        "has_wifi": db_obj.has_wifi,
        "has_sockets": db_obj.has_sockets,
        "can_take_calls": db_obj.can_take_calls,
        "coffee_price": db_obj.coffee_price
    }
    return cafe_dict

def validate_fields(form_data):
    name = form_data.get("name")
    map_url = form_data.get("map_url")
    img_url = form_data.get("img_url")
    location = form_data.get("location")
    seats = form_data.get("seats")
    has_toilet = form_data.get("has_toilet")
    has_wifi = form_data.get("has_wifi")
    has_sockets = form_data.get("has_sockets")
    can_take_calls = form_data.get("can_take_calls")
    coffee_price = form_data.get("coffee_price")

    # Validate required fields
    if not name or not location or not seats or not coffee_price:
        raise ValueError("Missing required fields.")

    # Validate boolean fields
    has_toilet = bool(has_toilet)
    has_wifi = bool(has_wifi)
    has_sockets = bool(has_sockets)
    can_take_calls = bool(can_take_calls)

    # Validate integer fields
    try:
        seats = int(seats)
    except ValueError:
        raise ValueError("Invalid value for seats.")

    # Validate float fields
    try:
        coffee_price = float(coffee_price)
    except ValueError:
        raise ValueError("Invalid value for coffee_price.")

    return {
        "name": name,
        "map_url": map_url,
        "img_url": img_url,
        "location": location,
        "seats": seats,
        "has_toilet": has_toilet,
        "has_wifi": has_wifi,
        "has_sockets": has_sockets,
        "can_take_calls": can_take_calls,
        "coffee_price": coffee_price
    }
    
def validate_new_price(new_price):
    try:
        new_price = float(new_price)
    except ValueError:
        raise ValueError("Invalid value for new_price.")