arr = [1,3,4]

print(arr)
#dynamic array
# elements can be pushed
arr.append(3)
arr.append(69)
print(arr)

# poping elements
arr.pop()
print(arr)

# inserting element at position
arr.insert(1,4)
print(arr)
# o(n) complexity

# changing value at index
arr[0] = -2
print(arr)

# initialize arr of size n with default value of 1
n = 5 
arr = [1] * n 
print(arr)

# -1 index is not out of bounds
arr = [1,5,3]
print(arr[-1])

# sublists aka slicing
# last index is non inclusive
arr = [1,5,3,7,34,7]
print(arr[1:3])

# unpacking 
a, b, c = [1,3,67]
print(a,b,c)

# looping through lists
# using index
for i in range(len(arr)):
    print(arr[i])

# without using index
for i in arr:
    print(i)

# with index and value
for i,val in enumerate(nums):
    print(i,n)

# loops through multiple lists
arr1 = [1,3,5]
arr2 = [2,4,6]
for n1,n2 in zip(arr1,arr2):
    print(n1,n2)
