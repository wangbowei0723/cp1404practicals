minimum_length = 7

def main():
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    for i in range(len(password)):
        print("*", end="")

def get_password():
    password = input("enter password:")
    while len(password) < minimum_length:
        print("password must be at least 7 characters")
        password = input("enter password:")
    return password

main()