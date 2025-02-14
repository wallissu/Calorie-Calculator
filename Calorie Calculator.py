print("#######################################")
print("############## Welcome ################")
print("#######################################")
print()

def calculate_metabolism(weight, height, age):
    return 66 + (13.8 * weight) + (5 * height) - (6.8 * age)

def display_calories(metabolism, goal):
    adjustment = 300 if goal == 1 else -300 if goal == 2 else 0
    print(f"For your goal, your estimated daily calories are: {int(metabolism + adjustment)} Kcal\n")

def calorie_division(metabolism):
    print("Recommended calorie division:")
    print(f"{int(metabolism * 0.37 // 4)}g Protein")
    print(f"{int(metabolism * 0.28 // 4)}g Carbs")
    print(f"{int(metabolism * 0.35 // 9)}g Fat\n")


goal = int(input("What is your goal?\n1 - Weight Gain\n2 - Weight Loss\n3 - Weight Maintenance\n: "))
weight = int(input("Weight (kg): "))
height = int(input("Height (cm): "))
age = int(input("Age: "))

metabolism = calculate_metabolism(weight, height, age)
display_calories(metabolism, goal)
    
if int(input("Would you like a calorie division?:\n1-Yes\n0-No\n:")):
    print()
    calorie_division(metabolism)
else:
    print("Thank you, see you later")

