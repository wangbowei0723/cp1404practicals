import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN, MAX)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{n:2}" for n in quick_pick))


main()
