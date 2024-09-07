'''
print(" We to the ridcroaster!")
height=int(input("what isyour height in cm?"))
if height>120:
    age=int(input("how old are you ?"))
    if age>=18:
        print("you should pay 12 $")
    else:
        print("you should pay 8$")
    print("you can rid the ridcroaster")
else:
    print("you can not rid the ridcroaster")

'''
'''
print("welcome the chick game ")
number=int(input("please enter the nummber want to chick  ?"))
chick=number%2
if chick == 0:
    print("The number you enter is EVEN")
    
    
else:
    print("THe number you enter is ODD")
'''
'''
weight=int(input("Please the enter your  weight "))
height=float(input("Please enter you height  ?"))
bmi=weight/height ** 2
if bmi<18.5:
    print(" under weight")
elif bmi>25:
    print("normal weight")
else:
    print("overweight")

print(bmi)
print(round(bmi,2))
print(int(bmi))
'''
print("Welcome to python piza deliver")
prise=0
size=input("what size do you want S,M,L")
if size=="s":
    prise +=15
elif size =="m" :
    prise +=20
else:
    prise +=25
extra_cheese=input("do you want extra cheese ")
if extra_cheese =='y':
    prise +=2
extra_pepperoni=input("do you want extra pepperoni ")
if extra_pepperoni =="y":
    prise +=2

print(f"the prise of your pizza are  {prise}")


