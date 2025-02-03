class AquaFlow:
    def __init__(self, length, width, depth):
        self.length = length
        self.width = width
        self.depth = depth

    def Calculate_area(self):
        print("Calculating Area")
        return self.length * self.width

    def Calculate_volume(self):
        print("Calculating Volume")
        return self.length * self.width * self.depth

    def display(self):
        print("Area:", self.Calculate_area())
        print("Volume:", self.Calculate_volume())


# input values
length = float(input("Enter length: "))
width = float(input("Enter width: "))
depth = float(input("Enter depth: "))

# making tuple of input
volume = (length, width, depth)

# passing tuple to class instance
irrigation = AquaFlow(*volume)
irrigation.display()
print("Irrigation Starts...")
