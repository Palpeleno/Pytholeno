from random import randrange


"""
Simulates 200 rolls of 2 6-sided dice
Records the results of each dice individually
Computes an average roll from the recorded rolls
"""


def dice():
    diceOneSum = 0
    diceTwoSum = 0
    roll = 0

    for roll in range(201):
        diceOne = randrange(1, 6)
        # print(diceOne,"+",end='')

        diceOneSum += diceOne
    # print(diceOneSum)

    for roll in range(201):
        diceTwo = randrange(1, 6)
        # print(diceTwo,"+",end='')

        diceTwoSum += diceTwo
        # print(dicetwoSum)

        dice1Ave = diceOneSum / 200
        dice2Ave = diceTwoSum / 200
    print("\nDice one average: ", round(dice1Ave, 1))
    print("\nDice two average: ", round(dice2Ave, 1))


dice()