class Computer:
    def add(self):
        self.memory[self.getParam(3)] = self.mem(self.getParam(1)) + self.mem(self.getParam(2))
        self.instrPointer += 4

    def multiply(self):
        self.memory[self.getParam(3)] = self.mem(self.getParam(1)) * self.mem(self.getParam(2))
        self.instrPointer += 4

    def input(self):
        inputVal = self.getInput()
        if inputVal == None:
            return "Awaiting input"
        self.memory[self.getParam(1)] = inputVal
        self.instrPointer += 2

    def output(self):
        self.output = self.mem(self.getParam(1))
        self.allOutputs.append(self.output)
        self.instrPointer += 2

    def jumpIfTrue(self):
        if self.mem(self.getParam(1)) != 0:
            self.instrPointer = self.mem(self.getParam(2))
        else:
            self.instrPointer += 3

    def jumpIfFalse(self):
        if self.mem(self.getParam(1)) == 0:
            self.instrPointer = self.mem(self.getParam(2))
        else:
            self.instrPointer += 3

    def lessThan(self):
        if self.mem(self.getParam(1)) < self.mem(self.getParam(2)):
            self.memory[self.getParam(3)] = 1
        else:
            self.memory[self.getParam(3)] = 0
        self.instrPointer += 4

    def equals(self):
        if self.mem(self.getParam(1)) == self.mem(self.getParam(2)):
            self.memory[self.getParam(3)] = 1
        else:
            self.memory[self.getParam(3)] = 0
        self.instrPointer += 4

    def adjustRelativeBase(self):
        self.relativeBase += self.mem(self.getParam(1))
        self.instrPointer += 2

    def __init__(self, program):
        self.instrPointer = 0
        self.relativeBase = 0
        self.initialProgram = program
        self.loadMem(program)
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
            8: self.equals,
            9: self.adjustRelativeBase
        }

    def mem(self, adr):
        if adr in self.memory:
            return self.memory[adr]
        else:
            return 0

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
        paramAdr = self.instrPointer + paramIndex
        adrMode = self.mem(self.instrPointer) // (10 * (10 ** paramIndex)) % 10
        if adrMode == 0:
            return self.mem(paramAdr)
        elif adrMode == 1:
            return paramAdr
        elif adrMode == 2:
            return self.mem(paramAdr) + self.relativeBase
        else:
            print("Unknown adr mode", adrMode)

    def loadMem(self, data):
        self.memory = {}
        for adr, d in enumerate(data):
            self.memory[adr] = d

    def reset(self):
        self.setInput([])
        self.loadMem(self.initialProgram)
        self.instrPointer = 0
        self.relativeBase = 0

    def run(self, input = [], reset = False):
        if reset:
            self.reset()
        self.addInput(input)
        self.output = 0
        self.allOutputs = []
        self.awaitingInput = False
        while True:
            operation = self.mem(self.instrPointer) % 100
            if operation == 99:
                break
            if operation in self.ops:
                if self.ops[operation]() == "Awaiting input":
                    self.awaitingInput = True
                    break
            else:
                print("unknown operation", operation, instrPointer)
        return self.output


testProgram1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
testComputer1 = Computer(testProgram1)
testComputer1.run([])
print("TestComputer1 output:", testComputer1.allOutputs)

testProgram2 = [1102,34915192,34915192,7,4,7,99,0]
testComputer2 = Computer(testProgram2)
testComputer2.run()
print("Test4: ", testComputer2.allOutputs)

testComputer3 = Computer([104,1125899906842624,99])
testComputer3.run()
print("Test3", testComputer3.allOutputs)

with open('input.txt', 'r') as file:
    lines = file.readlines()
boostProgram = [int(i) for i in lines[0].split(",")]

boostComputer = Computer(boostProgram)
print("Step 1 (2204990589):", boostComputer.run([1]))

print("Step 2 result (50008):", boostComputer.run([2], True))