class AstralMap:
    def __init__(self, orbits):
        self.childrenMap = {}
        self.parentMap = {}
        for orbit in orbits:
            objects = orbit.split(")")
            if objects[0] in self.childrenMap:
                self.childrenMap[objects[0]].add(objects[1])
            else:
                self.childrenMap[objects[0]] = { objects[1] }
            self.parentMap[objects[1]] = objects[0]

    def getChecksum(self):
        checksum = 0
        for object in self.parentMap.keys():
            checksum += len(self.getPathToCenter(object))
        return checksum

    def getPathToCenter(self, object):
        path = []
        while True:
            parent = None
            if object in self.parentMap:
                parent = self.parentMap[object]
            if parent == None:
                return path
            else:
                object = parent
                path.append(parent)

    def getShortestPath(self, origin, target):
        targetToCenter = self.getPathToCenter(target)
        originToCenter = self.getPathToCenter(origin)
        for node in originToCenter:
            if node in targetToCenter:
                return targetToCenter.index(node) + originToCenter.index(node)


with open('input.txt', 'r') as file:
    orbits = [line.strip() for line in file.readlines()]

testInput = ["COM)B",
"B)C",
"C)D",
"D)E",
"E)F",
"B)G",
"G)H",
"D)I",
"E)J",
"J)K",
"K)L"]

testMap = AstralMap(testInput)
print("Testchecksum (42):", testMap.getChecksum())

testPathMap = AstralMap(testInput + ["K)YOU", "I)SAN"])
print("TestPath (4):", testPathMap.getShortestPath("YOU", "SAN"))

astralMap = AstralMap(orbits)
print("Shortest path (445):", astralMap.getShortestPath("YOU", "SAN"))
print("Checksum (254447):", astralMap.getChecksum())
