from itertools import permutations

commandList = [3,8,1001,8,10,8,105,1,0,0,21,38,59,84,93,110,191,272,353,434,99999,3,9,101,5,9,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,5,9,9,1001,9,4,9,1002,9,2,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,1002,9,5,9,101,4,9,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99]

def executeCommand(idx = 0, commands = [], phase = -1, inVal = 0):
	code = commands[idx]
	phase = phase

	if code == 99:
		return idx, commands, phase, True, None

	codeStr = str(code).zfill(5)
	opCode = int(codeStr[-2:])
	# mode 0 = index; 1 = value
	modes = [int(x) for x in codeStr[:-2].zfill(3)][::-1]

	firstIdx = commands[idx + 1]
	firstVal = commands[firstIdx] if modes[0] == 0 else firstIdx

	if opCode == 4:
		idx += 2
		return idx, commands, phase, False, firstVal
	if opCode == 3:
		idx += 2

		if phase < 0:
			commands[firstIdx] = inVal
			return idx, commands, phase, False, None
		else:
			commands[firstIdx] = phase
			return idx, commands, -1, False, None

	secondIdx = commands[idx + 2]
	secondVal = commands[secondIdx] if modes[1] == 0 else secondIdx

	if opCode == 6:
		idx = secondVal if firstVal == 0 else (idx + 3)
		return idx, commands, phase, False, None
	if opCode == 5:
		idx = secondVal if firstVal != 0 else (idx + 3)
		return idx, commands, phase, False, None

	outIdx = commands[idx + 3]

	if opCode == 8:
		commands[outIdx] = 1 if firstVal == secondVal else 0
	if opCode == 7:
		commands[outIdx] = 1 if firstVal < secondVal else 0
	elif opCode == 2:
		commands[outIdx] = firstVal * secondVal
	elif opCode == 1:
		commands[outIdx] = firstVal + secondVal

	idx += 4

	return idx, commands, phase, False, None

def compute(comms = [], phase = 0, inVal = 0):
	result = ""
	idx = 0
	phaseVal = phase

	while idx < len(comms):
		idx, comms, phaseVal, brk, out = executeCommand(idx, comms, phaseVal, inVal)

		if brk:
			break

		if out is not None:
			result = out

	return result

# phases: 0...4 (incl)
# inputs: 0, (prev out)

permuts = list(permutations(range(5)))
results = {}

for phaseList in permuts:
	lastInput = 0
	key = "".join(str(w) for w in phaseList)

	if key not in results:
		results[key] = -1

	for p in phaseList:
		lastInput = compute(commandList.copy(), p, lastInput)
	
	results[key] = lastInput

results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}
print(list(results.values())[0])