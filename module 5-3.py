number = int(input("Enter a number"))

if number < 2:
    print(number, "is not a prime number")
else:
    is-prime = True
    for i in range(2,number):
        if number % i == 0:
            is-prime = False
            break
    if is-"prime:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number")