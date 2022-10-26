import numpy as np

def real_state_f():


    houses = {
        'flats': ['flat1', 'flat2', 'flat3', 'flat4'],
        'surface': [620, 3280, 1900, 1320],
        'bedrooms': [1, 4, 2, 3],
        'floors': [1, 2, 2, 3],
        'price': [244, 671, 504, 510],
    }

    x = np.asarray([[1, 1, 1, 1], houses['surface'], houses['bedrooms'], houses['floors']])
    x = x.transpose()

    y = np.array(houses['price'])
    y = y.reshape(4, 1)

    z = np.linalg.solve(x, y)

    print(x)
    print(y)
    print(z)

    new_home = np.array([1, 3000, 5, 1])
    print(x)
    print(new_home)
    X2 = np.vstack([x, new_home])
    print(X2)


    # permet de trouver le prix de la maison
    # metohde Jo
    # res = new_home[0] * z[0] + new_home[1] * z[1] + new_home[2] * z[2] + new_home[3] * z[3]
    # res = int(res[0])

    # metohde Numpy
    res = np.dot(new_home, z)
    print(f"la valeur de la maison par rapport a toute les informations est estimé a {sum(res)}")

    y0 = np.array([700])
    Y2 = np.vstack([y, y0])
    print("y:   ", y)

    print("y2:   ", Y2)

    try:
        # ne fonctionne pas car la matrice n'est plus carrée
        res_final = np.linalg.solve(X2, Y2)
        print(res_final)
    except:
        print("le calcul res_final = np.linalg.solve(X2, Y2)")
        print("ne fonctionne pas car la matrice n'est plus carrée")

