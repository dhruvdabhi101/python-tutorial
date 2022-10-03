class MyClass:
    # constructor
    def __init__(self,nums):
# self is like this keyword from other languages
        self.nums = nums
        self.size = len(nums)

    #self keyword required as parameter
    def getlenght(self):
        return self.size
    
    def getbiggerlength(self):
        return self.size+12


myc = MyClass([1,256,2,4,5,])
print(myc.getlenght())
print(myc.getbiggerlength())
