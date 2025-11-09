import csv
from guitar import Guitar


def main():
    """Load from a CSV file and return a list"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

# Regular display
    for guitar in guitars:
        print(guitar)

# Display guitars from oldest to newest
    guitars.sort()
    print("\nSorted by year:")
    for guitar in guitars:
        print(guitar)

    name = input("\nName: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input, enter again.")
        name = input("Name: ")

    print("\nGuitars list:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    guitars.sort()
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()