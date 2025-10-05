# Q1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Q2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Q3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)

# Q4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)