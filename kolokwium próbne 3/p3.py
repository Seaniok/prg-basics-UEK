def f(d):
    average = 0
    count = 0
    
    people_count = list(d.values())
    total_people = sum(people_count)
    average = total_people / len(people_count)

    for people in people_count:
        if people > average:
            count += 1
    return count

print(f({"LO231":150,"BA787":120,"NZ15":30}))
