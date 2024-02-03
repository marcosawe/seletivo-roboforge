#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

LEFT_MOTOR:object = Motor(Port.A)
RIGTH_MOTOR:object = Motor(Port.B)
WHEEL_DIAMETER:int = 56
AXLE_TRACK:int = 114

ROBOT:object = DriveBase(LEFT_MOTOR, RIGTH_MOTOR, WHEEL_DIAMETER, AXLE_TRACK)

COLOR_SENSOR:object = ColorSensor(Port.S1)
ULTRASONIC_SENSOR:object = UltrasonicSensor(Port.S2)

SPEED:int = 30

OBSTACLE_DISTANCE:int = 200

# Loop principal
while True:
    # Lê a intensidade de luz refletida (0 a 100)
    REFLECTION:object = COLOR_SENSOR.reflection()
    
    # Calcula o desvio da leitura para o valor de referência
    # Ajusta os valores abaixo conforme a necessidade para melhor seguimento da linha
    DEVIATION:float = REFLECTION - 50
    TURN_RATE:float = DEVIATION * 2  # Ajusta a taxa de giro baseada no desvio
    
    # Verifica se há um "quadrado" ou obstáculo à frente
    if ULTRASONIC_SENSOR.distance() < OBSTACLE_DISTANCE:
        # Detecta a cor sob o sensor
        COLOR:object = COLOR_SENSOR.color()
        
        # Para o robô se detectar um obstáculo e a cor amarela
        if COLOR == Color.YELLOW:
            ROBOT.stop()
            wait(5000)  # Espera 5 segundos
        # Para o robô se detectar um obstáculo e a cor verde
        elif COLOR == Color.GREEN:
            ROBOT.stop()
        else:
            wait(2)  # Pequena pausa antes de continuar
    else:
        # Se não há obstáculos, continua seguindo a linha
        ROBOT.drive(SPEED, TURN_RATE)


