mymap = {}
# also called dict

mymap['dhruv'] = 19
mymap['rushi'] = 69
print(mymap)

print(len(mymap))

# we can modify the value of any key
mymap['rushi'] = 420
print(mymap['rushi'])

print('dhruv' in mymap)

# removing element from mymap
mymap.pop('rushi')
print(mymap)

# can be created with pairs l
mymap = {'kc' : 22, 'ayush' : 21}
print(mymap)


# dict comprehension
mymap = {i: 2*i for i in range(3)}
print(mymap)


# looping through maps
for key in mymap:
    print(key, mymap[key])

for val in mymap.values():
    print(val)

for key,val in mymap.items():
    print(key,val)


