from random import choices
from typing_extensions import Required
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
                        required="False")

class Page2(Form):
    intro = HtmlBlock (title="test html",
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
                    "text": " Se faire des nouveaux ami ?"
                }, {
                    "value": "D4_5",
                    "text": " À quel point avez-vous eu des difficultés dans vos activités sexuelles ?"
                }
            ],
                                    all_rows_required = False)

class Page7(Form):
        D5_1 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de vos responsabilités ménagères (tâches ménagères, familles)",
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
        D5_5 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de faire votre journée de travail/d'école",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_6 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches ménagères les plus importantes ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_7 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire toutes les activités ménagères que vous aviez besoin de faire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)
        
        D5_8 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire vos activités ménagères aussi rapidement que nécessaire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = False)   


        D5_9 = BooleanQuestion(title="Avez-vous besoin de travailler à un niveau moins élevé à d'un problème de santé ?",
                               required = False)
        
        D5_10 = BooleanQuestion(title="Gagnez-vous moins d'un problème de santé ?",
                               required = False)
        
        D5_02 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
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
                        html = '''<img src='/static/Annees_etudes_quebec.png' alt='Annees_etudes_quebec' width='100%' height='100%'/>''')
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


class Page13(Form):
    intro = HtmlBlock (title="test html",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Ce questionnaire vous demande ce que vous pensez de votre qualité de vie, de votre santé ou des autres sphères de votre vie.</h4>
<h4 style="text-align: justify;">S'il vous plaît, répondre à toutes les questions. Si vous n'êtes pas certain de votre réponse, choisissez celle qui apparaît le plus appropriée. Cela peut souvent être la première réponse à laquelle vous avez pensé. </h4>
<h4 style="text-align: justify;">Gardez à l'esprit vos standards, espoirs, plaisirs et préoccupations. Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.</h4>
</font></div> ''')


class Page14(Form):
        WHOQOL_1 = RadioGroupQuestion(title="Comment évalueriez-vous votre qualité de vie ?",
                                  choices=["1|Très pauvre", "2|Pauvre","3|Ni pauvre ni bonne","4|Bonne","5|Très bonne"],
                                  required = False)
        
        WHOQOL_2 = RadioGroupQuestion(title="À quel point êtes-vous satisfait de votre santé ?",
                                  choices=["1|Très insatisfait", "2|Insatisfait","3|Ni satisfait ni insatisfait","4|Satisfait","5|Très satisfait"],
                                  required = False)
        
class Page15(Form): 
    WHOQOL_3_6 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Pas du tout"
                }, {
                    "value": 2,
                    "text": "Un peu"
                }, {
                    "value": 3,
                    "text": "Modérément "
                }, {
                    "value": 4,
                    "text": "Beaucoup"
                }, {
                    "value": 5,
                    "text": "Extrêmement"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_3 ",
                    "text": "À quel point pensez-vous que la douleur physique vous empêche de faire ce que vous avez besoin de faire ?"
                }, {
                    "value": "WHOQOL_4",
                    "text": "Combien de traitements médicaux avez-vous besoin pour fonctionner dans votre vie de tous les jours ?"
                }, {
                    "value": "WHOQOL_5",
                    "text": "À quel point vous trouvez la vie agréable ?"
                }, {
                    "value": "WHOQOL_6",
                    "text": "À quel  point sentez-vous que votre vie a un sens ?"
                }
            ],
                                    all_rows_required = False)
    

class Page16(Form): 
    WHOQOL_7_9 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Pas du tout"
                }, {
                    "value": 2,
                    "text": "Légèrement"
                }, {
                    "value": 3,
                    "text": "Modérément "
                }, {
                    "value": 4,
                    "text": "Beaucoup"
                }, {
                    "value": 5,
                    "text": "Extrêmement"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_7 ",
                    "text": "À quel point êtes-vous capable de vous concentrer ?"
                }, {
                    "value": "WHOQOL_8",
                    "text": "À quel point vous vous sentez en sécurité dans votre vie de tous les jours ?"
                }, {
                    "value": "WHOQOL_9",
                    "text": "À quel point votre environnement physique est-il sain ?"
                }
            ],
                                    all_rows_required = False)
    
class Page17(Form): 
    WHOQOL_10_14 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Pas du tout"
                }, {
                    "value": 2,
                    "text": "Un peu"
                }, {
                    "value": 3,
                    "text": "Modérément "
                }, {
                    "value": 4,
                    "text": "La plupart du temps"
                }, {
                    "value": 5,
                    "text": "Complètement"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_10 ",
                    "text": "Avez-vous assez d'énergie pour votre vie de tous les jours ?"
                }, {
                    "value": "WHOQOL_11",
                    "text": "Êtes-vous capable d'accepter votre apparence physique ?"
                }, {
                    "value": "WHOQOL_12",
                    "text": "Avez-vous assez d'argent pour répondre à vos besoins ?"
                }, {
                    "value": "WHOQOL_13",
                    "text": "À quel point l'information que vous avez besoin pour votre vie de tous les jours vous est accessible ?"
                }, {
                    "value": "WHOQOL_14",
                    "text": "À quel point avez-vous des opportunités pour des activités de loisirs ?"
                }
            ],
                                    all_rows_required = False)
    WHOQOL_15 = RadioGroupQuestion(title="Comment est votre capacité à vous déplacer ?",
                                  choices=["1|Très pauvre", "2|Pauvre","3|Ni pauvre ni bonne","4|Bonne","5|Très bonne"],
                                  required = False)

class Page18(Form): 
    WHOQOL_16_19 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Très insatisfait"
                }, {
                    "value": 2,
                    "text": "Insatisfait"
                }, {
                    "value": 3,
                    "text": "Ni satisfait ni insatisfait "
                }, {
                    "value": 4,
                    "text": "Satisfait"
                }, {
                    "value": 5,
                    "text": "Satisfait"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_16 ",
                    "text": "À quel point êtes-vous satisfait de votre sommeil ?"
                }, {
                    "value": "WHOQOL_17",
                    "text": "À quel point êtes-vous satisfait de votre habileté à performer dans vos activités quotidiennes ?"
                }, {
                    "value": "WHOQOL_18",
                    "text": "À quel point êtes-vous satisfait de votre capacité à travailler ?"
                }, {
                    "value": "WHOQOL_19",
                    "text": "À quel point êtes-vous satisfait de vous-même ?"
                }
            ],
                                    all_rows_required = False)
    
class Page19(Form): 
    WHOQOL_20_23 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Très insatisfait"
                }, {
                    "value": 2,
                    "text": "Insatisfait"
                }, {
                    "value": 3,
                    "text": "Ni satisfait ni insatisfait "
                }, {
                    "value": 4,
                    "text": "Satisfait"
                }, {
                    "value": 5,
                    "text": "Satisfait"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_20 ",
                    "text": "À quel point êtes-vous satisfaits de vos relations personnelles ?"
                }, {
                    "value": "WHOQOL_21",
                    "text": "À quel point êtes-vous satisfait de votre vie sexuelle ?"
                }, {
                    "value": "WHOQOL_22",
                    "text": "À quel point êtes-vous satisfait du support que vous recevez de vos amis ?"
                }, {
                    "value": "WHOQOL_23",
                    "text": "À quel point êtes-vous satisfait des conditions de votre milieu de vie ?"
                }
            ],
                                    all_rows_required = False)
    
    
class Page20(Form): 
    WHOQOL_24_25 = MatrixQuestion(title="Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Très insatisfait"
                }, {
                    "value": 2,
                    "text": "Insatisfait"
                }, {
                    "value": 3,
                    "text": "Ni satisfait ni insatisfait "
                }, {
                    "value": 4,
                    "text": "Satisfait"
                }, {
                    "value": 5,
                    "text": "Satisfait"
                }
            ],
                                    rows=[
                {
                    "value": "WHOQOL_24 ",
                    "text": "À quel point êtes-vous satisfait de votre accès à des soins de santé ?"
                }, {
                    "value": "WHOQOL_25",
                    "text": "À quel point êtes-vous satisfait de votre moyen de transport ?"
                }
            ],
                                    all_rows_required = False)
    
    WHOQOL_25 = RadioGroupQuestion(title="À quelle fréquence ressentez-vous des sentiments négatifs, comme une mauvaise humeur, le désespoir, l'anxiété, la dépression ? ",
                                  choices=["1|Jamais", "2|Rarement","3|Assez souvent","4|Très souvent","5|Toujours"],
                                  required = False)
    
class Page21(Form):
    intro = HtmlBlock (title="DASS-21",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Veuillez lire chaque énoncé et indiquez lequel correspond le mieux à votre expérience au cours de la dernière semaine.</h4>
<h4 style="text-align: justify;">Indiquez votre choix en cochant la case qui vous correspond.</h4>
<h4 style="text-align: justify;"> Il n'y a pas de bonne ou de mauvaise réponse. Ne vous attardez pas trop longuement aux énoncés.</h4>
</font></div> ''')
    
