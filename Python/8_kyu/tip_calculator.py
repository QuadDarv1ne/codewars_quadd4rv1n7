'''
[ Tip Calculator ]

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:
Terrible: tip 0%
Poor: tip 5%
Good: tip 10%
Great: tip 15%
Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT").
If an unrecognised rating is received, then you need to return:

"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, regardless of the service.
'''


import math

def calculate_tip(amount, rating):
    # Define the mapping of ratings to tip percentages
    ratings = {
        'terrible': 0,
        'poor': 0.05,
        'good': 0.10,
        'great': 0.15,
        'excellent': 0.20
    }
    
    # Normalize the rating to lowercase
    rating = rating.lower()
    
    # Check if the rating is valid
    if rating in ratings:
        # Calculate the tip based on the amount and rating
        tip = amount * ratings[rating]
        # Round up the tip
        return math.ceil(tip)
    else:
        # If the rating is not recognized
        return "Rating not recognised"


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
