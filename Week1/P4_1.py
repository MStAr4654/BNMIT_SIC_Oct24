#Find the biggest and smallest numbers among the numbers given by the user
#Something about the list

input_size = int(input("Enter the size of the array: "))

num = []
for i in range(input_size):
    number = int(input("Enter a number "))
    num.append(number)
    #another way -> num.append(int(input()))

print("The array is: ",num)

#print(f'The array of size {input_size} is:')
for nums in num:
    print(nums,end=' ')