class Page22(Form): 
    DASS_1_7 = MatrixQuestion(title="Indiquez lequel correspond le mieux à votre expérience au cours de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": " ne s'applique pas du tout à moi"
                }, {
                    "value": 2,
                    "text": "s'applique un peu à moi, ou une partie du temps"
                }, {
                    "value": 3,
                    "text": "s'applique beaucoup à moi, ou une bonne partie du temps "
                }, {
                    "value": 4,
                    "text": " s'applique entièrement à moi, ou la grande majorité du temps"
                }
            ],
                                    rows=[
                {
                    "value": "DASS_1 ",
                    "text": "J'ai eu de la difficulté à me détendre"
                }, {
                    "value": "DASS_2",
                    "text": " J'ai été conscient(e) d'avoir la bouche sèche"
                }, {
                    "value": "DASS_3",
                    "text": " J'ai été conscient(e) d'avoir la bouche sèche"
                }, {
                    "value": "DASS_4",
                    "text": "J'ai eu de la difficulté à respirer (par exemple, respirations excessivement rapides, essoufflement sans effort physique)."
                }, {
                    "value": "DASS_5",
                    "text": "J'ai eu de la difficulté à initier de nouvelles activités"
                }, {
                    "value": "DASS_6",
                    "text": "J'ai eu tendance à réagir de façon exagérée"
                }, {
                    "value": "DASS_7",
                    "text": "J'ai eu des tremblements (par exemple, des mains)"
                }
            ],
                                    all_rows_required = False)    

