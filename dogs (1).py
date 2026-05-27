#CORRIE DOG BREED (create) goal 2


#initialize
import pandas as pd
import webbrowser
data = pd.read_csv('dogs.csv')
min_weight = data['Minimum Weight'].tolist()
max_weight = data['Maximum Weight'].tolist()
dog_name = data['Name'].tolist()
dog_temperament = data['Temperament'].tolist()
dog_image = data['Image'].tolist()
filtered = []

#functions
def dog_finder():
    print("Hello! What size dog would you like?")
    response = input("tiny/small/medium/large: ")
    if response == "tiny":
        for i in range(len(min_weight)):
            if min_weight[i] <= 10:
                filtered.append(dog_name[i])
                print(filtered)
                filtered.clear()
    if response == "small":
        for i in range(len(min_weight)):
            if min_weight[i] >= 11 and min_weight[i] <= 25:
                filtered.append(dog_name[i])
                print(filtered)
                filtered.clear()
    if response == "medium":
        for i in range(len(min_weight)):
            if min_weight[i] >= 26 and min_weight[i] <= 60:
                filtered.append(dog_name[i])
                print(filtered)
                filtered.clear()
    if response == "large":
        for i in range(len(min_weight)):
            if min_weight[i] > 60:
                filtered.append(dog_name[i])
                print(filtered)
                filtered.clear()

#GOAL 3
def dog_image_finder():
    print("Hello! What dog breed would you like to research?")
    response_2 = input("Dog name: ")
    if response_2 in dog_name:
        dog_index = dog_name.index(response_2)
        webbrowser.open(dog_image[dog_index])
        print(dog_temperament[dog_index])

#GOAL 4
def BredFor(purpose):
    x = bred_for.index(purpose)
    if purpose in bred_for:
        print(bred_for[x])
        i=0
        for item in bred_for:
            if purpose in item.lower():
                dog_name.append(name[i])
        i = i+1
        print("Some other options include: ", dog_name)


#GOAL 5
def MainMenu():
    print("Hello! What would you like to do?")
    choice = "search"
    while choice != "quit":
        choice = input("Search for a dog or find a match?")
        if choice == "search for a dog":
            dog_breed = input("What dog are you looking for?")
            dog_image_finder(dog_breed)
        if choice == "find a match":
            choice2 = input("Search based on weight or purpose?")
            size = input("What is your desired weight?")
            dog_finder(size)
        if choice2 == "purpose":
            purpose = input("What do you want a dog for?")
            BredFor(purpose)


#main
BredFor()




#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
