class C:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
        if age < 18:
            self.formated_name = first_name[0].lower() + last_name[0].lower() + str(age)
        else:
            self.formated_name = first_name[0].upper() + last_name[0].upper() + str(age)
            
    def __str__(self):
        return self.formated_name
            
if __name__ == '__main__':
    name1 = C('John', 'May', 18)
    name2 = C('Anna', 'Brown', 17)
    print(name1)
    print(name2)
    