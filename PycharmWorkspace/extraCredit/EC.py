# 1. goes up 6 "*" then down
# 2. counts down from 9- 1

def q1():
    for a in range(7):
        for b in range(a):
            print("*", end=' ')  # body
        print()

    for c in range(5, 0, -1):
        for d in range(c):
            print("*", end=' ')  # body
        print()
    print()


def q2():
    for c in range(9, 0, -1):
        for d in range(c):
            print(c, end='')
        print()
    print()


q1()
q2()
