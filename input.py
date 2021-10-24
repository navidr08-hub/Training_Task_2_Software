from typing import Match
import pygame
from pygame import key
from pygame.constants import KEYDOWN, QUIT
import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)

# KEYS
up = pygame.Rect(200, 75, 100, 100)
down = pygame.Rect(200, 325, 100, 100)
left = pygame.Rect(75, 200, 100, 100)
right = pygame.Rect(325, 200, 100, 100)

controlpad = pygame.display.set_mode((500, 500))

def refresh():
    controlpad.fill(white)
    pygame.draw.rect(controlpad, black, up, 3)
    pygame.draw.rect(controlpad, black, down, 3)
    pygame.draw.rect(controlpad, black, left, 3)
    pygame.draw.rect(controlpad, black, right, 3)

def press_handle(keys):
    direction = ''
    if keys[pygame.K_UP]:
        direction = 'forward'
        controlpad.fill(black, up)
    elif keys[pygame.K_DOWN]:
        direction = 'backward'
        controlpad.fill(black, down)
    elif keys[pygame.K_LEFT]:
        direction = 'left'
        controlpad.fill(black, left)
    elif keys[pygame.K_RIGHT]:
        direction = 'right'
        controlpad.fill(black, right)

    return(direction)


def send_data(motor_data='Hello World!'):
    s.sendall(motor_data.encode('utf-8'))
    data = s.recv(1024)
    print('Received', data.decode('utf-8'))


def motor_control(direction, speed_value):
    data = ''
    if direction == 'forward':
        data = '[f{}][f{}][f{}][f{}]'.format(speed_value, speed_value, speed_value, speed_value)
    elif direction == 'backward':
        data = '[r{}][r{}][r{}][r{}]'.format(speed_value, speed_value, speed_value, speed_value)
    elif direction == 'left':
        data = '[r{}][r{}][f{}][f{}]'.format(speed_value, speed_value, speed_value, speed_value)
    elif direction == 'right':
        data = '[f{}][f{}][r{}][r{}]'.format(speed_value, speed_value, speed_value, speed_value)

    if data != '':
        send_data(data)


def main(): 
    pygame.init()

    s.connect((HOST, PORT))

    pygame.display.set_caption('Controlpad')

    controlpad.fill(white)
    pygame.display.update()

    pygame.draw.rect(controlpad, black, up, 3)
    pygame.draw.rect(controlpad, black, down, 3)
    pygame.draw.rect(controlpad, black, left, 3)
    pygame.draw.rect(controlpad, black, right, 3)

    speed = input('Enter a speed for the motors (0-5): ')

    running = True
    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                motor_control(press_handle(keys), speed_value=255/6 * (int(speed) + 1))  
            else:
                refresh()
    s.close()
    pygame.quit()

if __name__ == "__main__":
    main()