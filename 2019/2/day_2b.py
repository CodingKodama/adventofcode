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

program[1] = 12
program[2] = 2

print("Result (4138658)", runProgram(program))