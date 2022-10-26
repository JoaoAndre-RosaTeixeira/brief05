
import pandas as pd

def proba_exercice_f():
    play_data_example = ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']

    weather_data_example = ['Sunny', 'Overcast', 'Rainy', 'Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Sunny',
                            'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy']

    data_weaver = {"weather": weather_data_example,
                   "played": play_data_example

                   }
    weaver_dict = {
        "Weather": [],
        "Played": [],
        "No": [],
        "Total": []
    }
    probabiltys = {
        "Weather": [],
        "Proba(Played | Weather)": [],
        "Proba(No | Weather)": []
    }
    df_weaver = pd.DataFrame(data_weaver)
    df_weaver.head()

    def prior_probability_pd():
        a = df_weaver[df_weaver["played"] == 'Yes'].count()["played"]
        b = df_weaver["played"].count()
        c = a / b * 100
        print(f"{c} prior_probability_pd result")
        return c

    def prior_probability_li():
        count_played = 0
        for data in play_data_example:
            if data == 'Yes':
                count_played += 1

        res = count_played / len(play_data_example) * 100
        print(f"{res} prior_probability_li result")

        return res

    # def prior_probability_np():

    def likelihood(weather, condition):
        # print(df_weaver.loc[(df_weaver['weather'] == "Rainy") & (df_weaver['played'] == "No")].count()['weather']) #3 not played rainy
        # print(df_weaver.loc[(df_weaver['played'] == "No")].count()['weather']) #5 not played
        a = df_weaver.loc[(df_weaver['weather'] == weather) & (df_weaver['played'] == condition)].count()['weather']

        b = df_weaver.loc[(df_weaver['played'] == condition)].count()['weather']

        c = a / b * 100
        # print(f"{c} likelihood result")
        return c

    def no_likelihood(weather, condition):
        a = df_weaver.loc[(df_weaver['weather'] == weather) & (df_weaver['played'] == condition)].count()['weather']
        b = df_weaver.loc[(df_weaver['played'] == condition)].count()['weather']

        c = a / b * 100
        print(c)
        d = 100 - c
        return d

    def probabiltys_f(weaver_d, probabiltys_d):

        for weaver in df_weaver["weather"]:
            if weaver not in weaver_d["Weather"]:
                weaver_d["Weather"].append(weaver)
                a = df_weaver.loc[((df_weaver['weather'] == weaver) & (df_weaver['played'] == "Yes"))].count()['played']
                b = df_weaver.loc[((df_weaver['weather'] == weaver) & (df_weaver['played'] == "No"))].count()['played']

                weaver_d["Played"].append(a)
                weaver_d["No"].append(b)
                weaver_d["Total"].append(a + b)

                probabiltys_d["Weather"].append(weaver)
                probabiltys_d["Proba(Played | Weather)"].append(no_likelihood(weaver, 'No'))
                probabiltys_d["Proba(No | Weather)"].append(likelihood(weaver, 'No'))

        # probabiltys = pd.DataFrame(probabiltys)
        # probabiltys["Weather"].append("Total")
        # print(probabiltys.loc[((probabiltys["Played"]) & (probabiltys["Weather"] == "Total"))])
        # probabiltys.loc[((probabiltys["Played"]) & (probabiltys["Weather"] == "Total"))].append(probabiltys["Played"])

        weaver_dict = pd.DataFrame(weaver_d)
        probabiltys = pd.DataFrame(probabiltys_d)

        print(weaver_dict)
        print(probabiltys)
        print(
            f"il y a plus de chance que le match soit jouer plutôt qu'il soit annulé car il y a {int(probabiltys[probabiltys['Weather'] == 'Sunny']['Proba(Played | Weather)'].values)}% de chance qu'il fasse soleil.")
        print(
            f"il y a {int(probabiltys[probabiltys['Weather'] == 'Rainy']['Proba(No | Weather)'].values)}% de chance que le match soit annulé si il pleut")

    probabiltys_f(weaver_dict, probabiltys)
