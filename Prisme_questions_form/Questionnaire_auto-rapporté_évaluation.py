from random import choices
from typing_extensions import Required
from flask import Flask
from flask import redirect
from flask import request

from questions import Form
from questions import FormPage
from questions import TextQuestion
from questions import ExpressionBlock
from questions import BooleanQuestion
from questions import FormPanel
from questions import RadioGroupQuestion
from questions import MatrixQuestion


import webbrowser
from threading import Timer

class PageOne(Form):
    projet = TextQuestion(title="Projet:")
    participant = TextQuestion(title="Numero du participant:",
                               input_type="number",
                               required="False")
    date = TextQuestion(title="Date",
                        input_type="date",
                        required="False")

class PageTwo(Form):
    intro = ExpressionBlock(title="Introduction:",expression= "",
                            description="Bonjour. Ce questionnaire vous demande des questions à propos des difficultés engendrées par votre état de santé. Par condition de santé, cela inclut les maladies, les troubles de santé mentale, les problèmes émotionnels, les blessures, les problèmes reliés à l’alcool et aux drogues et les autres problèmes de santé qui peuvent être de courte ou de longue durée (ex. problèmes chroniques).\n Pensez à la dernière semaine et répondez aux questions selon à quel point cela était difficile pour vous de faire les activités suivantes. Pour chaque question, encerclez une seule réponse.")
    
    D1 = MatrixQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de…",
                                    columns=[
                {
                    "value": 1,
                    "text": "Aucunement difficile"
                }, {
                    "value": 2,
                    "text": "Légèrement difficile"
                }, {
                    "value": 3,
                    "text": "Modérément difficile "
                }, {
                    "value": 4,
                    "text": "Sévèrement difficile"
                }, {
                    "value": 5,
                    "text": "Extrêmement difficile ou je ne pouvais pas le faire"
                }
            ],
                                    rows=[
                {
                    "value": "D1_1 ",
                    "text": "Vous concentrer à faire quelque chose pour 10 minutes ?"
                }, {
                    "value": "D1_2",
                    "text": "Vous souvenir de faire des choses importantes ?"
                }, {
                    "value": "D1_3",
                    "text": "Analyser et trouver des solutions aux problèmes de la vie de tous les jours ?"
                }, {
                    "value": "D1_4",
                    "text": "Apprendre une nouvelle tâche, par exemple apprendre à se rendre à un nouvel endroit ?"
                }, {
                    "value": "D1_5",
                    "text": "Généralement, comprendre ce que les gens disent ?"
                }, {
                    "value": "D1_6",
                    "text": " Débuter et maintenir une conversation ?"
                }
            ],
                                    all_rows_required = False)
    

class PageThree(Form):
    D2 = MatrixQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de…",
                                    columns=[
                {
                    "value": 1,
                    "text": "Aucunement difficile"
                }, {
                    "value": 2,
                    "text": "Légèrement difficile"
                }, {
                    "value": 3,
                    "text": "Modérément difficile "
                }, {
                    "value": 4,
                    "text": "Sévèrement difficile"
                }, {
                    "value": 5,
                    "text": "Extrêmement difficile ou je ne pouvais pas le faire"
                }
            ],
                                    rows=[
                {
                    "value": "D2_1 ",
                    "text": " Rester debout pendant une période aussi longue que 30 minutes ?"
                }, {
                    "value": "D2_2",
                    "text": " Vous levez lorsque vous étiez assis ?"
                }, {
                    "value": "D2_3",
                    "text": " Se déplacer à l’intérieur de votre maison ?"
                }, {
                    "value": "D2_4",
                    "text": " Sortir de la maison ?"
                }, {
                    "value": "D2_5",
                    "text": " Marcher une longue distance (ex. un kilomètre ou l’équivalent)"
                }
            ],
                                    all_rows_required = False)

class PageFour(Form):
    D3 = MatrixQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de…",
                                    columns=[
                {
                    "value": 1,
                    "text": "Aucunement difficile"
                }, {
                    "value": 2,
                    "text": "Légèrement difficile"
                }, {
                    "value": 3,
                    "text": "Modérément difficile "
                }, {
                    "value": 4,
                    "text": "Sévèrement difficile"
                }, {
                    "value": 5,
                    "text": "Extrêmement difficile ou je ne pouvais pas le faire"
                }
            ],
                                    rows=[
                {
                    "value": "D3_1 ",
                    "text": " Laver votre corps au complet ?"
                }, {
                    "value": "D3_2",
                    "text": " S'habiller ?"
                }, {
                    "value": "D3_3",
                    "text": " Manger ?"
                }, {
                    "value": "D3_4",
                    "text": "Rester seul pendant quelques jours ?"
                }
            ],
                                    all_rows_required = False)


