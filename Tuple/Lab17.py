#-6,-5,-4,-3,-2,-1 # -Ve Index
# A  B  C  D  E  F
# 0, 1, 2, 3, 4, 5 # +Ve Index
# Slice
# [X:Y]
# Here X= First/Start Index, Which return First element of a list
# Here Y= Last/End Index, which return [Y-1]th Value
# Where , X<=Y
myList=("A","B","C","D","E","F")
print(myList[-1:-3]) # []
print(myList[-5:-3]) # ['B', 'C']
print(myList[-6:-1]) # ['A', 'B', 'C', 'D', 'E']
print(myList[-0:-0]) # [] , There is nothing called -0
print(myList[-6:-100]) # []










