import os
import pandas as pd

from flask import Flask
from flask import redirect
from flask import request


from questions import Form
from questions import FormPage
from questions import TextQuestion
from questions import DropdownQuestion
from questions import BooleanQuestion
from questions import HtmlBlock
from questions import RadioGroupQuestion
from questions import MatrixQuestion
from questions import CommentQuestion
from questions import DropdownQuestion
from questions import MatrixDynamicQuestion
from questions import FormPanel


import webbrowser
from threading import Timer


class Page1(Form):
    intro = HtmlBlock (title="test html",
                        html = '''<div><font size="5">
<h4 style="text-align: justify;">Questionnaire auto-rapporté - Évaluation initiale </h4> </font></div> ''')
    projet = TextQuestion(title="Projet:")
    participant = TextQuestion(title="Numero du participant:",
                               input_type="number", 
                               required="False")
    date = TextQuestion(title="Date",
                        input_type="date",
                        required="False" )
#############################################################################################################################
########################## WHODAS 2.0 - 36 items - auto-rapporté ############################################################
class Page2(Form):
    intro = HtmlBlock (title="WHODAS 2.0",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Ce questionnaire vous demande des questions &agrave; propos des <strong>difficult&eacute;s</strong> <strong>engendr&eacute;es</strong> <strong>par votre</strong> <strong>&eacute;tat de sant&eacute;</strong>.</h4>
<h4 style="text-align: justify;">Par condition de sant&eacute;, cela inclut les maladies, les troubles de sant&eacute; mentale, les probl&egrave;mes &eacute;motionnels, les blessures, les probl&egrave;mes reli&eacute;s &agrave; l&rsquo;alcool et aux drogues et les autres probl&egrave;mes de sant&eacute; qui peuvent &ecirc;tre de courte ou de longue dur&eacute;e (ex. probl&egrave;mes chroniques).</h4>
<h4 style="text-align: justify;">Pensez &agrave; la <strong>derni&egrave;re semaine</strong> et r&eacute;pondez aux questions selon &agrave; quel point cela &eacute;tait difficile pour vous de faire les activit&eacute;s suivantes. Pour chaque question, cochez <strong>une seule r&eacute;ponse</strong>.</h4>
</font></div> ''')
class Page3(Form): 
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
    

class Page4(Form):
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
                    "text": " Se déplacer à l'intérieur de votre maison ?"
                }, {
                    "value": "D2_4",
                    "text": " Sortir de la maison ?"
                }, {
                    "value": "D2_5",
                    "text": " Marcher une longue distance (ex. un kilomètre ou l'équivalent)"
                }
            ],
                                    all_rows_required = False)

class Page5(Form):
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


class Page6(Form):
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
                    "text": " Se faire des nouveaux amis ?"
                }, {
                    "value": "D4_5",
                    "text": " À quel point avez-vous eu des difficultés dans vos activités sexuelles ?"
                }
            ],
                                    all_rows_required = False)

class Page7(Form):
        D5_1 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de vos responsabilités ménagères (tâches ménagères, familles) ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_2 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches ménagères les plus importantes ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_3 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire toutes les activités ménagères que vous aviez besoin de faire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_4 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire vos activités ménagères aussi rapidement que nécessaire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_01 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_2} = '2' or {D5_2} = '3' or {D5_2} = '4' or {D5_2} = '5' or {D5_3} = '2' or {D5_3} = '3' or {D5_3} = '4' or {D5_3} = '5' or {D5_4} = '2' or {D5_4} = '3' or {D5_4} = '4' or {D5_4} = '5'")
        
class Page8(Form):
        D5_5 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de faire votre journée de travail/d'école ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_6 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches reliées au travail/à l'école ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_7 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire tout le travail que vous aviez besoin de faire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_8 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire le travail aussi rapidement que nécessaire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)   


        D5_9 = BooleanQuestion(title="Avez-vous besoin de travailler à un niveau moins élevé à cause d'un problème de santé ?",
                               required = False)
        
        D5_10 = BooleanQuestion(title="Gagnez-vous moins d'argent à cause d'un problème de santé ?",
                               required = False)
        
        D5_02 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de manquer le travail ou l'école pour une demi-journée ou plus à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_5} = '2' or {D5_5} = '3' or {D5_5} = '4' or {D5_5} = '5' or {D5_6} = '2' or {D5_6} = '3' or {D5_6} = '4' or {D5_6} = '5' or {D5_7} = '2' or {D5_7} = '3' or {D5_7} = '4' or {D5_7} = '5' or {D5_8} = '2' or {D5_8} = '3' or {D5_8} = '4' or {D5_8} = '5' ")
        
class Page9(Form):
        D6_1_4 = MatrixQuestion(title="Dans la dernière semaine, …",
                                    columns=[ "1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                    rows=[ "D6_1| À quel point est-ce problématique pour vous de vous joindre à des activités communautaires (ex. festivités, activités religieuses, etc.), de la même manière que les autres le peuvent ?","D6_2|À quel point avez-vous eu des problèmes à cause de barrières ou d'obstacles autour de vous ? ","D6_3|À quel point cela était problématique pour vous de vivre avec dignité à cause des attitudes et des actions des autres ?","D6_4|Combien de temps avez-vous passé sur votre condition de santé ou à gérer les conséquences engendrées par votre condition de santé ?"],
                                    all_rows_required = False)

class Page10(Form):
        D6_5_8 = MatrixQuestion(title="Dans la dernière semaine, …",
                                    columns=[ "1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                    rows=[ "D6_5|À quel point avez-vous été émotionnellement affecté par vos conditions de santé ?","D6_6|À quel point votre santé a affecté vos ressources financières ou celles de votre famille ?","D6_7|À quel point vos problèmes de santé ont été problématiques pour votre famille ?","D6_8| À quel point cela a-t-il été problématique de faire des choses par vous-même pour vous relaxer ou pour le plaisir ?"],
                                    all_rows_required = False)

class Page11(Form):
    H1 = TextQuestion(title="De manière générale, dans les 7 derniers jours, combien y a-t-il eu de jours où ces difficultés étaient présentes ?",
                      input_type="number",
                      required = False)
    H2 = TextQuestion(title="Dans les 7 derniers jours, combien y a-t-il eu de jours où vous étiez totalement incapable de faire vos activités habituelles ou votre travail à cause d'une condition de santé ?",
                      input_type="number",
                      required = False)
    H3 = TextQuestion(title="Dans les 7 derniers jours, sans compter les jours où vous en étiez totalement incapable, combien y a-t-il eu de jours où vous avez dû couper ou réduire vos activités habituelles ou votre travail à cause d'une condition de santé ?",
                      input_type="number",
                      required = False)

class Page12(Form):
    intro = HtmlBlock (title="Année Études",
                        html = '''<img src='/static/Etudes_quebec_age.png' alt='Ages_quebec' width='100%' height='100%'/>
                        <img src='/static/Etudes_quebec_annees.png' alt='Annees_quebec' width='100%' height='100%'/>''')
    WHOQOL_apropo1 = TextQuestion(title="Quel est votre niveau d'éducation ? (Nombre d'années totales d'études)",
                                input_type="number",
                                required = False)
    
    WHOQOL_apropo2 = DropdownQuestion(title="Quel est votre état civil?",
                                choices = ["1|Célibataire", "2|Séparé","3|Marié","4|Divorcé","5|Veuf"],
                                required = False)
    WHOQOL_apropo3 = BooleanQuestion(title="Êtes-vous présentement malade ?",
                               required = False)
    WHOQOL_apropo4 = CommentQuestion(title="S'il y avait quelque chose qui n'allait pas avec votre santé, vous croyez que cela serait quoi ?",
                               required = False)


class Profile(Form):
    page_1 = FormPage(Page1, title="")
    page_2 = FormPage(Page2, title="WHODAS 2.0 - 36 items - auto-rapporté")
    page_3 = FormPage(Page3, title="")
    page_4 = FormPage(Page4, title="")
    page_5 = FormPage(Page5, title="")
    page_6 = FormPage(Page6, title="")
    page_7 = FormPage(Page7, title="")
    page_8 = FormPage(Page8, title="")
    page_9 = FormPage(Page9, title="")
    page_10 = FormPage(Page10, title="")
    page_11 = FormPage(Page11, title="")
    page_12 = FormPage(Page12, title="")

import webbrowser
def open_browser():
    # Windows
    chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
    browser = webbrowser.get(chrome_path)
    browser.args.append('--start-fullscreen')
    browser.open_new('http://127.0.0.1:5000/')
    #webbrowser.get(chrome_path).open_new('http://127.0.0.1:5000/')


app = Flask(__name__)

@app.route("/", methods=("GET",))
def form():
    form = Profile(title="Prisme", theme="modern",
                   platform="jquery", navigate_to_url="/merci",locale="fr")
                   #resource_url="/static/node_modules")
    return form.render_html()

from datetime import datetime
date_time = datetime.now()
current_time = date_time.strftime("%Hh%Mm%Ss")
current_date = date_time.strftime("%b-%d-%Y")

@app.route("/", methods=("POST",))
def post():
    form_data = request.get_json()
    # Here, we would save to a database or something
    print(form_data)
    current_f_name, extension = os.path.splitext(os.path.basename(__file__))
    project_name = form_data.get('projet')
    subject_name = form_data.get('participant')
    date = form_data.get('date')
    if date == None:
        date = current_date
        
    save_f_name = f'{project_name}_{subject_name}_{current_f_name}_{date}_{current_time}'
    print(save_f_name)
    print(os.getcwd())
    df = pd.DataFrame.from_dict(form_data, orient="index")
    if not os.path.exists('result/'):
       os.makedirs('result/')
    df.to_csv(f'result/{save_f_name}.csv')
    return redirect("/merci")

@app.route("/merci")
def merci():
    return "Merci pour votre participation"

if __name__ == "__main__":
      app.debug = False
      Timer(2, open_browser).start();
      app.run(port=5000)