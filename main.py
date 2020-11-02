import random

while True:
    food_list = ["Steak",
                 "Lasagna",
                 "Meatloaf",
                 "Turkey",
                 "Shepherds Pie",
                 "McDonalds",
                 "Chickfila",
                 "Wendy's",
                 "Arby's",
                 "Dairy Queen",
                 "Burger King",
                 "Pizza",
                 "Spaghetti",
                 "Sloppy Joe Tacos w/ Tabasco",
                 "Pork-Chops",
                 "Seafood",
                 "Burgers",
                 "Tacos",
                 "Chinese",
                 "Kielbasa",
                 "Crockpot Beef + Peppers",
                 "Crack-chicken",
                 "Crockpot BBQ Chicken",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 "",
                 ""]
    print("We're gonna eat: ", random.choice(food_list))
    user_input = input("\nWould you like to stop?\nEnter 'end': ")
    if user_input.lower() == "end":
        break
    else:
        continue
