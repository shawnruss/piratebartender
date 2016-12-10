import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
    }
    
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    
drinkNamePrefixes = ["Fluffy", "Stinking", "Dirty", "Hairy"]
drinkNameSuffixes = ["Bastard", "Sea-Dog", "Mermaid", "Whale"]

def GetDrinkStyle(): 
   """determine the style of drink the customer likes """
   styleResponses = {}
   for drinkstylequestions in questions:
      styleResponses[drinkstylequestions] = input(questions[drinkstylequestions] ) in ("y", "yes")
   return styleResponses
   

def ConstructDrink(drinkStyleResponses):
   """ Build the drink! """
   drinkIngredients = []
   for ingredient in ingredients:
      if drinkStyleResponses[ingredient] == True:
         drinkIngredients.append(random.choice(ingredients[ingredient]))
   return drinkIngredients

def main():
    
    wantToDrink = True
    
    while wantToDrink:
        drinkIngredients = ConstructDrink(GetDrinkStyle())
        print()
        print("ere be yer drink yer dirty landlubber:")
        print()
        for n in range (0, len(drinkIngredients)):
            print("{}".format(drinkIngredients[n]))
        print("\nI call this a {} {}\n".format(random.choice(drinkNamePrefixes), random.choice(drinkNameSuffixes)))

        if input("Does ye want another drink ya greedy mug?") in ("y", "yes"):
            wantToDrink = True
            print()
        else:
            wantToDrink = False
            print("\nBe gone with yer then!\n")


if __name__ == '__main__':
    main()
    
""" test commit """