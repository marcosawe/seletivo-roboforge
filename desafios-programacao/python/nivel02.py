from math import sqrt, acos, degrees


# Função para calcular a distância entre dois pontos
def calcular_distancia(P1, P2):
    return sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)


# Função para calcular o ângulo oposto a um lado
def calcular_angulo(A, B, C):
    # Lei dos Cossenos
    return degrees(acos((B**2 + C**2 - A**2) / (2 * B * C)))


# Função para classificar o triângulo quanto aos lados
def classificar_triangulo_lados(A, B, C):
    if A == B == C:
        return "Equilátero"
    elif A == B or A == C or B == C:
        return "Isósceles"
    else:
        return "Escaleno"


# Função para classificar o triângulo quanto aos ângulos
def classificar_triangulo_angulos(ANGULOS):
    if all(ANGULO < 90 for ANGULO in ANGULOS):
        return "Acutângulo"
    elif any(ANGULO == 90 for ANGULO in ANGULOS):
        return "Retângulo"
    else:
        return "Obtusângulo"


# Solicitando ao usuário os pontos do triângulo
print("Defina os pontos do triangulo: ")
PONTO_AX = int(input())
PONTO_AY = int(input())
PONTO_BX = int(input())
PONTO_BY = int(input())
PONTO_CX = int(input())
PONTO_CY = int(input())

# Definindo os pontos do triângulo
PONTO_A = (PONTO_AX, PONTO_AY)
PONTO_B = (PONTO_BX, PONTO_BY)
PONTO_C = (PONTO_CX, PONTO_CY)

# Calculando os lados do triângulo
LADO_AB = calcular_distancia(PONTO_A, PONTO_B)
LADO_AC = calcular_distancia(PONTO_A, PONTO_C)
LADO_BC = calcular_distancia(PONTO_B, PONTO_C)

# Calculando os ângulos do triângulo
ANGULO_A = calcular_angulo(LADO_BC, LADO_AB, LADO_AC)
ANGULO_B = calcular_angulo(LADO_AC, LADO_AB, LADO_BC)
ANGULO_C = 180 - ANGULO_A - ANGULO_B

# Calculando o perímetro do triângulo
PERIMETRO = LADO_AB + LADO_AC + LADO_BC

# Calculando a área do triângulo usando a Fórmula de Heron
S = PERIMETRO / 2
AREA = sqrt(S * (S - LADO_AB) * (S - LADO_AC) * (S - LADO_BC))

# Classificando o triângulo
CLASSIFICACAO_LADOS = classificar_triangulo_lados(LADO_AB, LADO_AC, LADO_BC)
CLASSIFICACAO_ANGULOS = classificar_triangulo_angulos([ANGULO_A, ANGULO_B, ANGULO_C])

# Imprimindo os resultados
print(f"Lados do triângulo: {LADO_AB:.2f}, {LADO_AC:.2f}, {LADO_BC:.2f}")
print(f"Ângulos do triângulo: {ANGULO_A:.2f}, {ANGULO_B:.2f}, {ANGULO_C:.2f}")
print(f"Perímetro do triângulo: {PERIMETRO:.2f}")
print(f"Área do triângulo: {AREA:.2f}")
print(f"Classificação quanto aos lados: {CLASSIFICACAO_LADOS}")
print(f"Classificação quanto aos ângulos: {CLASSIFICACAO_ANGULOS}")
