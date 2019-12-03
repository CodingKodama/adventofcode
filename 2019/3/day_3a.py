def addCoord(grid, coord, wireIndex):
	if coord in grid:
		grid[coord].add(wireIndex)
	else:
		grid[coord] = {wireIndex}

def computeWireGrid(wires):
	grid = {}
	wireIndex = 0
	grid[(0, 0)] = [-1]
	for wire in wires:
		x = 0;
		y = 0;
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
				addCoord(grid, (x, y), wireIndex)
		wireIndex += 1
	return grid

def getClosesIntersectionDistance(grid):
	min = 10000000 #let's pretend it's infinite...
	for coord, wires in grid.items():
		if len(wires) > 1:
			dist = abs(coord[0]) + abs(coord[1])
			if dist < min:
				print("New min dist", dist, "at", coord)
				min = dist
	return min

with open('day3a.txt', 'r') as file:
    lines = file.readlines()

testData1 = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
testData2 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72","U62,R66,U55,R34,D71,R55,D58,R83"]
testData3 = ["R8,U5,L5,D3", "U7,R6,D4,L4"]

print("Test1 (135)", getClosesIntersectionDistance(computeWireGrid(testData1)))
print("Test2 (159)", getClosesIntersectionDistance(computeWireGrid(testData2)))
print("Test3 (6)", getClosesIntersectionDistance(computeWireGrid(testData3)))

print("Result (651):", getClosesIntersectionDistance(computeWireGrid(lines)))