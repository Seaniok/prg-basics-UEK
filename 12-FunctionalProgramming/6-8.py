array = [37,51,44,23,78,92,39,84,83,51]

mean1 = list(filter(lambda x: x >= 30, array))
mean2 = list(filter(lambda x: x >= 40, array))
mean3 = list(filter(lambda x: x >= 70, array))

print('Min 70 pts: ', mean3)
print('Min 40 pts: ', mean2)
print('Min 30 pts: ', mean1)