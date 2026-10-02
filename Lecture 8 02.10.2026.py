##########  Naming Convention  ################

### function Example  ####

'''
def area_of_circle():
    print(3.14*5*5)

area_of_circle()
'''
#print(area_of_circle()+10) area_of_circle

### return statement ###
# >Above is how we define a function ans call it. now we want to add 1 to 2 to it. cant we take it to a variable?
# >This is what return statement is used for. it is like a black box where you want some task to be done. but after the taskis done you want it to return some value as well.

# def abc():
#     return 5

# print(abc())
# a=abc()
# print(a)


# def area_of_circle():
#     return 3.14*5*5

# print(area_of_circle())
# print(area_of_circle()+20)

## note: functions execution ends at return. once a return statement is found rest of line of the code will not be executed. it is just like a beack in loop.
# . If you do return without any value, it will return Now.

def abc():
    print("Hello")
    return
    print("World")
    return "top"
print(abc())


def even_odd():
    a=20
    if a%2==0:
        return "Even"
    else:
        return "Odd"
print(even_odd())

################### PARAMETER AND ARGUMENT IN FUNCTION  ########################

def area_of_circle_5():
    return 3.14*5*5
print(area_of_circle_5())


def area_of_circle_20():
    return 3.14*20*20
print(area_of_circle_20())


def area_of_circle(radius):
    return 3.14*radius*radius
print(area_of_circle(41))

def sum (a,b):
    return a+b
print(sum(5,10))

def sum (a,b):
    return a+b
def sum (a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def calulate_salary(base_monthly_salary,bonus,equity):
    yearly_base=mul(base_monthly_salary,12)
    yearly_bonus=sum(yearly_base,bonus)
    yearly_salary=sum(yearly_bonus,equity)
    return yearly_salary

a=calulate_salary(15000,10000,30000)
print(a)