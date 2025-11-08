import random

print("Welcome to Snake, Water and Gun Game 💖")

choices = ["Snake", "Water", "Gun"]
a = int(input("Enter number of times you want to play: "))

points = 0

for i in range(a):
    b = input("Enter Snake, Water or Gun: ").capitalize()
    c = random.choice(choices)
    print(f"Computer chose: {c}")
    
    if b == c:
        print("It's a tie!")
    elif (b == "Snake" and c == "Water") or \
         (b == "Water" and c == "Gun") or \
         (b == "Gun" and c == "Snake"):
        print("You Win!")
        points += 1
    else:
        print("You Lose!")

print("🎯 Total Points:", points)