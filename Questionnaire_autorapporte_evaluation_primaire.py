# Flask 
from flask import Flask
from flask import redirect
from flask import request
# Questions
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
# Other
import os
import pandas as pd
import webbrowser
from threading import Timer


class Page1(Form):
    intro = HtmlBlock (title="test html",
                        html = '''<div><font size="5">
<h4 style="text-align: justify;">Questionnaire auto-rapporté - Évaluation initiale </h4> </font></div> ''')
    projet = TextQuestion(title="Projet:")
    participant = TextQuestion(title="Numero du participant:",
                               input_type="number", 
                               required="True")
    date = TextQuestion(title="Date",
                        input_type="date",
                        required="True" )
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
                                    all_rows_required = True)
    

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
                    "text": " Marcher une longue distance (ex. un kilomètre ou l'équivalent) ?"
                }
            ],
                                    all_rows_required = True)

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
                                    all_rows_required = True)


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
                                    all_rows_required = True)

class Page7(Form):
        D5_1 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de s'occuper de vos responsabilités ménagères (tâches ménagères, familles)",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_2 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches ménagères les plus importantes ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_3 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire toutes les activités ménagères que vous aviez besoin de faire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_4 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire vos activités ménagères aussi rapidement que nécessaire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_01 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_2} = '2' or {D5_2} = '3' or {D5_2} = '4' or {D5_2} = '5' or {D5_3} = '2' or {D5_3} = '3' or {D5_3} = '4' or {D5_3} = '5' or {D5_4} = '2' or {D5_4} = '3' or {D5_4} = '4' or {D5_4} = '5'")
        
