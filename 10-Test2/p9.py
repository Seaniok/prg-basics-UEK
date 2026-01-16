import csv

def f(value):
    
    with open('data.csv', 'r', encoding = 'utf-8', newline = '') as file:
        reader = csv.DictReader(file)
        
        count = 0
        
        for row in reader:
            try:
                salary_str = row['salary']
                
                salary = float(salary_str)
                
                if salary >= value:
                    count += 1
            except ValueError:
                continue
            except KeyError:
                print("Error: Column 'salary' not found in CSV.")
                break
    return count


        
    