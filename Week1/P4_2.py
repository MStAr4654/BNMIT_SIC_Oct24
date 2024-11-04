import sys
print("User given numbers are: ",sys.argv)

num = []

for i in range(1,len(sys.argv)):
    num.append(int(sys.argv[i]))
print(f'User given numbers: {num}')
        