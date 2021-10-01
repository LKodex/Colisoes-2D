class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def rectIsColliding(self, rect):
        try:
            if (self.x > rect.x + rect.width) or (self.x + self.width < rect.x) or (self.y > rect.y + rect.height) or (self.y + self.height < rect.y):
                return False
            else:
                return True
        except:
            print("ERROR! Exception = Class:Rectangle | Method:rectIsColliding | Returning:False")
            return False

    def pointIsColliding(self, xPos, yPos):
        try:
            if (xPos < self.x) or (xPos > self.x + self.width) or (yPos < self.y) or (yPos > self.y + self.height):
                return False
            else:
                return True
        except:
            print("ERROR! Exception = Class:Rectangle | Method:pointIsColliding | Returning:False")
            return False

def simpleTest():
    retanguloA = Rectangle(0, 0, 100, 100)
    retanguloB = Rectangle(50, 50, 150, 150)
    if retanguloA.rectIsColliding(retanguloB) and retanguloB.rectIsColliding(retanguloA):
        print('The Rectangles are colliding!')
    else:
        print('The Rectangles are not colliding!')

    retanguloA.x = 500
    retanguloA.y = 800
    if retanguloA.pointIsColliding(550, 850):
        print('The x, y coordinates are colliding with the Rectangle A')
    else:
        print('The x, y coordinates are not colliding with the Rectangle A')
    
    if retanguloB.pointIsColliding(201, 100):
        print('The x, y coordinates are colliding with the Rectangle B')
    else:
        print('The x, y coordinates are not colliding with the Rectangle B')

def main():
    simpleTest()

if __name__ == "__main__":
    main()
