#Corrie's Images

import webbrowser


url = "https://www.burgesspetcare.com/wp-content/uploads/2025/06/All-about-Ragdoll-cats-.jpg" #Ragdoll
url2 = "https://mymodernmet.com/wp/wp-content/uploads/2022/01/kiefer-maine-coon-cat-3.jpeg" #Maine Coon
url3 ="https://www.trupanion.com/images/trupanionwebsitelibraries/bg/bengal-cat.jpg?sfvrsn=fc36dda4_5" #Bengal
url4 = "https://images.squarespace-cdn.com/content/v1/66ec3b49803ab81bf84f89e4/1737488319255-I9Y2KQ7FG8NLIZ15TZS0/Reno-Leopard-2025.jpg" #Leopard

description1 =["Ragdolls are your typical house cat, loving and caring for its owner as you love and care for them."]
description2 =["Main Coons might look intimidating, but  are extremely loving once you get to know them."]
description3 =["Bengals are small, but also very disruptive and mean. Knowing you, you would be the perfect fit to raise one!"]
description4 = ["Leopards are fierce, scary cats that live in desserts, snowy forests, and more. They are perfet for individuals who love a challenge."]

#functions
def cat_game():
    print("Hello! This is The Ultimate Cat Game, where you find the cat that best suits your personality!")
    reply = input("Ready to start/leave game: ")
    if reply == "Ready to start":
        print("Great! to start off, do you love a challenge?")
        reply_2 = input("Yes/No: ")
        if reply_2 == "Yes":
            print("...")
            print("Interesting...would you say you live in an open area with lots os space?")
            reply_3 = input("Yes/No: ")
            if reply_3 == "Yes":
                webbrowser.open(url4)
                print(description4)
            if reply_3 == "No":
                webbrowser.open(url3)
                print(description3)
        if reply_2 == "No":
            print("...")
            print("Perfect! Are you a calm or rowdy individual?")
            reply_4 = input("Calm/Rowdy: ")
            if reply_4 == "Calm":
                webbrowser.open(url)
                print(description1)
            if reply_4 == "Rowdy":
                webbrowser.open(url2)
                print(description2)

#main
cat_game()


#sources of information
#URL 1:
    #Picture of A Small Ragdoll Cat
    #Website Name: Burgess
    #URL: https://www.burgesspetcare.com/blog/cat/all-about-ragdoll-cats/
    #Title: All About Ragdoll Cats
    #Date: June 19th, 2025
#URL 2:
    #Picture of a Large Maine Coon Cat
    #Website Name: My Modern Met
    #URL: https://mymodernmet.com/kefir-maine-coon-cat/
    #Author: Sara Barnes
    # Title: This Giant Maine Coon Cat Is So Big That People Think He’s a Dog
    #Date: August 18th, 2024
#URL 3:
    #Picture of a Small Bengal Cat
    #Website name: Trupanion
    #URL: https://www.trupanion.com/pet-blog/article/bengal
    #Author: Trupanion Staff
    #Title: What is a Bengal Cat? Breed Facts & Care Tips
    #Date: March 22nd, 2024
#URL 4:
    #Picture of a Large Leopard
    #Website Name: Big Cat Rescue
    #URL: https://bigcatrescue.org/conservation-news/leopard-facts
    #Title: Leopard Facts
