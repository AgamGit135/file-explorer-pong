from PIL import Image
import Grid
import Paddle

height = 5
width = 10
imgWidth = 800
imgHeight = 800
paddleStart = 1
paddleLength = height - 2*paddleStart

paddle = Paddle.Paddle(paddleLength,paddleStart)
grid = Grid.Grid(width, height, imgWidth, imgHeight, paddle)

grid.makeGrid()