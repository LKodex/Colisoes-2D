### Fórmula da Colisão
### (ax1 >= bx1 and ax1 <= bx2 or ax2 >= bx1 and ax2 <= bx2) and (ay1 >= by1 and ay1 <= by2 or ay2 >= by1 and ay2 <= by2)
### As funções começadas com "coord" não utilizam classes

# Definindo a classe Rectangle
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

### --- Usando classes (as funções recebem Rectangle como parametros) --- ###
# Definindo função para checar não colisão entre retangulos (Rectangle)
# A função pergunta "Estão Colidindo?" retorna Falso se não houver colisão ou Verdadeiro para caso de colisão
# Recebe um par de Rectangle como parametros
def isColliding(A, B):
    if((A.x1 >= B.x1 and A.x1 <= B.x2 or A.x2 >= B.x1 and A.x2 <= B.x2) and (A.y1 >= B.y1 and A.y1 <= B.y2 or A.y2 >= B.y1 and A.y2 <= B.y2)):
        return True
    else:
        return False

# Definindo função para checar não colisão entre retangulos (Rectangle)
# A função pergunta "Não Estão Colidindo?" retorna Falso se não houver colisão ou Verdadeiro para caso de colisão
# Recebe um par de Rectangle como parametros
def isNotColliding(A, B):
    # Checa se os retangulos não estão colidindo
    if (A.x1 > B.x2) or (A.x2 < B.x1) or (A.y1 > B.y2) or (A.y2 < B.y1):
        # Caso de não colisão, retorna False para dizer que não ocorre colisão
        return False
    else:
        # Caso de colisão, retorna True para dizer que ocorre colisão
        return True

### --- Sem usar classes (apenas usando inputs diretos) --- ###
# Definindo função para checar não colisão entre coordenadas de retangulos
# A função pergunta "As Coordenadas Estão Colidindo?" retorna Falso se não houver colisão ou Verdadeiro para caso de colisão
# Recebe um par de 4 coordenadas como parametro
def coordIsColliding(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if((ax1 >= bx1 and ax1 <= bx2 or ax2 >= bx1 and ax2 <= bx2) and (ay1 >= by1 and ay1 <= by2 or ay2 >= by1 and ay2 <= by2)):
        return True
    else:
        return False

# Definindo função para checar não colisão entre coordenadas passadas por parametros
# A função pergunta "As Coordenadas Não Estão Colidindo?" retorna Verdadeiro se não houver colisão ou Falso para caso de colisão
# Recebe um par de 4 coordenadas como parametro
def coordIsNotColliding(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Checa se as coordenadas de dois retangulos não estão causando colisão entre eles
    if (ax1 > bx2) or (ax2 < bx1) or (ay1 > by2) or (ay2 < by1):
        # Caso de não colisão, retorna True para dizer que sim, não está ocorrendo colisão
        return True
    else:
        # Caso de colisão, retorna False para dizer que não, ocorre colisão
        return False

# Chame esta função durante a execução para testar o código rápidamente
def testeRapido():
    # Primeiro teste
    retanguloA = Rectangle(0, 0, 10, 10)
    retanguloB = Rectangle(10, 10, 20, 20)
    print(isColliding(retanguloB, retanguloA)) # Resultado esperado = True

    # Segundo teste
    print(coordIsColliding(0, 0, 10, 10, 10, 10, 20, 20)) # Resultado esperado = True

    # Terceiro teste
    rectC = Rectangle(0, 0, 10, 10)
    rectD = Rectangle(-5, 11, 20, 20)
    print(isColliding(rectC, rectD)) # Resultado esperado = False

    # Quarto teste
    print(coordIsColliding(0, 0, 10, 10, -5, 11, 20, 20)) # Resultado esperado = False

def main():
    testeRapido()

if __name__ == "__main__":
    main()
