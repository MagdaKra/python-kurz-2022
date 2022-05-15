import pandas

animals = pandas.read_csv("adopce-zvirat.csv", sep=';')
print(animals)

animals = pandas.read_csv('adopce-zvirat.csv', index_col="nazev_cz")
print("nazev_cz".index.is_unique)

animals.sort_index()

print(animals.loc[['Outloň váhavý']])

print(animals.loc["Želva Smithova" : "Želva žlutočelá"])