class PageFive(Form):
    D4 = MatrixQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de…",
                                    columns=[
                {
                    "value": 1,
                    "text": "Aucunement difficile"
                }, {
                    "value": 2,
                    "text": "Légèrement difficile"
                }, {
                    "value": 3,
                    "text": "Modérément difficile "
                }, {
                    "value": 4,
                    "text": "Sévèrement difficile"
                }, {
                    "value": 5,
                    "text": "Extrêmement difficile ou je ne pouvais pas le faire"
                }
            ],
                                    rows=[
                {
                    "value": "D4_1 ",
                    "text": " Être dans une situation avec des gens que vous ne connaissez pas ?"
                }, {
                    "value": "D4_2",
                    "text": "Maintenir une amitié ?"
                }, {
                    "value": "D4_3",
                    "text": " S'entendre avec les gens qui sont proches de vous ?"
                }, {
                    "value": "D4_4",
                    "text": " Se faire des nouveaux ami ?"
                }, {
                    "value": "D4_5",
                    "text": " À quel point avez-vous eu des difficultés dans vos activités sexuelles ?"
                }
            ],
                                    all_rows_required = False)

class PageSix(Form):
        D5_1 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de vos responsabilités ménagères (tâches ménagères, familles)",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_2 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches ménagères les plus importantes ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_3 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire toutes les activités ménagères que vous aviez besoin de faire ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_4 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire vos activités ménagères aussi rapidement que nécessaire ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_01 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_2} = 'Légèrement difficile' or {D5_2} = 'Modérément difficile' or {D5_2} = 'Sévèrement difficile' or {D5_2} = 'Extrêmement difficile ou je ne pouvais pas le faire' or {D5_3} = 'Légèrement difficile' or {D5_3} = 'Modérément difficile' or {D5_3} = 'Sévèrement difficile' or {D5_3} = 'Extrêmement difficile ou je ne pouvais pas le faire' or {D5_4} = 'Légèrement difficile' or {D5_4} = 'Modérément difficile' or {D5_4} = 'Sévèrement difficile' or {D5_4} = 'Extrêmement difficile ou je ne pouvais pas le faire'")
        
class PageSeven(Form):
        D5_5 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de faire votre journée de travail/d’école",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_6 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches ménagères les plus importantes ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_7 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire toutes les activités ménagères que vous aviez besoin de faire ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_8 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire vos activités ménagères aussi rapidement que nécessaire ?",
                                  choices=["Aucunement difficile", "Légèrement difficile","Modérément difficile","Sévèrement difficile","Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)   


        D5_9 = BooleanQuestion(title="Avez-vous besoin de travailler à un niveau moins élevé à d'un problème de santé ?",
                               required = False)
        
        D5_10 = BooleanQuestion(title="Gagnez-vous moins d'un problème de santé ?",
                               required = False)
        D5_02 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_5} = 'Légèrement difficile' or {D5_5} = 'Modérément difficile' or {D5_5} = 'Sévèrement difficile' or {D5_5} = 'Extrêmement difficile ou je ne pouvais pas le faire' or {D5_3} = 'Légèrement difficile' or {D5_3} = 'Modérément difficile' or {D5_3} = 'Sévèrement difficile' or {D5_3} = 'Extrêmement difficile ou je ne pouvais pas le faire' or {D5_4} = 'Légèrement difficile' or {D5_4} = 'Modérément difficile' or {D5_4} = 'Sévèrement difficile' or {D5_4} = 'Extrêmement difficile ou je ne pouvais pas le faire'")
        


class Profile(Form):
    page_one = FormPage(PageOne, title="Indentification Participant")
    page_two = FormPage(PageTwo, title="Questionnaire auto-rapporté")
    page_three = FormPage(PageThree, title="Échelle d'Hamilton")
    page_four = FormPage(PageFour, title="Échelle d'Hamilton")
    page_five = FormPage(PageFive, title="Échelle d'Hamilton")
    page_six = FormPage(PageSix, title="Échelle d'Hamilton")
    page_seven = FormPage(PageSeven, title="Échelle d'Hamilton")


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
      app.debug = True
      #Timer(2, open_browser).start();
      app.run(port=5000)