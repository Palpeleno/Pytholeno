fruitNames = []
fruitPrice = []
print("Welcome to fruit vendor!!!")
fruit = input("Enter a fruit name : ")
while not(fruit == "done"):
    fruitNames += [fruit]
    fruit = input("Enter a fruit name (or done): ")

for s in fruitNames:
    price = (input("Enter the price for " + s + ":  "))
    fruitPrice += [price]

totalPrice = 0
print(fruitPrice[0] , fruitPrice[1])
print(fruitPrice[0] + fruitPrice[1])

for i in range (len(fruitNames)):
    quantity = input("What is the quantitiy of...\n" + fruitNames[i] + "($ " + (fruitPrice[i]) + "):")
    alpha = (quantity * fruitPrice[i])

    print(alpha + "=" + quantity + "+" + (fruitPrice[i]))
    totalPrice += alpha
print("Your total purchase is $", totalPrice)

