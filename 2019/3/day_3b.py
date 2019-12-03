def addCoord(grid, coord, wireIndex, distance):
	if coord in grid:
		if wireIndex not in grid[coord]:
			grid[coord][wireIndex] = distance
	else:
		grid[coord] = {wireIndex: distance}

def computeWireGrid(wires):
	grid = {}
	wireIndex = 0
	grid[(0, 0)] = [-1]
	for wire in wires:
		x = 0;
		y = 0;
		length = 0;
		turns = wire.split(",")
		for turn in turns:
			direction = turn[0]
			distance = int(turn[1:])
			for i in range(distance):
				if direction == "D":
					y += 1
				elif direction == "U":
					y -= 1
				elif direction == "R":
					x += 1
				elif direction == "L":
					x -= 1
				else:
					print("Unknown direction", direction)
				length += 1
				addCoord(grid, (x, y), wireIndex, length)
		wireIndex += 1
	return grid

def getClosesIntersection(grid):
	min = 10000000
	for coord, wires in grid.items():
		if len(wires) > 1:
			dist = wires[0] + wires[1]
			if dist < min:
				print("New dist", dist, "at", coord, "with wires", wires)
				min = dist
	return min

with open('day3a.txt', 'r') as file:
    lines = file.readlines()

testData1 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
testData2 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
testData3 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]

print("Test1 (610):", getClosesIntersection(computeWireGrid(testData1)))
print("Test2 (410):", getClosesIntersection(computeWireGrid(testData2)))
print("Test3 (30):", getClosesIntersection(computeWireGrid(testData3)))

print("Result (7534):", getClosesIntersection(computeWireGrid(lines)))
