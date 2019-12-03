def runProgram(program):
	position = 0
	while True:
		operation = program[position]
		if operation == 99:
			break;

		operand1 = program[program[position + 1]]
		operand2 = program[program[position + 2]]
		target = program[position + 3]

		if operation == 1:
			program[target] = operand1 + operand2
		elif operation == 2:
			program[target] = operand1 * operand2
		else:
			print("unknown operation", operation, position)

		position += 4;
	return program[0]


with open('day2a.txt', 'r') as file:
    lines = file.readlines()
program = [int(i) for i in lines[0].split(",")]

initialProgram = program.copy()

for param1 in range(100):
	for param2 in range(100):
		program = initialProgram.copy()
		program[1] = param1
		program[2] = param2

		if runProgram(program) == 19690720:
			print("Result (7264):", 100*param1+param2)
