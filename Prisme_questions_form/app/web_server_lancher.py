from flask import Flask
from flask import redirect
from flask import request

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=("GET",))
    def form():
        return redirect("/thanks")

    @app.route("/thanks", methods=("GET",))
    def thanks():
        return "Thanks for your information"

    return app
# Create a flask server instance then run it
