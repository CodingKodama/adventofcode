class Computer:
    def add(self):
        self.program[self.program[self.instrPointer + 3]] = self.getParam(1) + self.getParam(2)
        self.instrPointer += 4

    def multiply(self):
        self.program[self.program[self.instrPointer + 3]] = self.getParam(1) * self.getParam(2)
        self.instrPointer += 4

    def input(self):
        inputVal = self.getInput()
        if inputVal == None:
            return "Awaiting input"
        self.program[self.program[self.instrPointer + 1]] = inputVal
        self.instrPointer += 2

    def output(self):
        self.output = self.getParam(1)
        self.instrPointer += 2

    def jumpIfTrue(self):
        if self.getParam(1) != 0:
            self.instrPointer = self.getParam(2)
        else:
            self.instrPointer += 3

    def jumpIfFalse(self):
        if self.getParam(1) == 0:
            self.instrPointer = self.getParam(2)
        else:
            self.instrPointer += 3

    def lessThan(self):
        target = self.program[self.instrPointer + 3]
        if self.getParam(1) < self.getParam(2):
            self.program[target] = 1
        else:
            self.program[target] = 0
        self.instrPointer += 4

    def equals(self):
        target = self.program[self.instrPointer + 3]
        if self.getParam(1) == self.getParam(2):
            self.program[target] = 1
        else:
            self.program[target] = 0
        self.instrPointer += 4

    def __init__(self, program):
        self.instrPointer = 0
        self.initialProgram = program
        self.program = program.copy()
        self.inputData = []
        self.inputPointer = -1
        self.ops = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jumpIfTrue,
            6: self.jumpIfFalse,
            7: self.lessThan,
            8: self.equals
        }

    def setInput(self, input):
        self.inputData = input
        self.inputPointer = -1

    def addInput(self, input):
        self.inputData += input

    def getInput(self):
        if self.inputPointer + 1 >= len(self.inputData):
            return None
        self.inputPointer += 1
        return self.inputData[self.inputPointer]

    def getParam(self, paramIndex):
        value = self.program[self.instrPointer + paramIndex]
        adrMode = self.program[self.instrPointer] // (10 * (10 ** paramIndex)) % 10
        if adrMode == 0:
            return self.program[value]
        else:
            return value

    def reset(self):
        self.setInput([])
        self.program = self.initialProgram.copy()
        self.instrPointer = 0

    def run(self, input, reset):
        if reset:
            self.reset()
        self.addInput(input)
        self.output = 0
        self.awaitingInput = False
        while True:
            operation = self.program[self.instrPointer] % 100
            if operation == 99:
                break
            if operation in self.ops:
                if self.ops[operation]() == "Awaiting input":
                    self.awaitingInput = True
                    break
            else:
                print("unknown operation", operation, instrPointer)
        return self.output

import itertools

def getMaxThrusters(program):
    maxThrusters = 0
    phases = [5, 6, 7, 8, 9]

    for phaseSequence in itertools.permutations(phases):
        computers = []
        for i, phase in enumerate(phaseSequence):
            computers.append(Computer(program))
            computers[i].addInput([phase])

        input = 0
        awaitingInput = True
        while awaitingInput:
            for computer in computers:
                input = computer.run([input], False)
                if computer.awaitingInput == False:
                    awaitingInput = False

        if input > maxThrusters:
            maxThrusters = input
    return maxThrusters

with open('input.txt', 'r') as file:
    lines = file.readlines()
program = [int(i) for i in lines[0].split(",")]

testProgram1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
testProgram2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

print("Testresult1 (139629729):", getMaxThrusters(testProgram1))
print("Testresult2 (18216):", getMaxThrusters(testProgram2))

print("Result (36497698):", getMaxThrusters(program))