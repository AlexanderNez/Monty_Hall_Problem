import random

def Monty_Hall():
    doors = ["goat", "goat", "Car"] 
    random.shuffle(doors) # Shuffle wil randomize the list of "doors"
    
    choice = random.choice(doors)
       
    