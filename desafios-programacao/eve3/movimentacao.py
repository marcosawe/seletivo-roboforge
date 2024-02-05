#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

# Inicializa o hub EV3
eve3: object = EV3Brick()

# Inicializando os motores
MOTO_ESQUERDO: object = Motor(Port.S3)
MOTOR_DIREITO: object = Motor(Port.S4)


def rodar_motores(velocidade_esq, velocidade_dir, tempo):
    """
    Roda ambos os motores com velocidades especificadas por um tempo determinado.
    """
    MOTO_ESQUERDO.run(velocidade_esq)
    MOTOR_DIREITO.run(velocidade_dir)
    wait(tempo)
    MOTO_ESQUERDO.stop()
    MOTOR_DIREITO.stop()


def rodar_motor_esquerdo(velocidade, tempo):
    """
    Roda o motor esquerdo com uma velocidade e tempo especificados.
    """
    MOTO_ESQUERDO.run_time(speed=velocidade, time=tempo)
    wait(tempo)  # Espera até a conclusão da ação do motor


# Define a sequência de ações para os motores
def executar_sequencia():
    """
    Executa uma sequência predefinida de ações usando os motores.
    """
    # Roda ambos os motores por 3 segundos a 200 de velocidade
    rodar_motores(200, 200, 3000)
    # Roda o motor esquerdo com uma velocidade diferente por 2 segundos
    rodar_motor_esquerdo(400, 2000)


# # Contador para a condição de saída
contador_de_ciclos: int = 0
CICLOS_MAXIMOS: int = 2  # Define o número máximo de ciclos

# Loop principal com condição de saí: intda
while contador_de_ciclos < CICLOS_MAXIMOS:
    executar_sequencia()
    contador_de_ciclos += 1
    # Apertando o botão o código será interrompido
    if Button.CENTER in eve3.buttons.pressed():
        print("Interrupção pelo botão central.")
        break
