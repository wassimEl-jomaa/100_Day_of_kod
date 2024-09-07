import random
studen_list=[120,111,134,154,176,199,189,169,178,156,183,162,188,177,166,122,260]
max=0
temp=0
for max_digre in studen_list:
    if max<max_digre:
        max=max_digre
print(max)

'''
for number in range(1,101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuss")

    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_passord=[]
x=nr_numbers+nr_symbols+nr_letters
nr=0
for letter in range(0,nr_letters):
    random_passord.append(random.choice(letters))
for number in range(1,nr_numbers+1):
    random_passord.append(random.choice(numbers))
for symbol in range(1,nr_symbols + 1):
    random_passord.append(random.choice(symbols))

print(random_passord)

random.shuffle(random_passord)
for rand in range(0,x):
    print(random_passord[rand],end="")