class Page23(Form): 
    DASS_8_14 = MatrixQuestion(title="Indiquez lequel correspond le mieux à votre expérience au cours de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": " ne s'applique pas du tout à moi"
                }, {
                    "value": 2,
                    "text": "s'applique un peu à moi, ou une partie du temps"
                }, {
                    "value": 3,
                    "text": "s'applique beaucoup à moi, ou une bonne partie du temps "
                }, {
                    "value": 4,
                    "text": " s'applique entièrement à moi, ou la grande majorité du temps"
                }
            ],
                                    rows=[
                {
                    "value": "DASS_8 ",
                    "text": " J'ai eu l'impression de dépenser beaucoup d'énergie nerveuse."
                }, {
                    "value": "DASS_9",
                    "text": " Je me suis inquiété(e) en pensant à des situations où je pourrais paniquer et faire de moi un(e) idiot(e)."
                }, {
                    "value": "DASS_10",
                    "text": " Je n'ai rien pu voir dans l'avenir qui me donnait de l'espoir."
                }, {
                    "value": "DASS_11",
                    "text": "Je me suis aperçu(e) que je devenais agité(e)."
                }, {
                    "value": "DASS_12",
                    "text": " J'ai trouvé difficile de décompresser."
                }, {
                    "value": "DASS_13",
                    "text": "Je me suis senti(e) abattu(e) et triste."
                }, {
                    "value": "DASS_14",
                    "text": "J'ai été intolérant(e) à tout ce qui m'empêchait de faire ce que j'avais à faire."
                }
            ],
                                    all_rows_required = False)  
    
    
class Page24(Form): 
    DASS_15_21 = MatrixQuestion(title="Indiquez lequel correspond le mieux à votre expérience au cours de la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": " ne s'applique pas du tout à moi"
                }, {
                    "value": 2,
                    "text": "s'applique un peu à moi, ou une partie du temps"
                }, {
                    "value": 3,
                    "text": "s'applique beaucoup à moi, ou une bonne partie du temps "
                }, {
                    "value": 4,
                    "text": " s'applique entièrement à moi, ou la grande majorité du temps"
                }
            ],
                                    rows=[
                {
                    "value": "DASS_15 ",
                    "text": " J'ai eu le sentiment d'être presque pris(e) de panique."
                }, {
                    "value": "DASS_16",
                    "text": " J'ai été incapable de me sentir enthousiaste au sujet de quoi que ce soit."
                }, {
                    "value": "DASS_17",
                    "text": " J'ai eu le sentiment de ne pas valoir grand chose comme personne"
                }, {
                    "value": "DASS_18",
                    "text": "J'ai eu l'impression d'être assez susceptible."
                }, {
                    "value": "DASS_19",
                    "text": " J'ai été conscient(e) des palpitations de mon cœur en l'absence d'effort physique (sensation d'augmentation de mon rythme cardiaque ou l'impression que mon cœur venait de sauter)."
                }, {
                    "value": "DASS_20",
                    "text": "J'ai eu peur sans bonne raison."
                }, {
                    "value": "DASS_21",
                    "text": "J'ai eu l'impression que la vie n'avait pas de sens."
                }
            ],
                                    all_rows_required = False)
    
