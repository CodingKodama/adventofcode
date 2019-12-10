class Computer:
    def add(self):
        self.program[self.program[self.instrPointer + 3]] = self.getParam(1) + self.getParam(2)
        self.instrPointer += 4

    def multiply(self):
        self.program[self.program[self.instrPointer + 3]] = self.getParam(1) * self.getParam(2)
        self.instrPointer += 4

    def input(self):
        self.program[self.program[self.instrPointer + 1]] = self.getInput()
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
        self.input = input
        self.inputPointer = -1

    def getInput(self):
        self.inputPointer += 1
        return self.input[self.inputPointer]

    def getParam(self, paramIndex):
        value = self.program[self.instrPointer + paramIndex]
        adrMode = self.program[self.instrPointer] // (10 * (10 ** paramIndex)) % 10
        if adrMode == 0:
            return self.program[value]
        else:
            return value

    def run(self, input):
        self.setInput(input)
        self.program = self.initialProgram.copy()
        self.output = 0
        self.instrPointer = 0
        while True:
            operation = self.program[self.instrPointer] % 100
            if operation == 99:
                break; 
            if operation in self.ops:
                self.ops[operation]()
            else:
                print("unknown operation", operation, instrPointer)
        return self.output

import itertools

def getMaxThrusters(computer):
    maxThrusters = 0
    for phaseSequence in itertools.permutations([0, 1, 2, 3, 4]):
        input = 0
        for phase in phaseSequence:
            input = computer.run([phase, input])
        if input > maxThrusters:
            maxThrusters = input
    return maxThrusters

with open('input.txt', 'r') as file:
    lines = file.readlines()
program = [int(i) for i in lines[0].split(",")]

testComputer1 = Computer([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
testComputer2 = Computer([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
testComputer3 = Computer([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])


print("Testresult1 (43210):", getMaxThrusters(testComputer1))
print("Testresult2 (54321):", getMaxThrusters(testComputer2))
print("Testresult3 (65210):", getMaxThrusters(testComputer3))

print("Result:", getMaxThrusters(Computer(program)))