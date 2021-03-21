"""
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'
"""
count = 0
for char in s:
  if (char == 'a' or char == 'e' or char == 'i' or char == 'i' or char == 'o' or char == 'u'):
    count +=1
print(count) 