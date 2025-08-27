import pygame
import Grid
import Paddle
import keyboard

height = 5
width = 10
imgWidth = 800
imgHeight = 800
paddleStart = 1
paddleLength = height - 2*paddleStart
running = True

paddle = Paddle.Paddle(paddleLength,paddleStart)
grid = Grid.Grid(width, height, imgWidth, imgHeight, paddle)

# grid.makeGrid()
# pygame.init()


while running:
    if keyboard.is_pressed("q"):
        running = False
    elif keyboard.is_pressed("up"):
        paddle.move("up")
        print("up")
    elif keyboard.is_pressed("down"):
        paddle.move("down")
        print("down")
    else:
        print("not a recognized key")         

# grid.deleteGrid()
