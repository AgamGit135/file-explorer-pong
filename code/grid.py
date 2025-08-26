from PIL import Image
import os

def init(width, height, imgWidth,imgHeight):
    for i in range(height):
        for j in range(1,width + 1):
            n = i*width + j-1
            makeWhite(imgWidth,imgHeight,n)


def makeWhite(imgWidth,imgHeight,n):
    img = Image.new("RGB",(imgWidth,imgHeight),(255,255,255))
    # there must be a better way to do this
    name = "img" + str(n) + ".jpg"
    # save to relative path
    img.save(os.path.join("pong",name))
