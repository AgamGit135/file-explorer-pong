from PIL import Image
import os

class Grid:
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    def __init__(self,width,height,imgWidth,imgHeight,paddle):
        self.width = width
        self.height = height
        self.imgWidth = imgWidth
        self.imgHeight = imgHeight
        self.paddle = paddle

    def makeGrid(self):
        for i in range(self.height):
            for j in range(self.width):
                n = i*self.width + j
                if self.inPaddle(i,j):
                    self.makeImg(n,self.BLACK)
                else:
                    self.makeImg(n,self.WHITE)

    def makeImg(self,n,color):
        img = Image.new("RGB",(self.imgWidth,self.imgHeight),color)
        # there must be a better way to do this
        name = f"img{str(n)}.png"
        # save to relative path
        img.save(os.path.join("pong",name))

    def inPaddle(self,row, column):
        inRow = row > self.paddle.start and row < self.paddle.end
        inColumn = column == 0 or column == self.width - 1
        return inColumn and inRow
    
    def deleteGrid(self):
        for file in os.listdir("pong"):
            os.remove(f"pong/{file}")
