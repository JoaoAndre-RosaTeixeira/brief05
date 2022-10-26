import inquirer as inquirer
import pandas as pd
import numpy as np

from proba_exercice import proba_exercice_f

# assert (round(prior_probability_pd(), 2) == 64.29)
# assert (round(prior_probability_li(), 2) == 64.29)
# assert (round(likelihood("Rainy", "No"), 2) == 60)
choose_exercice = ["probabiltys", "exit"]

end = False

while end is False:
    questions = [
            inquirer.List('exercice',
                          message="What end you desire ?",
                          choices=choose_exercice,
                          ),
        ]

    answers = inquirer.prompt(questions)

    if answers["exercice"] == choose_exercice[0]:
        print("lancement de probabiltys")
        proba_exercice_f()
    if answers["exercice"] == 'exit':
        print("fermeture de l'application")
        end = True


