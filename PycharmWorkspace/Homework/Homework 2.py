"""
Write a python program that takes two values as input from user, x and y; then applies
the following equations on x and y and prints the output of the functions.
𝑥 = (1/𝑦) ∗ (5)
𝑦 = (2 − 𝑥) ∗ (1/5)
Please note, you have you utilize functions to solve this problem.
Hint: Make sure to use floating point numbers while calculating.

2. Write a program that prints out the odd numbers from 10 to 20.

3. Suppose, you are taking loan from bank. And the bank charges 10% interest each year. If
you take your loan for 15 years, how much money you have to pay back to bank?
Write a python program to solve the above problem. Take the amount of loan as input
from the user. And use following expression.
𝑙𝑜𝑎𝑛 = 𝑙𝑜𝑎𝑛 ∗ (1 + 𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝑡
"""

print("Kush Darji 002-36-8275 \nHomework 2\n")


def q1():
    print("Question 1")
    x = float(input("What is the first value?"))
    y = float(input("What is the second value?"))

    def equ(x, y):
        print()
        xPrime = ((1 / y) * 5)
        print(xPrime, "=(1/", y, ")*5")

        yPrime = (2 - x) * (1 / 5)
        print(yPrime, "=(2−", x, ")∗(1/5)")

    equ(x, y)


def q2():
    print("Question 2")
    start = 10
    end = 21

    for a in range(start, end):
        if a % 2 != 0:
            print(a)


def q3():
    print("Question 3")
    loan = eval(input("What is the loan amount?:"))
    intrest = eval(input("What is the intrest amount? (enter 10 or your own number)?:"))
    time = eval(input("How many years ?(enter 15 or another amount)?:"))
    rate = intrest / 100

    amount = loan * (1 + (rate * time))
    print("You will have to pay back:", amount)


# q1()
print()
# q2()
print()
q3()
