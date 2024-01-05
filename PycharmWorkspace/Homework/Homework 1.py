"""
This is Kush From the past if you're reading this you are doing the right thing,
all you need to do is run this python file and all the answers will be in the run console.
"""


# Problem 1 code
def main():
    First = input("Whats your first name?: ")
    Last = input("Whats your last name?: ")
    numMonth = input("What number is your birth month?: ")
    day = input("What number day?: ")
    year = input("What year?: ")

    monthName = ["January ", "February ", "March ", "April ", "May ", "June ", "July ", "August ", "September ",
                 "October ", "November ", "December "]
    month = monthName[int(numMonth) - 1]
    """
    willa sk questions to be answer as is 
    will convert number month to month Name as is 
    final, will print first last name and DOB 
    """
    print("\n" + First, Last, "was born on", month, day, ",", year, ".")


print("         Problem 1.")

main()

# Problem 2 code
print("\n\n     Problem 2.Multiple Choice (2 pts each)\n")

print("i. What is the output for: 'search'.find('a'): ")
print('search'.find('a'))
print("ANSWER b.2")

print("\n\n")

# 2
print("ii. What is the output for:"
      "\n               a = 12"
      "\n               b = a//4"
      "\n               c = b + a % 4"
      "\n               print(c) ")
a = 12
b = a // 4
c = b + a % 4
print("ANSWER   d.3")

print("\n\n")

# 3
print("iii. Which operation on an int will result in a float output?"
      "\n ANSWER d. %")

print("\n\n")

# 4
print("iv. It is World War 3, we captured an enemy message,"
      "\n  it read: “Vo uv! Fvb dlyl uva zbwwvzlk av zll aopz”."
      "\n  We thought long and hard about what they meant."
      "\n  Then we realized – this looks like Caesar cipher!"
      "\n  What value was the original message incremented by?"
      "\n\n  ANSWER c. 7 \n")

print(" Vo uv! Fvb dlyl uva zbwwvzlk av zll aopz = Oh no! You were not supposed to see this ")
