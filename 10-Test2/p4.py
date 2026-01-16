def f(subjects):
    average = 0
    highest = -1
    best_subj = ''
    subjects = dict(subjects)
    for key,value in subjects.items():
        average += sum(value) / len(value)
        if average > highest:
            highest = average
            best_subj = key
    return best_subj
        
print(f({'math':[3,4,4], 'geo':[5,4,4,4], 'comp':[5,4]}))