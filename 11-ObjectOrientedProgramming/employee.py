class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        
    def __str__(self):
        self.convert = self.surname + self.name[0] + str(self.seniority)
        
        if self.age >= 18:
            return self.convert.upper()
        else:
            return self.convert.lower()
            
def main():
   name1 = C('Anna', 'May', 17, 7)
   name2 = C('George', 'Brown', 21, 4)
   
   print(name1)
   print(name2)
   
if __name__ == '__main__':
    main() 