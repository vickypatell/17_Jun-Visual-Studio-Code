#DATE 25.08.2026

for i in range(10):
    if i==5:
        break
    print(i)

for i in range(10):
    if i==5:
        continue
    print(i)

# Good programming practice: if you dont use
# variable in for loop the replace it with _

for _ in range(3):
    print("vicky")
    
# pass

    #it is not tp be uesrd in competitive
    # programming or interviews
    # it is usually used in testing
    # the pass dose nothing
    # it signifies that the programmer
    # will later add some code to it
    # right noe ignore this block

for i in range(5):
    if i%2==0:
        pass
    print("other statement")

for i in range(0,10):
    if i%3==0:
        continue
    print(i,end=" ")
print()

for i in range(1,10):
    if i%3==0:
        break
    print(i,end=" ")
print()
# nested loops
# * * * *
# * * * *

for _ in range(2):
    for _ in range(4):
        print("*",end=" ")
    print()
    
# @ @ @
# @ @ @ 

for _ in range(2):
    for _ in range(4):
        print("@",end=" ")
    print()
    