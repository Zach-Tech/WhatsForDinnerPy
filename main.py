import random


def user_answer(param):
    pass


while user_answer != 0:
    foodList = ["Steak",
                "Lasagna",
                "Meatloaf",
                "Turkey", 
                "Shepherds Pie",
                "Mcdonalds",
                "Chickfila",
                "Wendy's",
                "Arby's",
                "Dairy Queen",
                "Burger King",
                "Pizza"]
    print("We're gonna eat: ", random.choice(foodList))
    user_answer(input("Would you like to stop? Enter '0': "))
    if input == '0'.format():
        exit(0)
    else:
        continue
