import pandas

animals = pandas.read_csv("adopce-zvirat.csv", sep=';')
print(animals)

print (animals.shape)
print(animals.info())
print(animals.columns)

animals = animals.set_index("id")
print(animals.index)
# print(animals.loc['34'])

print(animals.iloc[[35]])
print(animals.iloc[35, [0, 1]])
