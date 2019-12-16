import copy

commands = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0]

# result = -1

# for idx in range(0, len(commands), 4):
# 	code = commands[idx]

# 	if code == 99:
# 		result = commands[0]
# 		break
# 	else:
# 		firstIdx = commands[idx + 1]
# 		secondIdx = commands[idx + 2]
# 		outIdx = commands[idx + 3]

# 		if code == 1:
# 			commands[outIdx] = commands[firstIdx] + commands[secondIdx]
# 		elif code == 2:
# 			commands[outIdx] = commands[firstIdx] * commands[secondIdx]
# 		else:
# 			print("Uh oh, something went wrong. Code: " + code + " @ " + idx)

# if result < 0:
# 	result = commands[0]

# print(result)

for noun in range(100):
	for verb in range(100):
		modified = copy.deepcopy(commands)
		modified[1] = noun
		modified[2] = verb
		length = len(modified)
		result = -1

		for idx in range(0, length, 4):
			code = modified[idx]

			if code == 99:
				result = modified[0]
				break
			else:
				firstIdx = modified[idx + 1]
				secondIdx = modified[idx + 2]
				outIdx = modified[idx + 3]

				if firstIdx > length or secondIdx > length or outIdx > length:
					break

				if code == 1:
					modified[outIdx] = modified[firstIdx] + modified[secondIdx]
				elif code == 2:
					modified[outIdx] = modified[firstIdx] * modified[secondIdx]
				else:
					print("Uh oh, something went wrong. Code: " + str(code) + " @ " + str(idx))

		if result < 0:
			result = modified[0]

		if result == 19690720:
			answer = (100 * noun) + verb
			print(str(answer) + " ");