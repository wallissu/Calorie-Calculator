import Functions
from Variables import *

macro = int(input("Would you like a calorie division?:\n1.Yes\n0.No\n:"))
print()

if goal == 1:
    Functions.Bulking()

elif goal == 2:
    Functions.Cutting()

else:
    Functions.Maintenance()

if macro == True:
    print("I would recommend your calorie division in:\n",
    int(metabolism*0.37//4),"grams of Protein\n", int(metabolism*0.28//4),"grams of Carbohydrate and\n", int(metabolism*0.35//9),"grams of Fat")

else:
    print("Thank you, see you later")