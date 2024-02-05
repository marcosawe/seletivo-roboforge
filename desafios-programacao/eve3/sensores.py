#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Inicializações Gerais
ev3: object = EV3Brick()
MOTOR_ESQUERDO: object = Motor(Port.A)
MOTOR_DIREITO: object = Motor(Port.D)
DIAMETRO_RODA: int = 56
DISTANCIA_EIXO: int = 114

MOVIMENTO_BASE: object = DriveBase(MOTOR_ESQUERDO, MOTOR_DIREITO, DIAMETRO_RODA, DISTANCIA_EIXO)

COR_SENSOR: object = ColorSensor(Port.S3)
sensor_ultrassonico: object = UltrasonicSensor(Port.S4)

# Constantes
DISTANCIA_PAREDE: int = 200  # Distância desejada da parede em mm
VELOCIDADE: int = 100  # Velocidade do robô em mm/s
ANGULO_GIRO: int = 90  # Ângulo de giro para curvas
VELOCIDADE_GIRO: int = 50  # Velocidade de giro


# Função principal
def seguir_parede():
    while True:
        # Mantendo a distância da parede
        DISTANCIA = sensor_ultrassonico.distance()
        if DISTANCIA > DISTANCIA_PAREDE + 10:
            # Se estiver muito longe, move-se para mais perto
            MOVIMENTO_BASE.drive(VELOCIDADE, -VELOCIDADE_GIRO)
        elif DISTANCIA < DISTANCIA_PAREDE - 10:
            # Se estiver muito perto, move-se para mais longe
            MOVIMENTO_BASE.drive(VELOCIDADE, VELOCIDADE_GIRO)
        else:
            # Mantendo o movimento paralelo à parede
            MOVIMENTO_BASE.drive(VELOCIDADE, 0)

        # Verificando a cor no chão
        COR_CHAO = COR_SENSOR.color()
        if COR_CHAO == Color.RED:
            # Girando 90 graus para a direita
            MOVIMENTO_BASE.turn(ANGULO_GIRO)
        elif COR_CHAO == Color.YELLOW:
            # Esperando por um comando (botão pressionado)
            ev3.speaker.beep()
            while not any(ev3.buttons.pressed()):
                wait(10)
        elif COR_CHAO == Color.GREEN:
            # Parando completamente
            MOVIMENTO_BASE.stop()
            break


# Executando a função
seguir_parede()
