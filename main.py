import math


def greet():
    print('hello')


def printMe(str):
    print(str)
    return


def calSquare(n):
    res = n * n
    print(" The square (', n, ') = ", res)


num = int(input("Enter a number: "))
calSquare(num)


def calSquare1(n):
    res = n * n
    return res


def calSum(num1, num2):
    return num1 + num2


def calSubtract(num1, num2):
    return num1 - num2


def caldivision(num1, num2):
    return (num1 + num2) / 2


def calMultiply(num1, num2):
    return num1 * num2


a = int(input("give a num"))
b = int(input("give a num"))
while True:
    print('1. For Sum of the values ')
    print('2. For devision of the values ')
    print('3. For multiplication of the values ')
    print('4. For subtraction ')
    print('5. Thank you  great service ')
    choice = input("\n enter your choice or 5 to stop")
    if choice == '1':
        print('um of the values ', calSum(a, b))
    elif choice == '2':
        print('Division  of the values ', caldivision(a, b))
    elif choice == '3':
        print('Multiplication of the values ', calMultiply(a, b))
    elif choice == '4':
        print('Subtractions of the values ', calSubtract(a, b))
    elif choice == '5':
        break
    else:
        print('invalid choice')

num1 = int(input('Enter a number '))
print(' the square of (', num1, ')= ', calSquare1(num1))

greet()
printMe("What a beautiful rainy day")
print(' Test: ', round(1.34, 1))

def add(a, b):
    total = a + b
    print('Total = ', total)


total = 0


def add(a, b):
    total = a + b
    print('Inside add Total = ', total)


add(4, 9)
print('Main Block Total = ', total)


def calculateTotal(amount, discountPercentage=0):
    dicountAmount = discountPercentage / 100 * amount
    return amount - dicountAmount

amount = 500
totalBill = calculateTotal(amount, 10)
print(totalBill)

amount = 500
totalBill = calculateTotal(amount)
print(totalBill)