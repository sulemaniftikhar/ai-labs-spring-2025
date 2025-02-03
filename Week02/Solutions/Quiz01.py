def CheckPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


num = int(input("\nEnter a number: "))

if CheckPrime(num):
    print(f"{num} is a PRIME number.")
else:
    print(f"{num} is NOT a prime number.")