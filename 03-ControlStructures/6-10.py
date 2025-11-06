# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

dog_age = int(input("Enter the dog's age in human years: "))
first_two_years = 2 * 10.5
if dog_age <= 2:
    dog_age = first_two_years
    print(f"The dog's age in dog's years is {first_two_years}")
elif dog_age > 2:
    dog_age = ((dog_age-2) * 4) + first_two_years
    print(f"The dog's age in dog's years is {dog_age}")

