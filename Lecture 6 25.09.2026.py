# 

N=int(input("Enter the number:"))
flag=False

if N==1:
    print("Not a prime number")
elif N==2:
    print("Prime number")
else:
    for i in range(2,N):
        if N%i==0:
            flag=True
            break
        else:
            flag=False
    if flag==False:
        print("Prime number")
    else:
        print("Not a prime number")
        