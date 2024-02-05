# Importa a função randint do módulo random para gerar números aleatórios.
from random import randint


# Define a função fizz_buzz que aceita um número inteiro como argumento.
def fizz_buzz(numero: int) -> str:
    # Cria uma lista contendo as strings a serem retornadas com base na lógica do FizzBuzz.
    RETURN_ITEM = ["FizzBuzz", "Fizz", "Buzz", "#"]
    # Verifica se o número é divisível por 3 e por 5 simultaneamente.
    if numero % 3 == 0 and numero % 5 == 0:
        return RETURN_ITEM[0]  # Retorna "FizzBuzz" se a condição for verdadeira.
    # Verifica se o número é divisível apenas por 3.
    elif numero % 3 == 0:
        return RETURN_ITEM[1]  # Retorna "Fizz" se a condição for verdadeira.
    # Verifica se o número é divisível apenas por 5.
    elif numero % 5 == 0:
        return RETURN_ITEM[2]  # Retorna "Buzz" se a condição for verdadeira.
    # Se o número não se encaixar nas condições acima, retorna "#".
    else:
        return RETURN_ITEM[3]


# Gera um número aleatório entre 0 e 100.
NUMERO: int = randint(0, 100)

# Chama a função fizz_buzz com o número aleatório gerado e armazena o resultado.
RESULTADO: str = fizz_buzz(NUMERO)

# Imprime o resultado da função fizz_buzz baseado no número gerado.
print(RESULTADO)
