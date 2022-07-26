# THIS PROGRAM EXPLAINS SOME OF THE ARITHMETIC OPERATIONE

print("1)add two numbers")  # add two numbers
def sum(num1, num2):
    return num1 + num2
print("enter two numbers \n")
num1 = input()
num2 = input()
res1 = int(num1) + int(num2)
print("THE SUM OF TWO NUMBERS IS " + str(res1))


print("2)subtract two numbers")  # subtract two numbers
def sub(num3, num4):
    return num3 - num4
print("enter two numbers \n")
num3 = input()
num4 = input()
res2 = int(num3) - int(num4)
print("THE SUB OF TWO NUMBERS IS " + str(res2))

print("3)multiply two numbers")  # multiply two numbers


def multi(num5, num6):
    return num5 * num6


print("enter two numbers \n")
num5 = input()
num6 = input()
res3 = int(num5) * int(num6)
print("THE PRODUCT OF TWO NUMBERS IS " + str(res3))

print("4)divide two numbers")  # divide two numbers


def div(num7, num8):
    return num7 / num8


print("enter two numbers \n")
num7 = input()
num8 = input()
res4 = int(num7) / int(num8)
print("THE DIVISION OF TWO NUMBERS IS " + str(res4))

# the absolute value of a number
print("5)to calculate the absolute value of number")
print("enter number")
num=input()
print("the absolute value of a number is "+str (abs(int(num))).upper())

print("6)to raise the number to any power ")
print("enter number \n")
num=input()
print("enter power")
num1=input()
print("the result is "+str(pow(int(num),int(num1))).upper())

print("7)to cubing number")
def cube(num):
    return num * num * num
print("enter number")
num=input()
print("the result is "+str(cube(int(num))))

print("8)to find the remainder f the division")
def mod(a,b):
    return a%b
print("enter to number")
num=input()
num1=input()
print("the result is "+str(mod(int(num),int(num1))))

#to find root