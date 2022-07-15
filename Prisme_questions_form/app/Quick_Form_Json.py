from flask import Flask
from flask import redirect
from flask import request

from questions import Form
import webbrowser
from threading import Timer

# Load json file
js = open("/home/yassine/git/Prisme_questions_form/Demo_Json_form.json").read()
Demo = Form.from_json(js,"Demo")

# create a flask app
app = Flask(__name__)
Form.set_resource_url("/static")

@app.route("/", methods=("GET",))
def form():
    form = Demo(title="Demo_Json_form", theme="modern",
                platform="jquery", navigate_to_url="/thanks") #,

    return form.render_html()

@app.route("/", methods=("POST",))
def post():
    form_data = request.get_json()
    
    form = Demo.from_json(form_data, "Prisme")
    form.render_html()
    
    # Here, we would save to a database or something
    print(form_data)
    return redirect("/thanks")

@app.route("/thanks", methods=("GET",))
def thanks():
    return "Thanks for your information"

def open_browser():
      webbrowser.open_new('http://127.0.0.1:2000/')

if __name__ == "__main__":
      Timer(1, open_browser).start()
      app.run(port=2000)