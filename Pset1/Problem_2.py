"""
prints the number of times the string 'bob' occurs in s
"""
count = 0
for char in range(len(s)):
  if (s[char:char+3] == 'bob'):
    count +=1
print("Number of times bob occurs is: {}".format(count))    