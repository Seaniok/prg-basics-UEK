class C:
    def __init__(self, counter):
        self.counter = counter
        
    def m1(self):
        return self.counter
    
    def m2(self):
        self.counter += 1
    
    def m3(self):
        self.counter -= 1
    
    def m4(self, num):
        self.counter += num
    
    def __str__(self):
        return str(self.counter)
    
def main():
    
    c = C(5)
    print(c.m1())      # returns 5
    c.m2()
    print(c.m1())      # returns 6
    c.m4(-8)
    print(c.m1())      # returns -2
    c.m3()
    print(c.m1())      # returns -3
    c.m4(10)
    print(c.m1())      # returns 7
    print(str(c))      # returns "7"
    
    
    
if __name__ == '__main__':
    main()