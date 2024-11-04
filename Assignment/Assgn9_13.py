"""
9. Accept a number and find sum of digits of the number
10.Accept a number and find count the number of digits in it.
11.Accept a number and find biggest/smallest digit in the number
12.Find sum of Even/Odd digits in the number
13.Find the frequency of a digit in the number
"""

#============================================================================

#9. Accept a number and find sum of digits of the number
#10. Accept a number and find count the number of digits in it.

n = input("Enter a number: ");sum = 0

for i in n: sum += int(i)

print("Sum of digits = ",sum)

print("Number of digits: ",len(n))
print("\n")
#============================================================================

#11. Accept a number and find biggest/smallest digit in the number

ls = n.split()

print("Biggest digit: ",max(ls))

print("Smallest digit: ",min(ls))
print("\n")
#============================================================================

#12.1 Sum of Odd digits
sumOdd = 0 
for i in range(0,len(n)+1,2):
    sumOdd += int(n[i])
print("Sum of Odd Digits: ",sumOdd)

#12.2 Sum of Even digits
sumEven = 0
try:
    for i in range(1,len(n)+1,2):
        sumEven += int(n[i])
except IndexError:
    pass

print("Sum of Even Digits: ",sumEven)
print("\n")
#============================================================================

#13.Find the frequency of a digit in the number
dict = {}
cnt = 0
for i in n:
    if i not in dict:
        dict[int(i)] = 1
    else:
        cnt += 1
        dict[int(n)] = cnt
print("Frequency of each digit in the number:\n",dict)
print("\n")