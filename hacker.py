import pandas as pd
data = pd.read_csv('hacker.csv')
print(data)
log = data['Log_ID'].tolist()
ip = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
kb = data['Data_KB'].tolist()
time = data['Time'].tolist()
description = data['Description'].tolist()
filtered = []
def account_compromised():
    for i in range(len(description)):
        if "Failed" in description[i]:
            filtered.append([i])
    print(filtered)
    filtered.clear()
def data_stolen():
    for i in range(len(kb)):
        if kb[i] > 4000:
            filtered.append([i])
    print(filtered)
    filtered.clear()
def forced_users():
    for i in range(len(description)):
        if "Reset" in description[i]:
            filtered.append([i])
    print(len(filtered))
    filtered.clear()
account_compromised()
print(data.loc[196])
data_stolen()
print(data.loc[199])
print("Users affected:")
forced_users()
