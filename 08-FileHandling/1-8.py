def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content

file_content = read_from_file('pets.txt')
file_lines = file_content.split()

count = 0
for word in file_lines:
    count = count + 1

print(file_content)
print(count)
    