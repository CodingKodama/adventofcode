def getFuelWeight(moduleWeight):
	return moduleWeight//3-2

def calcTotalWeight(modules):
	total = 0
	for module in modules:
		total += getFuelWeight(int(module))
	return total


with open('day1a.txt', 'r') as file:
    lines = file.readlines()
print("Total (3443395):", calcTotalWeight(lines))
