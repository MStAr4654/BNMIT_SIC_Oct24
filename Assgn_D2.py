#Check if the year is a leap year
#Check if the num is a composite number
num = str(input("Enter a number to find your lucky digit: "))
sum=0
#print(type(num))
#for i in range(-1,-(len(num)),-1):
#    sum+=int(num[i])
while len(num)!=1:
  sum=0
  for i in num:
    sum+=int(i)
  num = str(sum)
print("Your lucky digit = ",sum)