class Page8(Form):
        D5_5 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire votre journée de travail/d'école",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_6 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de bien faire vos tâches reliées au travail/à l'école ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_7 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire tout le travail que vous aviez besoin de faire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)
        
        D5_8 = RadioGroupQuestion(title="Dans la dernière semaine, à quel point avez-vous trouvé difficile de faire le travail aussi rapidement que nécessaire ?",
                                  choices=["1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                  required = True)   


        D5_9 = BooleanQuestion(title="Avez-vous besoin de travailler à un niveau moins élevé à d'un problème de santé ?",
                               required = True)
        
        D5_10 = BooleanQuestion(title="Gagnez-vous moins d'un problème de santé ?",
                               required = True)
        
        D5_02 = TextQuestion(title="Dans les 7 derniers jours, combien de jours cela vous est-il arrivé de réduire ou de ne pas faire du tout de tâches ménagères à cause de votre condition de santé ?",
                             required="False",
                             input_type="number",
                             visible_if="{D5_5} = '2' or {D5_5} = '3' or {D5_5} = '4' or {D5_5} = '5' or {D5_6} = '2' or {D5_6} = '3' or {D5_6} = '4' or {D5_6} = '5' or {D5_7} = '2' or {D5_7} = '3' or {D5_7} = '4' or {D5_7} = '5' or {D5_8} = '2' or {D5_8} = '3' or {D5_8} = '4' or {D5_8} = '5' ")
        
class Page9(Form):
        D6_1_4 = MatrixQuestion(title="Dans la dernière semaine, …",
                                    columns=[ "1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                    rows=[ "D6_1| À quel point est-ce problématique pour vous de vous joindre à des activités communautaires (ex. festivités, activités religieuses, etc.), de la même manière que les autres le peuvent ?","D6_2|À quel point avez-vous eu des problèmes à cause de barrières ou d'obstacles autour de vous ? ","D6_3|À quel point cela était problématique pour vous de vivre avec dignité à cause des attitudes et des actions des autres ?","D6_4|Combien de temps avez-vous passé sur votre condition de santé ou à gérer les conséquences engendrées par votre condition de santé ?"],
                                    all_rows_required = True)

class Page10(Form):
        D6_5_8 = MatrixQuestion(title="Dans la dernière semaine, …",
                                    columns=[ "1|Aucunement difficile", "2|Légèrement difficile","3|Modérément difficile","4|Sévèrement difficile","5|Extrêmement difficile ou je ne pouvais pas le faire"],
                                    rows=[ "D6_5|À quel point avez-vous été émotionnellement affecté par vos conditions de santé ?","D6_6|À quel point votre santé a affecté vos ressources financières ou celles de votre famille ?","D6_7|À quel point vos problèmes de santé ont été problématiques pour votre famille ?","D6_8| À quel point cela a-t-il été problématique de faire des choses par vous-même pour vous relaxer ou pour le plaisir ?"],
                                    all_rows_required = True)

class Page11(Form):
    H1 = TextQuestion(title="De manière générale, dans les 7 derniers jours, combien y a-t-il eu de jours où ces difficultés étaient présentes ?",
                      input_type="number",
                      required = True)
    H2 = TextQuestion(title="Dans les 7 derniers jours, combien y a-t-il eu de jours où vous étiez totalement incapable de faire vos activités habituelles ou votre travail à cause d'une condition de santé ?",
                      input_type="number",
                      required = True)
    H3 = TextQuestion(title="Dans les 7 derniers jours, sans compter les jours où vous en étiez totalement incapable, combien y a-t-il eu de jours où vous avez dû couper ou réduire vos activités habituelles ou votre travail à cause d'une condition de santé ?",
                      input_type="number",
                      required = True)

class Page12(Form):
    intro = HtmlBlock (title="Année Études",
                        html = '''<img src='/static/Etudes_quebec_age.png' alt='Ages_quebec' width='100%' height='100%'/>
                        <img src='/static/Etudes_quebec_annees.png' alt='Annees_quebec' width='100%' height='100%'/>''')
    WHOQOL_apropo1 = TextQuestion(title="Quel est votre niveau d'éducation ? (Nombre d'années totales d'études)",
                                input_type="number",
                                required = True)
    
    WHOQOL_apropo2 = DropdownQuestion(title="Quel est votre état civil?",
                                choices = ["1|Célibataire", "2|Séparé","3|Marié","4|Divorcé","5|Veuf"],
                                required = True)
    WHOQOL_apropo3 = BooleanQuestion(title="Êtes-vous présentement malade ?",
                               required = True)
    WHOQOL_apropo4 = CommentQuestion(title="S'il y avait quelque chose qui n'allait pas avec votre santé, vous croyez que cela serait quoi ?",
                               required = True)

#####################################################################################################################################################################################
############################# 3. WHOQOL-BREF - 26 items - auto-rapporté ##############################################################################################################
class Page13(Form):
    intro = HtmlBlock (title="test html",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Ce questionnaire vous demande ce que vous pensez de votre qualité de vie, de votre santé ou des autres sphères de votre vie.</h4>
<h4 style="text-align: justify;">S'il vous plaît, répondre à toutes les questions. Si vous n'êtes pas certain de votre réponse, choisissez celle qui apparaît le plus appropriée. Cela peut souvent être la première réponse à laquelle vous avez pensé. </h4>
<h4 style="text-align: justify;">Gardez à l'esprit vos standards, espoirs, plaisirs et préoccupations. Nous vous demandons de répondre en fonction de ce que vous pensiez de votre vie lors de la dernière semaine. Lisez chaque question et cochez votre réponse. </h4>
</font></div> ''')


class Page14(Form):
        WHOQOL_1 = RadioGroupQuestion(title="Comment évalueriez-vous votre qualité de vie ?",
                                  choices=["1|Très pauvre", "2|Pauvre","3|Ni pauvre ni bonne","4|Bonne","5|Très bonne"],
                                  required = True)
        
        WHOQOL_2 = RadioGroupQuestion(title="À quel point êtes-vous satisfait de votre santé ?",
                                  choices=["1|Très insatisfait", "2|Insatisfait","3|Ni satisfait ni insatisfait","4|Satisfait","5|Très satisfait"],
                                  required = True)
        
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
                                    all_rows_required = True)
    

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
                                    all_rows_required = True)
    
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
                                    all_rows_required = True)
    WHOQOL_15 = RadioGroupQuestion(title="Comment est votre capacité à vous déplacer ?",
                                  choices=["1|Très pauvre", "2|Pauvre","3|Ni pauvre ni bonne","4|Bonne","5|Très bonne"],
                                  required = True)

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
                    "text": "Très satisfait"
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
                                    all_rows_required = True)
    
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
                    "text": " Très satisfait"
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
                                    all_rows_required = True)
    
    
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
                    "text": "Très satisfait"
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
                                    all_rows_required = True)
    
    WHOQOL_26 = RadioGroupQuestion(title="À quelle fréquence ressentez-vous des sentiments négatifs, comme une mauvaise humeur, le désespoir, l'anxiété, la dépression ? ",
                                  choices=["1|Jamais", "2|Rarement","3|Assez souvent","4|Très souvent","5|Toujours"],
                                  required = True)
###########################################################################################################################################################################################################
############################################### DASS-21 #############################################################################################################################################################    
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
                    "text": "J'ai eu de la difficulté à me détendre."
                }, {
                    "value": "DASS_2",
                    "text": " J'ai été conscient(e) d'avoir la bouche sèche."
                }, {
                    "value": "DASS_3",
                    "text": " J'ai l'impression de ne pas pouvoir ressentir d'émotion positive."
                }, {
                    "value": "DASS_4",
                    "text": "J'ai eu de la difficulté à respirer (par exemple, respirations excessivement rapides, essoufflement sans effort physique)."
                }, {
                    "value": "DASS_5",
                    "text": "J'ai eu de la difficulté à initier de nouvelles activités."
                }, {
                    "value": "DASS_6",
                    "text": "J'ai eu tendance à réagir de façon exagérée."
                }, {
                    "value": "DASS_7",
                    "text": "J'ai eu des tremblements (par exemple, des mains)."
                }
            ],
                                    all_rows_required = True)    

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
                                    all_rows_required = True)  
    
    
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
                    "text": " J'ai eu le sentiment de ne pas valoir grand chose comme personne."
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
                                    all_rows_required = True)
########################################################################################################################################################################################
################################### CAPE-15 #############################################################################################################################################    
class Page25(Form):
    intro = HtmlBlock (title="CAPE-15",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Pour chaque item, indiquez à quelle fréquence vous vous êtes senti de cette manière dans la dernière semaine.</h4>
<h4 style="text-align: justify;">Indiquez votre choix en cochant la case qui vous correspond.</h4>
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
                    "text": " Avez-vous senti que vous étiez persécuté(e) d'une manière ou d'une autre ? "
                }, {
                    "value": "CAPE_4",
                    "text": "Avez-vous senti qu'il y avait un complot contre vous ?"
                }, {
                    "value": "CAPE_5",
                    "text": " Vous êtes-vous senti comme si des appareils électriques tels que des ordinateurs pouvaient influencer votre façon de penser?"
                }
            ],
                                    all_rows_required = True) 
    
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
                    "text": " Avez-vous ressenti que l'on tentait de vous voler/vous enlever vos pensées de votre tête?"
                }, {
                    "value": "CAPE_8",
                    "text": " Vous êtes-vous senti comme si les pensées de votre tête n'étaient pas les vôtres ? "
                }, {
                    "value": "CAPE_9",
                    "text": "Vos pensées ont-elles été si vives que vous craigniez que d'autres personnes ne les entendent ?"
                }, {
                    "value": "CAPE_10",
                    "text": " Avez-vous entendu vos pensées vous revenir en échos ?"
                }
            ],
                                    all_rows_required = True)

class Page28(Form): 
    CAPE_11_15 = MatrixQuestion(title=" Indiquez à quelle fréquence vous vous êtes senti de cette manière dans la dernière semaine.",
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
                    "value": "CAPE_11 ",
                    "text": " Avez-vous senti que vous étiez sous le contrôle d'une force ou d'un autre pouvoir autre que vous-même ?"
                }, {
                    "value": "CAPE_12",
                    "text": " Avez-vous entendu des voix lorsque vous étiez seul(e) ?"
                }, {
                    "value": "CAPE_13",
                    "text": " Avez-vous entendu des voix se parler entre elles lorsque vous étiez seul(e) ? "
                }, {
                    "value": "CAPE_14",
                    "text": " Vous etes-vous senti comme si un double avait pris la place d'un membre de la famille, d'un ami ou d'une connaissance ?"
                }, {
                    "value": "CAPE_15",
                    "text": " Avez-vous vu des objets, des personnes ou des animaux que les autres ne peuvent pas voir ?"
                }
            ],
                                    all_rows_required = True)   
##################################################################################################################################################################
######################################## Altman Scale #############################################################################################################    

class Page29(Form):
    intro = HtmlBlock (title="Altman",
                        html = '''<div><font size="+1">
<h4 style="text-align: justify;">Il y a 5 groupes d'énoncés sur ce questionnaire: lisez attentivement chaque groupe d'énoncés.</h4>
<h4 style="text-align: justify;">Choisissez, dans chaque groupe, l'affirmation qui décrit le mieux la façon dont vous vous sentez la semaine passée.</h4>
<h4 style="text-align: justify;"> Remarque: le mot « occasionnellement » signifie une ou deux fois; « Souvent » signifie plusieurs fois et « fréquemment » signifie la plupart du temps.</h4>
</font></div> ''')

    Altman_group1 = DropdownQuestion(title="Groupes d'énoncés 1 ",
                                     choices=["0|Je ne me sens pas plus heureux ni de meilleure humeur que d'habitude",
                                              "1|Je me sens occasionnellement plus heureux ou de meilleure humeur que d'habitude",
                                              "2|Je me sens souvent plus heureux ou de meilleure humeur que d'habitude",
                                              "3|Je me sens fréquemment plus heureux ou de meilleure humeur que d'habitude",
                                              "4|Je me sens tout le temps plus heureux ou de meilleure humeur que d'habitude"],
                                     required = True)
    
    Altman_group2 = DropdownQuestion(title="Groupes d'énoncés 2",
                                     choices=["0|Je ne me sens pas plus confiant que d'habitude.",
                                              "1|Je me sens occasionnellement plus confiant que d'habitude",
                                              "2|J'ai souvent plus confiance en moi que d'habitude",
                                              "3|Je me sens fréquemment plus confiant que d'habitude",
                                              "4|Je me sens extrêmement confiant tout le temps"],
                                     required = True)
    
    Altman_group3 = DropdownQuestion(title="Groupes d'énoncés 3",
                                     choices=["0|Je n'ai pas besoin de moins de sommeil que d'habitude",
                                              "1|J'ai occasionnellement besoin de moins de sommeil que d'habitude",
                                              "2|J'ai souvent besoin de moins de sommeil que d'habitude",
                                              "3|J'ai fréquemment besoin de moins de sommeil que d'habitude",
                                              "4|Je peux rester éveillé toute la journée et toute la nuit et je ne me sens toujours pas fatigué"],
                                     required = True)
    
    Altman_group4 = DropdownQuestion(title="Groupes d'énoncés 4",
                                     choices=["0|Je ne parle pas plus que d'habitude",
                                              "1|Je parle occasionnellement plus que d'habitude",
                                              "2|Je parle souvent plus que d'habitude",
                                              "3|Je parle fréquemment plus que d'habitude",
                                              "4|Je parle constamment et je ne peux pas être interrompu"],
                                     required = True)
    
    Altman_group5 = DropdownQuestion(title="Groupes d'énoncés 5",
                                     choices=["0|Je n'ai pas été plus actif (que ce soit socialement, sexuellement, au travail, à la maison ou à l'école) que d'habitude",
                                              "1|J'ai occasionnellement été plus actif que d'habitude",
                                              "2|J'ai souvent été plus actif que d'habitude",
                                              "3|J'ai fréquemment été plus actif que d'habitude",
                                              "4|Je suis constamment actif ou tout le temps en déplacement"],
                                     required = True)
################################################################################################################################################################################################
######################################### Consommation #########################################################################################################################################
class AutresConsommation(Form):
    autres_conso = TextQuestion(title='Rajoutez des lignes au besoin', is_required=False)
    
class Page30(Form):
    intro = HtmlBlock (title="Consomation",
                        html = '''<div><font size="+1">
<h4 style="text-align:justify;"> Complétez le formulaire en vous basant sur votre consommation des 7 derniers jours.</h4>
</font></div> ''')
    date_debut_consomation = TextQuestion(title="Date du début de la période de 7 jours : ",
                             input_type="date",
                             required="False")
    conso_1 = BooleanQuestion(title="Lors des 7 derniers jours, avez-vous consommé de l'alcool ou des drogues ?")
    conso_2 = TextQuestion(title="Combien de fois avez-vous consommé de l'alcool ?",
                                                 input_type="number",
                                                 visible_if="{conso_1} = True",
                                                 required="False")
    conso_3_12 = MatrixQuestion(title="Lors des 7 derniers jours, avez-vous consommé …",
                                    columns=[ "0|Non", "1|Oui"],
                                    rows=[ "conso_3| Cannabinoïdes / Marijuana ",
                                          "conso_4| Cocaïne",
                                          "conso_5| Crack",
                                          "conso_6| Stimulants de type amphétamine",
                                          "conso_7| Analgésiques opioïdes, y compris la méthadone",
                                          "conso_8| Héroïne",
                                          "conso_9| Hallucinogènes, y compris MDMA / ecstasy",
                                          "conso_10| Sédatifs et hypnotiques, à l'exclusion des benzodiazépines",
                                          "conso_11| Benzodiazépines",
                                          "conso_12| Inhalants"],
                                    has_other = True)
    conso_13_bool = BooleanQuestion(title="Lors des 7 derniers jours, avez-vous consommé d'autres drogues que celles montionnées si haut?")
    conso_13 = FormPanel(AutresConsommation,
                         name="conso_13",
                         title=" Specifiez en ecrivant le nom de la drogue.",
                         visible_if="{conso_13_bool} = True",
                         dynamic=True
                         )
    
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
    page_13 = FormPage(Page13, title="WHOQOL-BREF - 26 items - auto-rapporté")
    page_14 = FormPage(Page14, title="")
    page_15 = FormPage(Page15, title="")
    page_16 = FormPage(Page16, title="")
    page_17 = FormPage(Page17, title="")
    age_18 = FormPage(Page18, title="")
    page_19 = FormPage(Page19, title="")
    page_20 = FormPage(Page20, title="")
    page_21 = FormPage(Page21, title="DASS-21")
    page_22 = FormPage(Page22, title="")
    page_23 = FormPage(Page23, title="")
    page_24 = FormPage(Page24, title="")
    page_25 = FormPage(Page25, title="CAPE-15")
    page_26 = FormPage(Page26, title="")
    page_27 = FormPage(Page27, title="")
    page_28 = FormPage(Page28, title="")
    page_29 = FormPage(Page29, title="Altman")
    page_30 = FormPage(Page30, title="Suivi chronologique - Consommation")
    


# auntomatic web browser popup in full screen
def open_browser():
    # Windows
    chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
    browser = webbrowser.get(chrome_path)
    browser.args.append('--start-fullscreen')
    browser.open_new('http://127.0.0.1:5000/')


app = Flask(__name__)

@app.route("/", methods=("GET",))
def form():
    form = Profile(title="Prisme", theme="modern",
                   platform="jquery", navigate_to_url="/merci",locale="fr")
                   #resource_url="/static/node_modules") ##uncomment if you administer the form offline
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
        
    save_f_name = f'{project_name.replace(" ", "_")}_{subject_name}_{current_f_name.replace(" ", "_")}_{date}_{current_time}'
    print(save_f_name)
    print(os.getcwd())
    df = pd.DataFrame.from_dict(form_data, orient="index")
    
    # save data locally
    base_path = os.path.expanduser('~')
    local_path = os.path.join(base_path,'result')
    if not os.path.exists(local_path):
       os.makedirs(local_path)
    file_name = os.path.join(local_path, f'{save_f_name}.csv')
    df.to_csv(file_name)
    
    # Send to remote server
    os.chdir(local_path)
    backup_command = f'scp -r {save_f_name}.csv elm:/data/orban/data/prisme_questions/result/.'
    os.system(backup_command)
    return redirect("/merci")

@app.route("/merci")
def merci():
    return "Merci pour votre participation"

if __name__ == "__main__":
      app.debug = False
      Timer(2, open_browser).start();
      app.run(port=5000)