import os
data = []
f = open('data/cuisine.txt', 'r')
t = f.read().split('\n##\n')
cuisine = [dish.split('\n#\n') for dish in t]
for dish in cuisine:
	mealName = dish[0]
	material = dish[1].split(' ')
	for m in material:
		data.append(m)
	style = dish[2]
	steps = dish[3].split('\n')
	steps = [step.split('$') for step in steps]
	for step in steps:
		if len(step) == 1:
			step.append(0)
		else:
			step[1] = int(step[1])
f.close()
print(data)
print(len(data))
data = list(set(data))
print(data)
print(len(data))

