from areaCircle_module import calcArea


def main():
    print("This program calculates the area of circle.")
    radius = float(input("Enter the radius of circle: "))
    area = calcArea(radius)
    print(f"Area of circle is: {area:.2f}")


main()
