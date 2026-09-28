# to extract last digit: i will use %10
N=235
print(N%10)

# to remove the last from: integer division
N=123
print(N//10)

# print the digits of number 459 in reverse order
# print 9 5 4

# take input from user
# to extract last digit 
# to remove the last from N

#N=int(input("Enter a value in positive integer :"))
#while N>0:
#    print(N%10,end=" ")
#    N=N//10


# print sum of digit of N. N>0
# N = 6531
# 6+5+3+1 = 15. print (15)

# input from user
# while N>0

#N=int(input("Enter the number in positive integer"))
#ans=0
#while N>0:
#    ans+=N%10
#    N//=10
#print(ans)



# add a giver digit to the back of a given number N
# N > 0
# 0  <= D <= 9

#N=int(input("Enter positive integer :"))
#D=int(input("Enter value greater than 0 less than 10 :"))

#N=N*10+D
#print(N)


N=-443
if N<0:
    copy=N*-1  # hack for negative number
else:
    copy=N
rev=0
while copy>0:
    d=copy%10 # last digit
    rev=rev*10+d   # append the last digit
    copy=copy//10

if N<0:
    rev=rev*-1
print(rev)

    
