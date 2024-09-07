import random
#random_number=random.randint(1 ,10)
#print(random_number)

#random_number_0_to_1=random.random()*10
#print(random_number_0_to_1)

#random_float=random.uniform(1,10)
#print(random_float)

#random_heads_tails=random.randint(1,2)
#if random_heads_tails==1:
#    print("Heads")
#else:
#    print("Tails")

#name_list= ["wasim","Salim", "Mahoud","Eva","Abdalrahman"]
#print(random.choice(name_list))
list=["Rock","paper","scissors"]
you_choices=input("please enter you choices Rock,paper or scissors ")
random_choices=random.choice(list)
print("the coputer random choices ",random_choices)
print("Your choices is ", you_choices)
if you_choices!="Rock" and  you_choices!="paper" and  you_choices !="scissors" :
    print("your choices is rang")

elif you_choices==random_choices:
    print("No one win is game you have the same choices")
elif you_choices=="scissors"  and random_choices =="paper" :
    print("You win the game ")
elif you_choices=="Rock"  and random_choices =="scissors":
    print("You win the game ")
elif you_choices=="paper" and random_choices=="Rock":
    print("You win the game ")
else:
    print("you lose")



