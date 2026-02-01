numbers = []

while True:
user_input = input("Enter a number(press enter to quit: "))
if user_input == "":
    break

numbers.append(int(user_input))
numbers.sort(revers=True)

print("five greatest numbers:")
print(numbers[:5])
