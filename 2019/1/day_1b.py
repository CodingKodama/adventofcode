def getFuelWeight(moduleWeight):
	return moduleWeight//3-2

def calcTotalWeight(modules):
	total = 0
	for module in modules:
		additionalFuel = getFuelWeight(int(module))
		while additionalFuel > 0:
			total += additionalFuel
			additionalFuel = getFuelWeight(additionalFuel)
	return total



with open('day1a.txt', 'r') as file:
    lines = file.readlines()
print("Total (5162216):", calcTotalWeight(lines))
