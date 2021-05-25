def main():
    print("This program reverse's the entered name.")
    firstN = input("Enter first name: ")
    lastN = input("Enter last name: ")
    nameStr = firstN + " " + lastN
    rev_nameStr = reverse(nameStr)
    print(f"Correct order is: {nameStr}")
    print(f"Reverse order is: {rev_nameStr}")


def reverse(strg):
    lis = " "
    for i in range(len(strg)-1, -1, -1):
        lis += strg[i]
    return lis.lstrip()


main()

