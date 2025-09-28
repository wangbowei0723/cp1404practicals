"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


import random

def main():
    score = get_score()
    print_result(score)

    random_score = random.randint(0, 100)
    print(f"random score is {random_score}")
    print_result(random_score)

def print_result(score):
    if score < 0 or score > 100:
        print("Invalid score")

    elif score > 90:
        print("excellent")

    elif score >= 50:
        print("Passable")

    else:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score

main()