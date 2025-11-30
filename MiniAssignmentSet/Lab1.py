scoreSet={34,56,78,97,66,87,56,78,97}
print("Score",scoreSet)

avg= sum(scoreSet)/len(scoreSet)
print("average",avg)

# 2. CAn you write code to find the count where number is grater than 50

count=0
for a in scoreSet:
    if(a>50):
        count+=1
print("Count grater than 50 :: ",count)


#
myString ="Apple book cat apple book Cat"
#word=myString.lower().split()
word=myString.split()
print(word) # ['apple', 'book', 'cat', 'apple', 'book', 'cat']
uniqueSet=set(word)
print(uniqueSet)