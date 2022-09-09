import pandas

data = pandas.read_csv("Central_Park_Squirrel.csv")
print(data.columns)
print(data["Primary Fur Color"])

