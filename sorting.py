arr = ["dhruv","ayush", "darshan", "rushi", "samrat"]
arr.sort()
print(arr)

# custom sort

arr.sort(key = lambda x: len(x))
print(arr)

