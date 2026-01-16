import json

def f(years, course, average_grade):
    
    with open('data.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        
    for student in data:
        if student['age'] >= years:
            
        
            