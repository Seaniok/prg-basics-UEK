class C:
    def __init__(self, array):
        self.array = array
    
    def m(self, n):
        count = 0
        for point in self.array:
            if point[0] > 0 and point[1] > 0:
                count += 1
                
        return count >= n

def main():
    
    cords = C([[2,3], [1,8], [-6,4], [3,-7]])
    
    print(cords.m(2))
    print(cords.m(3))
    
if __name__ == '__main__':
    main()