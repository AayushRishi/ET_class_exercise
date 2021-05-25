from math import pi


def main():
    print("This program calculates the area of circle.")
    radius = float(input("Enter the radius of circle: "))
    calcArea(radius)


def calcArea(radius):
    area = pi * (radius * radius)
    print(f"Area of circle is: {area:.2f}")


main()
