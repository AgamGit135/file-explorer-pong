
class Paddle:

    def __init__(self,paddleLength,paddleStart):
        self.length = paddleLength
        self.start = paddleStart
        self.end = self.start + self.length
    
    def move(self, dir):
        pass