recorded = [48,47,54,50,42,68,39,46]
func = list(filter(lambda x: x>50, recorded))

print('Recorded values:', *recorded, sep = ',')
print('Speed too high:', *func, sep = ',')