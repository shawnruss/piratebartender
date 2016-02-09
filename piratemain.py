questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",}

def GetDrinkStyle(): 
   """determine the style of drink the customer likes """
   styleResponses = {}
   for drinkstylequestions in questions:
      styleResponses[drinkstylequestions] = input(questions[drinkstylequestions] ) in ("y", "yes")

   return styleResponses
   
print(GetDrinkStyle())