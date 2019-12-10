class ImageLayer:
    def __init__(self, dimensions, sifData, startIndex = 0):
        self.layer = [[int(sifData[startIndex + x + y * dimensions[0]]) for x in range(dimensions[0])] for y in range(dimensions[1])]
        self.dimensions = dimensions

    def print(self):
        for y in range(self.dimensions[1]):
            row = ""
            for x in range(self.dimensions[0]):
                row += str(self.get(x, y))
            print(row)

    def get(self, x, y):
        return self.layer[y][x]

    def pixelCountWithValue(self, value):
        count = 0
        for y in range(self.dimensions[1]):
            for x in range(self.dimensions[0]):
                if self.get(x, y) == value:
                    count += 1
        return count

class Image:
    def __init__(self, dimensions, sifData):
        self.layers = []
        self.dimensions = dimensions
        self.renderMap = {
            0: "#",
            1: " "
        }
        index = 0
        while index < len(sifData):
            self.layers.append(ImageLayer(dimensions, sifData, index))
            index += dimensions[0] * dimensions[1]

    def print(self):
        for index, layer in enumerate(self.layers):
            print("Layer", index + 1)
            layer.print()

    def checksum(self):
        fewestZeroesLayer = None
        nrOfZeroes = 9999999
        for index, layer in enumerate(self.layers):
            count = layer.pixelCountWithValue(0)
            if count < nrOfZeroes:
                fewestZeroesLayer = layer
                nrOfZeroes = count
        return fewestZeroesLayer.pixelCountWithValue(1) * fewestZeroesLayer.pixelCountWithValue(2)

    def getPixelValue(self, x, y):
        for layer in self.layers:
            pixelValue = layer.get(x, y)
            if pixelValue != 2:
                break
        return pixelValue

    def render(self):
        for y in range(self.dimensions[1]):
            row = ""
            for x in range(self.dimensions[0]):
                row += self.renderMap[self.getPixelValue(x, y)]
            print(row)



with open('input.txt', 'r') as file:
    imageData = file.readlines()[0].strip()

testImage1 = Image((3, 2), "123456782912")
renderTest = Image((2, 2), "0222112222120000")
print("Test1 Checksum (1):", testImage1.checksum())
print("Rendertest:")
renderTest.render()

image = Image((25, 6), imageData)
print("Result: (1452)", image.checksum())
print("Rendered (PHPEU):")
image.render()