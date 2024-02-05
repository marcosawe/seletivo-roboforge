#!/usr/bin/env pybricks-micropython

# Importação das bibliotecas de código que serão utilizadas no desenvolvimento.
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Define a inicialização da biblioteca como módulo de documentação.
ev3: object = EV3Brick()

# Definição das variáveis de motor.
LEFT_MOTOR: object = Motor(Port.A)
RIGHT_MOTOR: object = Motor(Port.B)

# Definição do diametro das rodas e da pista de eixo.
WHEEL_DIAMETER: int = 56
AXLE_TRACK: int = 114

# Intanciação da classe que direciona o robo.
ROBOT: object = DriveBase(LEFT_MOTOR, RIGHT_MOTOR, WHEEL_DIAMETER, AXLE_TRACK)

# Definição das classes que compõem o robo.
COLOR_SENSOR: object = ColorSensor(Port.S1)
ULTRASONIC_SENSOR: object = UltrasonicSensor(Port.S2)

# Definição da velocidade em que o robo vai seguir a linha
SPEED: int = 30

# Definição da percepção de distância entre o robo e o quadrado
OBSTACLE_DISTANCE: int = 200

# Loop principal
while True:
    # Lê a intensidade de luz refletida (0 a 100)
    REFLECTION: int = COLOR_SENSOR.reflection()
    # Calcula o desvio da leitura para o valor de referência
    # Ajusta os valores abaixo conforme a necessidade para melhor seguimento da linha
    DEVIATION: float = REFLECTION - 50
    TURN_RATE: float = DEVIATION * 2  # Ajusta a taxa de giro baseada no desvio
    # Verifica se há um "quadrado" ou obstáculo à frente
    if ULTRASONIC_SENSOR.distance() < OBSTACLE_DISTANCE:
        # Detecta a cor sob o sensor
        COLOR: object = COLOR_SENSOR.color()
        # Para o robô se detectar um obstáculo e a cor amarela
        if COLOR == Color.YELLOW:
            ROBOT.stop()
            wait(10000)  # Espera 5 segundos
        # Para o robô se detectar um obstáculo e a cor verde
        elif COLOR == Color.GREEN:
            ROBOT.stop()
        else:
            wait(1000)  # Pequena pausa antes de continuar
    else:
        # Se não há obstáculos, continua seguindo a linha
        ROBOT.drive(SPEED, TURN_RATE)
