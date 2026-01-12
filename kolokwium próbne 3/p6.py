class C:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        if age < 18:
            fn = first_name[0].lower()
            ln = last_name[0].lower() 
        else:
            fn = first_name[0].upper() 
            ln = last_name[0].upper() 

        self.imie = fn + ln + str(age)

    def __str__(self):
        return self.imie


print(C("John", "May", 21))
print(C("Anna", "Brown", 17))


        
