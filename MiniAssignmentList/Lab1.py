scoreList=[34,56,78,97,66,87,56,78,97]

print("Score",scoreList)

# 1. Remove the duplicate
uniqueList=list(set(scoreList))
print("Unique List :: ",uniqueList)


# 2 . Short this in to descending Order
uniqueList.sort(reverse=True)
print("Descending Order :: ",uniqueList)

# 3 . Short this in to Accending Order
uniqueList.sort(reverse=False)
print("Accesnding Order :: ",uniqueList)

# 4. Average of all the score
avg=sum(uniqueList)/len(uniqueList)
print("Average :: ",avg)

# 5. Count the number of score which is more than 70

count=0
for a in uniqueList:
    if(a>70):
        count=count+1
print("Count of the number  which is more than 70:: ",count)