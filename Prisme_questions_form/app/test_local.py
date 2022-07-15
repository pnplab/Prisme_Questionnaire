from flask import Flask
from flask import redirect
from flask import request

from questions import Form
from questions import FormPanel
from questions import BooleanQuestion
from questions import DropdownQuestion
from questions import TextQuestion


class PreferencesForm(Form):
    email = TextQuestion(input_type="email")
    email_format = DropdownQuestion(choices=["PDF", "HTML", "Plain Text"])

class ProfileForm(Form):
    receive_newsletter = BooleanQuestion(
        title="Do you wish to receive our newsletter?",
        required=True,
    )
    newsletter_panel = FormPanel(
        PreferencesForm,
        title="Newsletter Preferences",
        visible_if="{receive_newsletter} == True",
    )



app = Flask(__name__)

@app.route("/", methods=("GET",))
def form():
    form = PreferencesForm()
    return form.render_html()

@app.route("/", methods=("POST",))
def post():
    form_data = request.get_json()
    # Here, we would save to a database or something
    print(form_data)
    return redirect("/thanks")

@app.route("/thanks")
def thanks():
    return "Thanks for your information"

if __name__ == "__main__":
    app.run()