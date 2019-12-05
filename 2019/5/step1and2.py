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
        print("Output:", self.getParam(1))
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
        self.program = program
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
        while True:
            operation = self.program[self.instrPointer] % 100
            if operation == 99:
                break; 
            if operation in self.ops:
                self.ops[operation]()
            else:
                print("unknown operation", operation, instrPointer)
        return 0


with open('input.txt', 'r') as file:
    lines = file.readlines()
program = [int(i) for i in lines[0].split(",")]

testProgram = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,
1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
print("Test   (1001):")
Computer(testProgram.copy()).run([99])
print("Test   (999):")
Computer(testProgram.copy()).run([4])
print("Test   (1000):")
Computer(testProgram.copy()).run([8])

print("Step 1 (13210611):")
Computer(program.copy()).run([1])

print("Step 2 (584126):")
Computer(program.copy()).run([5])