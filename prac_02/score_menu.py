LOWEST_SCORE = 0
HIGHEST_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    score = LOWEST_SCORE
    choice = ''
    while choice != 'Q':
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice:").upper()

        if choice == 'G':
            score = get_valid_score()

        elif choice == 'P':
            if score == LOWEST_SCORE:
                print("Please get a score first!")
            else:
                print_result(score)

        elif choice == 'S':
            if score == LOWEST_SCORE:
                print("Please get a score first!")
            else:
                show_stars(score)

        elif choice == 'Q':
            print("farewell")

        else:
            print("Error, please enter again")


def get_valid_score():
    score = float(input("enter your score:"))
    while score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("score must be between 0 and 100")
        score = float(input("enter your score:"))
    return score


def print_result(score):
    if score < LOWEST_SCORE or score > HIGHEST_SCORE:
        print("Invalid score")

    elif score > EXCELLENT_SCORE:
        print("excellent")

    elif score >= PASSABLE_SCORE:
        print("Passable")

    else:
        print("Bad")


def show_stars(score):
    stars = ''
    for i in range(int(score)):
        stars += '*'
    print(stars)


main()