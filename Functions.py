from Variables import *

def Bulking():
    print("For weight gain, your estimated calories are", int(metabolism + 300),"Kcal")
    print()

def Cutting():
    print("For weight loss, your estimated calories are", int(metabolism - 300),"Kcal")
    print()

def Maintenance():
    print("For weight maintain, your estimated calories are", int(metabolism),"Kcal")
    print()