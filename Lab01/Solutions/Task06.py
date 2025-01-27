def Calculate_Area(length, width):
    return length * width


def Calculate_Volume(length, width, height):
    return length * width * height


def main():
    length = float(input("\nEnter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room: "))

    area = Calculate_Area(length, width)
    volume = Calculate_Volume(length, width, height)

    print(f"Area of the room: {area} square units")
    print(f"Volume of the room: {volume} cubic units")

    print("Cleaning Starts...")


if __name__ == "__main__":
    main()
