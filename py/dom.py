import random

answer = "y"
while answer == "y":
    print("Can you tell what I am thinking about? (y/n)")
    answer = input("Enter your answer: ")
    if answer == "y":
        num = input("Pick a number. (0,3)")
        print("I am thinking about:")
        for numb in range(int(num)):
            print(random.choice(["python", "food", "chapel", "Moneyy!"]))
    if answer == "n":
        print("Alright! Great to meet you though!")
    answer = input("Try again? (y/n)")