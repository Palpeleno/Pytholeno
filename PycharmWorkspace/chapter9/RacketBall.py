from random import random
from random import randrange


teamA = "Bronze"
teamB = "Silver"

pointA = randrange(1,11)
pointB = randrange(1,11)

if pointA > pointB:
    print(teamA ,"won with",pointA, "points\nTeam" ,teamB ,"lost with",pointB, " points")
else:
    print(teamB ,"won with" ,pointB, "points\nTeam" , teamA , "lost with" ,pointA, " points")
