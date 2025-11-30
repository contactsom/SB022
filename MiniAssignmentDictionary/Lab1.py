line_text = "Learn and practice and learn to practice"

# 1. Find the frequency of each words
# Learn=2
# practice=2
# and=2

words=line_text.lower().split()
print(words) # ['learn', 'and', 'practice', 'and', 'learn', 'to', 'practice']

frequency={} # Empty Dictionary

for word in words:
    frequency[word]=frequency.get(word,0)+1

print(frequency)

