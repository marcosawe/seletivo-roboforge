# Importando o módulo random para gerar números aleatórios.
import random


# Definindo a função eh_primo que verifica se um número é primo.
def eh_primo(N: int) -> bool:
    # Retorna False se N for menor ou igual a 1, pois números primos são maiores que 1.
    if N <= 1:
        return False
    # Iterando de 2 até a raiz quadrada de N, mais um, para verificar divisores.
    for i in range(2, int(N**0.5) + 1):
        # Se N é divisível por i, então N não é primo.
        if N % i == 0:
            return False
    # Se não foram encontrados divisores, retorna True, indicando que N é primo.
    return True


# Definindo a função gerar_lista_numeros para criar uma lista de 10 números aleatórios.
def gerar_lista_numeros(INICIO: int, FIM: int) -> list:
    # Usa list comprehension para gerar 10 números aleatórios entre INICIO e FIM.
    return [random.randint(INICIO, FIM) for _ in range(10)]


# Definindo a função multiplicar_primos para calcular o produto dos números primos em uma lista.
def multiplicar_primos(NUMEROS: list) -> int:
    # Inicializando a variável produto como 1 (elemento neutro da multiplicação).
    produto = 1
    # Iterando sobre cada número na lista NUMEROS.
    for numero in NUMEROS:
        # Verificando se o número atual é primo.
        if eh_primo(numero):
            # Multiplicando o produto pelo número primo.
            produto *= numero
    # Retornando o produto final após iterar por toda a lista.
    return produto


# Definindo os valores de início e fim para o intervalo dos números aleatórios.
INICIO, FIM = 1, 100

# Gerando a lista de números usando a função gerar_lista_numeros.
lista_numeros = gerar_lista_numeros(INICIO, FIM)

# Calculando o produto dos números primos na lista gerada.
produto_primos = multiplicar_primos(lista_numeros)

# Imprimindo a lista de números gerados e o produto dos números primos encontrados.
print(f"Lista de Números: {lista_numeros}")
print(f"Produto dos Números Primos: {produto_primos}")
