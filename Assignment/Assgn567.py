"""
5. Check if the year is Leap year
6. Check if the input digit is Composite number
7. Check if the character is only a alpha-numeric
"""
#============================================================================

#5. Check if the year is Leap year

yr = int(input("Enter a year: "))
if(yr % 4 == 0 or (yr % 100 == 0 and yr % 400 == 0)):
    print("It is a leap year\n")
else:
    print("It is not a leap year\n")
print("\n")

#============================================================================

#6. Check if the input digit is Composite number

n = int(input("Enter a number: ")) ; cnt = 0
for i in range(1,n + 1):
    if i % n == 0:
        cnt += 1

print("It is a composite number\n" if cnt != 2 else "It is not a Composite Number\n")
print("\n")

#============================================================================

#7. Check if the character is only a alpha-numeric

chr = input("Enter a character: ")

print("It is only an alpha-numeric\n" if chr.isalnum() else "It is not only an alpha-numeric\n")
print("\n")