'''T=int(input("Enter a single digit :"))
while T>0:
    N=int(input("Enter a digit :"))
    if N<0:
        copy=N*-1
    else:
        copy=N
    rev=0
    while copy>0:
        d=copy%10  # last digit
        rev=rev*10+d
        copy//=10
    if N<0:
        rev=rev*-1
        
    print(rev)
    
    T-=1 '''



for _ in range(7):
    print("#"*9)

for i in range(1,9):
    print("*"*i)

