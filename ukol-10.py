import pandas

teplota = pandas.read_csv("temperature.csv")
print(teplota.head())

teplota = teplota.set_index("City")
print(teplota.loc[["Prague"]])

print(teplota[teplota["AvgTemperature"] > 80])

print(teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")])

extremni_hodnoty = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)]
print(extremni_hodnoty)

import pytemperature
teplota["AvgTemperatureCelsia"] = pytemperature.f2c(teplota["AvgTemperature"])

print(teplota[teplota["AvgTemperatureCelsia"] > 30])

print(teplota[(teplota["AvgTemperatureCelsia"] > 15) & (teplota["Region"] == "Europe")])

extremni_hodnotyC = teplota[(teplota["AvgTemperatureCelsia"] > 30) | (teplota["AvgTemperatureCelsia"] < -10)]
print(extremni_hodnotyC)


