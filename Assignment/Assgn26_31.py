#============================================================================
"""
26.
Find sum of the series:
n + n2 + n3 + upto 10 terms
"""

n = int(input("Enter the starting number: "))
sum = 0
for i in range( n , n + 11 ): sum += i
print("Sum of Series: ", sum)
print("\n")

#============================================================================

"""
27.
Find sum of the series:
1 - n + n2 - n3 + upto M terms
"""

m,n = int(input("Enter the number of terms")),int(input("Enter the starting number: "))
sum = 1
for i in range(2 , m + 1 ):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print("Sum of series: ", sum)
print("\n")

#============================================================================

"""
28.
Find sum of the series:
1 - n/3 + n2/5 - n4/7 + n8/9 ....
(1<n<5 and 1<m<10)
"""

m,n = int(input("Enter the number of terms (<10)")),int(input("Enter the starting number: (<5)"))
sum = 1

for i in range(2 , m + 1 ):
    if i % 2 == 0:
        sum -= i/(2*i-1)
    else:
        sum += i/(2*i-1)
print("Sum of series: ",sum)
print("\n")


#============================================================================

"""
29.
Print the Nth Prime number
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter the nth Prime Number you wish to see: "))
cnt,pri = 0,0
for i in range(1,1000):
    res = is_prime(i)
    if res==True:
        pri=i
        cnt += 1
    if cnt == n:
        break
print("nth Prime Number: ",pri)
        

#============================================================================

"""
30.
Check if the sum of Prime digits in a number is a Prime number
"""

prim_str = str(pri)
for j in prim_str:
    if is_prime(int(j)) == True:
        sum+=int(j)
if is_prime(sum) == True: print("The sum is a Prime Number")
else: print("The sum isn't a Prime Number")
print("\n")


#============================================================================

"""
31.
Print Nth term of the following series:
1 2 2 3 3 5 5 7 8 11 13 13
"""

series_ls = "1 2 2 3 3 5 5 7 8 11 13 13".split()
n_term = int(input("Enter the nth term you want to print: "))
print(series_ls[n_term-1])

