rows = int(input("\nEnter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)
