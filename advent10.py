import math

def getAsteroids():
	with open("advent10.in") as file:
		for y, line in enumerate(file.readlines()):
			for x, a in enumerate(line):
				if a == "#":
					yield(x, y)

def angle(start, end):
	# get the angle between the two points (asteroids)
	result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi

	# asteroid 2 is below the horizon (X axis) for asteroid 1
	if result < 0:
		result += 360

	return result

def getAstAngles(asteroid, asteroidList):
	result = []

	for a in asteroidList:
		if asteroid != a:
			result.append(angle(asteroid, a))

	return result

def remDupes(lst):
	result = [] 

	for num in lst: 
		if num not in result: 
			result.append(num) 

	return result 

asteroids = list(getAsteroids())
maxCount = 0
baseLoc = None

for a in asteroids:
	count = len(remDupes(getAstAngles(a, asteroids)))

	if count > maxCount:
		maxCount = count
		baseLoc = a

asteroids.remove(baseLoc)
angles = sorted(((angle(baseLoc, ast), ast) for ast in asteroids), key=lambda x: (x[0], abs(baseLoc[0] - x[1][0]) + abs(baseLoc[1] - x[1][1])))

idx = 0
prev = angles.pop(idx)
prevAngle = prev[0]
count = 1

while count < 200 and angles:
	if idx >= len(angles):
		idx = 0
		prevAngle = None
	# Cannot shoot an asteroid behind another asteroid
	if prevAngle == angles[idx][0]:
		idx += 1
		continue
	prev = angles.pop(idx)
	prevAngle = prev[0]
	count += 1

print(prev[1][0] * 100 + prev[1][1])