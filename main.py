import random
while True:
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
    user_input = input("Would you like to stop? Enter 'end': ")
    if user_input.lower() == "end":
        break
    else:
        continue
