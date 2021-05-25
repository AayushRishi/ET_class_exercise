from name_module import reverse


def main():
    print("This program reverse's the entered name.")
    firstN = input("Enter first name: ")
    lastN = input("Enter last name: ")
    nameStr = firstN + " " + lastN
    rev_nameStr = reverse(nameStr)
    print(f"Correct order is: {nameStr}")
    print(f"Reverse order is: {rev_nameStr}")


main()

