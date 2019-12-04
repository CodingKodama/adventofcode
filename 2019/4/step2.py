def validateCode(passcode):
    last = 0
    duplicate = False
    sequenceLength = 1
    for char in passcode:
        digit = int(char)
        if digit < last:
            return False
        
        if digit == last:
            sequenceLength += 1
        else:
            if sequenceLength == 2:
                duplicate = True
            sequenceLength = 1     


        last = digit
    return duplicate or sequenceLength == 2

def bruteForce(start, end):
    validCodes = 0
    for code in range(start, end + 1):
        if validateCode(str(code)):
            validCodes += 1
    return validCodes

print("111111 (false):", validateCode("111111"))
print("223450 (false):", validateCode("223450"))
print("123789 (false):", validateCode("123789"))
print("122345 (true):", validateCode("122345"))
print("123444 (false):", validateCode("123444"))

print("Result (1111):", bruteForce(171309, 643603))