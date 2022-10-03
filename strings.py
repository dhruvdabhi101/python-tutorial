# strings are similar to arrays
s = "abc"
print(s[0:2])

# they are immutable
# s[0] = 'a'

# we can update it 
s += 'abd'
print(s)

# strings can be converted to integers
ss = "1232"
print(int(ss) + int(ss))

# integers can be converted to strings
print(str(123)+str(123))

# to get ascii value of a character
print(ord('a'))
print(ord("b"))

# combine list of strings
strings = ["ab","bc","cd"]
print("".join(strings))


