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

def GetDrinkStyle(): 
   """determine the style of drink the customer likes """
   styleResponses = {}
   for drinkstylequestions in questions:
      styleResponses[drinkstylequestions] = input(questions[drinkstylequestions] ) in ("y", "yes")

   #print(styleResponses)

   return styleResponses
   

def ConstructDrink(drinkStyleResponses):
   """ Build the drink! """
   
   drinkIngredients = []

   for ingredient in ingredients:
      if drinkStyleResponses[ingredient] == True:
         #get a random ingredient that has the same key
         #print(random.choice(ingredients[ingredient]))
         drinkIngredients.append(random.choice(ingredients[ingredient]))
         
   return drinkIngredients

#print(ConstructDrink(GetDrinkStyle()))

if __name__ == '__main__':
    drinkIngredients = ConstructDrink(GetDrinkStyle())
    
    print()
    print("ere be yer drink yer dirty landlubber:")
    print()
    for n in range (0, len(drinkIngredients)):
        print(drinkIngredients[n])
        
    print()