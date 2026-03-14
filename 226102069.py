
# a).
scores = [78, 85, 62, 90, 55, 88, 73] 

HighestScore = max(scores)
print("Highest Score: ", HighestScore)

LowestScore = max(scores)
print("Lowest Score: ",LowestScore)

AverageScore = round(sum(scores)/len(scores),2)
print("Average Score: ",AverageScore)

# b).
greater75 = [s for s in scores if s>= 75 ]
print(greater75)

sorted75 = sorted(greater75)
print(sorted75)

# c).
tup75 = tuple(sorted75)
print(tup75)
