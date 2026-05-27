#CREATE Project - Cat Adoption Helper


#initialize
import pandas as pd
import webbrowser
data = pd.read_csv('create.csv')
max_lifespan = data['Maximum Life Span'].tolist() #The maximum lifespan a cat will live
max_weight = data['Maximum Weight'].tolist() #The maximum weight a cat can be
cat_name = data['Name'].tolist() #The name of the cat
cat_temperament = data['Temperament'].tolist() #Traits a cat may have
weight_matches = []
lifespan_matches = []
trait_matches = []
filtered = []




#functions
def research_lifespan(max_lifespan):
    print("What is the maximum number you would want your cat to live?: ")
    reply_2 = input("15-20 years: ").strip()
    target = int(reply_2)
    for i in range(len(max_lifespan)):
        if max_lifespan[i] == target:
            lifespan_matches.append(i)
    print("Information saved.")




def research_traits(cat_temperament):
    print("What traits would you want in your cat?")
    reply_3 = input("Affectionate/Active/Easy Going: ")
#AFFECTIONATE
    if reply_3 == "affectionate":
        print("Interesting! Would you like your cat to be playful?")
        reply_4 = input("Yes/No: ").lower()
        if reply_4 == "yes":
            for i in range(len(cat_temperament)):
                if "Affectionate" in cat_temperament[i] and "Playful" in cat_temperament[i]:
                    trait_matches.append(i)
        elif reply_4 == "no":
            for i in range(len(cat_temperament)):
                if "Affectionate" in cat_temperament[i]:
                    trait_matches.append(i)
#ACTIVE
    if reply_3.lower() == "active":
        print("Interesting! Would you like your cat to be social?")
        reply_5 = input("Yes/No: ").lower()
        if reply_5 == "yes":
            for i in range(len(cat_temperament)):
                if "Active" in cat_temperament[i] and "Social" in cat_temperament[i]:
                    trait_matches.append(i)
        elif reply_5 == "no":
            for i in range(len(cat_temperament)):
                if "Active" in cat_temperament[i]:
                    trait_matches.append(i)
#EASY GOING
    if reply_3 == "easy going":
        print("Would you like your cat to be independent?")
        reply_6 = input("Yes/No: ").lower()
        if reply_6 == "yes":
            for i in range(len(cat_temperament)):
                if "Easy Going" in cat_temperament[i] and "Independent" in cat_temperament[i]:
                    trait_matches.append(i)
        elif reply_6 == "no":
            for i in range(len(cat_temperament)):
                if "Easy Going" in cat_temperament[i]:
                    trait_matches.append(i)
    print("Information saved.")




def research_weight(max_weight):
    print("What is the maximum number you would like your cat to weigh?")
    reply_7 = input("8-25 lbs: ")
    for i in range(len(max_weight)):
        if max_weight[i] == int(reply_7):
            weight_matches.append(i)
    print("Information saved.")




def complete_research():
    print("Hello! I am a website that knows all about cats! Give me a topic to research about!")
    while True:
        choice = input("Type START to begin or QUIT to exit: ").lower().strip()
        if choice == "quit":
            print("Goodbye! Thank you for using my website!")
            break
        elif choice == "start":
            research_lifespan(max_lifespan)
            research_traits(cat_temperament)
            research_weight(max_weight)
            final_matches = set(lifespan_matches) & set(trait_matches) & set(weight_matches) #Finding cats that appear in ALL lists
            print("Here are the cats that match ALL your preferences: ")
            if not final_matches:
                print("No cats match all your criteria.")
            else:
                for i in final_matches:
                    print(cat_name[i])


#main
complete_research()




#SOURCES


#Cat Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source: https://thecatapi.com/



