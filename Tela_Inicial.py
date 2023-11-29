from lib2to3.pgen2.literals import simple_escapes
import Funções
from Variaveis import *

macro = int(input("Would you like a calorie division?:\n1.Yes\n0.No\n:"))
print()

if objetivo == 1:
    Funções.Bulking()

elif objetivo == 2:
    Funções.Cutting()

else:
    Funções.Maintenance()

if macro == True:
    print("I would recommend your calorie division in:\n",
    int(metabolismo*0.37//4),"grams of Protein\n", int(metabolismo*0.28//4),"grams of Carbohydrate and\n", int(metabolismo*0.35//9),"grams of Fat")

else:
    print("Thank you, see you later")
