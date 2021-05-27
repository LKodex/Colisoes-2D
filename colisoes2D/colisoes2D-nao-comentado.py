class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def isColliding(rect1, rect2):
    if (rect1.x1 > rect2.x2) or (rect1.x2 < rect2.x1) or (rect1.y1 > rect2.y2) or (rect1.y2 < rect2.y1):
        return False
    else:
        return True

def estaColidindo(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if (ax1 > bx2) or (ax2 < bx1) or (ay1 > by2) or (ay2 < by1):
        return False
    else:
        return True

def testeRapido():
    retanguloA = Rectangle(0, 0, 10, 10)
    retanguloB = Rectangle(5, 5, 15, 15)
    if isColliding(retanguloA, retanguloB):
        print('Os retangulos se colidem')
    else:
        print('Os retangulos não se colidem')

    if estaColidindo(0, 0, 10, 10, 5, 5, 15, 15):
        print('As coordenadas criam uma colisão entre dois retangulos')
    else:
        print('As coordenadas não criam uma colisão entre dois retangulos')

def main():
    testeRapido()

if __name__ == "__main__":
    main()
