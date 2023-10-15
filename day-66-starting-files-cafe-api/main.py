from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rand

from models import db, Cafe
from utils import make_dict, validate_fields, validate_new_price

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=["GET"])
def random():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = rand.choice(all_cafes)
    cafe_dict = make_dict(random_cafe)
    return jsonify(cafe_dict), 200

@app.route("/all", methods=["GET"])
def all():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    all_cafes_list = [make_dict(cafe) for cafe in all_cafes]
    return jsonify(all_cafes_list), 200

@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("loc")
    cafe = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars()
    if cafe:
        cafe_list_dict = [make_dict(c) for c in cafe]
        return jsonify(cafe_list_dict), 200
    else:
        return jsonify({"error": "Not Found"}), 400
    
@app.route("/add", methods=["POST"])
def add():
    try:
        fields = validate_fields(request.form)
        cafe = Cafe(**fields)
        db.session.add(cafe)
        db.session.commit()
        return jsonify({"success": "Successfully added the new cafe."}), 200
    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        new_price = request.args.get("new_price")
        validate_new_price(new_price)
        cafe = Cafe.query.get_or_404(cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api_key")
    try:
        if api_key != "TopSecretAPIKey":
            raise Exception("Invalid API Key.")
        cafe = Cafe.query.get_or_404(cafe_id)
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"success": "Successfully deleted the cafe."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)