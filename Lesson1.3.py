n = input("Enter an integer: ")

while n < '0':
    print("Humph! Not exactly")
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

