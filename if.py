import random
drinks = ["beer", "wine", "whiskey", "campari", "tequila", "rum", "gin tonic", "sangria"]
try:
    age = int(input("How old are you?"))
    country = input("Where do you live?")
except ValueError:
    print("I am sorry, but that is not a valid number")
else:
    #Do some sanity checks on age
    if age < 0:
        print("I am sorry, but your age cannot be negative")
    elif age > 130:
        print("I am sorry, but your age cannot be greater than 130")

    elif age < 18:
        print("I am sorry but you are too young to play this drinking game everywhere in the world")
    elif age < 21 and country == "US":
        print("I am sorry but you are too young to play this drinking game in the US")
    else:
        drink = random.choice(drinks)
        print("Drink some",drink,". Thank you for playing, you are", age, "years old so you can play this game in",country)