import inquirer as inquirer
import pandas as pd
import numpy as np

from low_of_large_numbers import low_large_number_f
from proba_exercice import proba_exercice_f
from real_estate_exercice import real_state_f

choose_exercice = ["probabiltys", "real_estate_exercice", "low_of_large_numbers", "exit"]

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
    if answers["exercice"] == choose_exercice[1]:
        print("lancement de probabiltys")
        real_state_f()
    if answers["exercice"] == choose_exercice[2]:
        print("lancement de probabiltys")
        low_large_number_f()
    if answers["exercice"] == 'exit':
        print("fermeture de l'application")
        end = True


