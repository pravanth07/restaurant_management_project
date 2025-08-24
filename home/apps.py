from django.apps import AppConfig


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
