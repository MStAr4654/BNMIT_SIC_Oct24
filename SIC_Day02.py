"""
i=-1
i-=-1
print(i)
"""
#------------------------------------------------------------------------------------------------------------
"""
import random 

player_num = int(input("Enter a number of your choice bwteen 0 to 9:"))

system_num = int(random.randint(0,10)) #random.seed() --> Starting from the number given in the argument
print(player_num,system_num)

if player_num == system_num: #If I put it as != , then I'll have 90% chance of winning
    print("You are a Billionaire")
else:
    print("You are Roadpati")
"""
#------------------------------------------------------------------------------------------------------------
"""
#Generate a multiples table until 20
n = int(input("Enter a number to find it's multiples till 20: "))
for i in range(1,21):
    print(n,"x",i,"=",n*i) #print("%2d * %02d = %03d" %(n,i,n*i))
"""
#------------------------------------------------------------------------------------------------------------
#A16
num = input("Enter a number to find your lucky digit: ");sum=0
print(type(num))
for i in range(-1,(len(num))):
    print(num[i])
