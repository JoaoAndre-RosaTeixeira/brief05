import numpy as np

houses = {
    'flats': ['flat1', 'flat2', 'flat3', 'flat4'],
    'surface': [620, 3280, 1900, 1320],
    'bedrooms': [1, 4, 2, 3],
    'floors': [1, 2, 2, 3],
    'price': [244, 671, 504, 510],
}

x = np.asarray([houses['surface'], houses['bedrooms'], houses['floors'], [1, 1, 1, 1]])
x = x.transpose()

y = np.array(houses['price'])
y = y.reshape(4, 1)

z = np.linalg.solve(x, y)
print(x)

print(y)
print(z)

new_home = np.array([3000, 5, 1, 1]).reshape(4, 1)
print(new_home)
res = new_home[0] * z[0] + new_home[1] * z[1] + new_home[2] * z[2] + new_home[3] * z[3]
res = int(res[0])
print(res)


a = (z[1] + z[2]) * (z[3] * 700000)
b = (z[0] + z[2]) * (z[3] * 700000)
c = (z[0] + z[1]) * (z[3] * 700000)
print(f"surface est = {a}")
print(f"bedrooms est = {b}")
print(f"floors est = {c}")