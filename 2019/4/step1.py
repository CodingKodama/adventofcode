def validateCode(passcode):
    last = 0
    duplicate = False
    for char in passcode:
        digit = int(char)
        if digit < last:
            return False
        
        if digit == last:
            duplicate = True

        last = digit
    return duplicate

def bruteForce(start, end):
    validCodes = 0
    for code in range(start, end + 1):
        if validateCode(str(code)):
            validCodes += 1
    return validCodes

print("111111 (true):", validateCode("111111"))
print("223450 (false):", validateCode("223450"))
print("123789 (false):", validateCode("123789"))
print("122345 (true):", validateCode("122345"))

print("Result (1625):", bruteForce(171309, 643603))