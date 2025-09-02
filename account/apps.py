from flask import flask, render_template

app = flask(__name__)

@app.route("/reservations")
def reservations():
    return render_template("reservations.html")
def ready(self):
    import yourapp.signals
    