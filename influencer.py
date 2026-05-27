#influencer corrie
import pandas as pd
data = pd.read_csv('influencer.csv')
print(data)
month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subscriber = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filtered = []
def humble_beginnings():
    for i in range(len(views)):
        if views[i] <= 2000:
            filtered.append([i])
            print(month[i])
        filtered.clear()
def golden_age():
    for i in range(len(subscriber)):
        if subscriber[i] >= 50000:
            filtered.append([i])
            print(month[i])
        filtered.clear()
def scandel():
    for i in range(len(revenue)):
        if revenue[i] == 0:
            filtered.append([i])
            print(month[i])
        filtered.clear()
print("Views > 2000:")
humble_beginnings()
print("Growth > 50000:")
golden_age()
print("No growth:")
scandel()
