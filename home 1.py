print(2==2)
print(2==3)

print(2==2.002)

print(2=="2")
print(1==None)

print(2!="2")

#logical operators
age=25
print(age>18 and age<60)

## conditional Statement
m_comp=-110
m_culture='positive'
m_distance=30
if m_comp>80:
    print('microsoft criteria filled')
elif m_comp>80:
    print('google criteria filled')
else:
    print('sad life')
    

#nested
m_comp=-110
m_culture='positive'
m_distance=300

g_comp=110
g_culture='positive'
g_distance=3000
if m_comp>80 and m_comp>80:
    if m_distance>g_distance:
        print("go to microsoft")
    
    


# Double click to edit

light=input("Enter Value")
if light=="green":
    print("go")
elif light=="yellow":
    print("wait")
elif light=="red":
    print("stop")
else:
    print("invalid input")


print(10,12,14,15, sep='\n')
