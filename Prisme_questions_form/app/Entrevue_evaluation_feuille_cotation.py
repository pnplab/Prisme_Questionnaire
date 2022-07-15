from flask import Flask
from flask import redirect
from flask import request

from questions import Form
from questions import FormPage
from questions import TextQuestion
from questions import DropdownQuestion
from questions import RadioGroupQuestion


import webbrowser
from threading import Timer

class PageOne(Form):
    projet = TextQuestion(title="Projet:")
    participant = TextQuestion(title="Numero Participant",
                               input_type="number",
                               required="True")
    date = TextQuestion(title="Date",
                        input_type="date",
                        required="True")


class PageTwo(Form):
    role = TextQuestion(title="Cote finale du fonctionnement global - Rôle:",
                        input_type="number",
                        required="True")
    social = TextQuestion(title="Cote finale du fonctionnement global - social:",
                        input_type="number",
                        required="True")

class PageThree(Form):
    hdrs = TextQuestion(title="Depression (HDRS) Total des 17 premiers items:",
                        input_type="number",
                        required="True")
    anxiete = TextQuestion(title="Évaluation de l'anxiété, total des 14 items:",
                        input_type="number",
                        required="True")


class Profile(Form):
    page_one = FormPage(PageOne, title="Indentification Participant")
    page_two = FormPage(PageTwo, title="Fonctionnement Global")
    page_three = FormPage(PageThree, title="Échelle d'Hamilton")


def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')


app = Flask(__name__)
Form.set_resource_url("/static")

@app.route("/", methods=("GET",))
def form():
    form = Profile(title="Prisme", theme="modern",
                   platform="jquery", navigate_to_url="/thanks"
                   )
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
      app.debug = False
      Timer(2, open_browser).start();
      app.run(port=5000)