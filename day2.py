# weight=84
# height=1.6
'''
bmi=weight/height ** 2
print(bmi)
print(round(bmi,2))
print(int(bmi))
'''
##########
'''
score=0
height=1.0
is_wining=True
print(f"the score are = {score},the height is  ={height},the is winning {is_wining}")
'''
print("Welcome to the tip calculator")
total_bil = int(input(print("what was the total bill  $")))
tips = int(input(print("How much tip would you like to give ? 10 , 12 or 15 ?")))
number_people = int(input(print("how many people to split the bill ?")))
cal_tips = (total_bil * tips / 100) + total_bil
pay_each = round(cal_tips / number_people)
print("Each person should pay  :", pay_each)