class Page25(Form):
    intro = HtmlBlock (title="CAPE-15",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Veuillez lire chaque énoncé et indiquez lequel correspond le mieux à votre expérience au cours de la dernière semaine.</h4>
<h4 style="text-align: justify;">Indiquez votre choix en cochant la case qui vous correspond.</h4>
<h4 style="text-align: justify;"> Il n'y a pas de bonne ou de mauvaise réponse.</h4>
</font></div> ''')
    
    
class Page26(Form): 
    CAPE_1_5 = MatrixQuestion(title=" Indiquez à quelle fréquence vous vous êtes senti de cette manière dans la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Jamais"
                }, {
                    "value": 2,
                    "text": "Parfois"
                }, {
                    "value": 3,
                    "text": "Souvent"
                }, {
                    "value": 4,
                    "text": "Presque toujours"
                }
            ],
                                    rows=[
                {
                    "value": "CAPE_1 ",
                    "text": " Vous êtes-vous senti comme si les gens semblaient vous dire des choses en faisant allusions à quelque chose d'autre ou s'ils disaient des choses à double sens?"
                }, {
                    "value": "CAPE_2",
                    "text": " Avez-vous senti que certaines personnes n'étaient pas ce qu'elles semblaient être?"
                }, {
                    "value": "CAPE_3",
                    "text": " Avez-vous senti que vous étiez persécuté d'une manière ou d'une autre ? "
                }, {
                    "value": "CAPE_4",
                    "text": "Avez-vous senti qu'il y avait un complot contre vous ?"
                }, {
                    "value": "CAPE_5",
                    "text": " Vous êtes-vous senti comme si des appareils électriques tels que des ordinateurs pouvaient influencer votre façon de penser?"
                }
            ],
                                    all_rows_required = False) 
    
class Page27(Form): 
    CAPE_6_10 = MatrixQuestion(title=" Indiquez à quelle fréquence vous vous êtes senti de cette manière dans la dernière semaine.",
                                    columns=[
                {
                    "value": 1,
                    "text": "Jamais"
                }, {
                    "value": 2,
                    "text": "Parfois"
                }, {
                    "value": 3,
                    "text": "Souvent"
                }, {
                    "value": 4,
                    "text": "Presque toujours"
                }
            ],
                                    rows=[
                {
                    "value": "CAPE_6 ",
                    "text": " Avez-vous senti que les gens vous regardaient étrangement à cause de votre apparence?"
                }, {
                    "value": "CAPE_7",
                    "text": " Avez-vous senti que certaines personnes n'étaient pas ce qu'elles semblaient être?"
                }, {
                    "value": "CAPE_8",
                    "text": " Avez-vous senti que vous étiez persécuté d'une manière ou d'une autre ? "
                }, {
                    "value": "CAPE_9",
                    "text": "Avez-vous senti qu'il y avait un complot contre vous ?"
                }, {
                    "value": "CAPE_10",
                    "text": " Vous êtes-vous senti comme si des appareils électriques tels que des ordinateurs pouvaient influencer votre façon de penser?"
                }
            ],
                                    all_rows_required = False)   
    

class Profile(Form):
    page_1 = FormPage(Page1, title="")
    page_2 = FormPage(Page2, title="WHODAS 2.0 - 36 items - auto-rapporté")
    #page_3 = FormPage(Page3, title="")
    #page_4 = FormPage(Page4, title="")
    #page_5 = FormPage(Page5, title="")
    #page_6 = FormPage(Page6, title="")
    #page_7 = FormPage(Page7, title="")
    #page_8 = FormPage(Page8, title="")
    #page_9 = FormPage(Page9, title="")
    #page_10 = FormPage(Page10, title="")
    #page_11 = FormPage(Page11, title="")
    #page_12 = FormPage(Page12, title="")
    page_13 = FormPage(Page13, title="WHOQOL-BREF - 26 items - auto-rapporté")
    #page_14 = FormPage(Page14, title="")
    #page_15 = FormPage(Page15, title="")
    #page_16 = FormPage(Page16, title="")
    page_17 = FormPage(Page17, title="")
    page_18 = FormPage(Page18, title="")
    page_19 = FormPage(Page19, title="")
    page_20 = FormPage(Page20, title="")
    page_21 = FormPage(Page21, title="DASS-21")
    page_22 = FormPage(Page22, title="")
    page_23 = FormPage(Page23, title="")
    page_24 = FormPage(Page24, title="")
    page_25 = FormPage(Page25, title="CAPE-15")
    


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
    df = pd.DataFrame.from_dict(form_data, orient="index")
    df.to_csv('csvfile.csv')
    return redirect("/thanks")

@app.route("/thanks")
def thanks():
    return "Thanks for your information"

if __name__ == "__main__":
      app.debug = True
      #Timer(2, open_browser).start();
      app.run(port=5000)