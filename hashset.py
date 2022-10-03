# hashset

myset = set()
myset.add(1)
myset.add(2)

print(myset)
print(len(myset))

#checking if element is in set or not
print(2 in myset)
print(4 in myset)

# removing value in constant time 
myset.remove(2)
print(2 in myset)

# list to set 
print(set([1,2,3]))

# set comprehension
myset = {i for i in range(5)}
print(myset)



