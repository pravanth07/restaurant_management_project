from django.apps import AppConfig
from flask import Flask, jsonify
from models import MenuItem


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

app = flask(___name__)

@app.context_processor
def inject_current_year():
    return {"current_year": datetime.now().year}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/reservations")
def reservations():
    return render_template("reservations.html")
def menu_item_detail(item_id):
    try:
        item = MenuItem.query.get(item_id)
        if not item:
            return jsonify({"error": "Menu item not found"}), 404
        return jsonify({
            "id": item.id,
            "name": item.name,
            "price": item.price
        })
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
        