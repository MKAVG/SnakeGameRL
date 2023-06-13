from Directions import Directions
import numpy as np

class Snake:
    def __init__(self,rows,cols):
        self.directions = Directions()

        # Body Locations
        self.head = [int(cols/2),int(rows/2)]
        self.bodyLocations = [[int(cols/2),int(rows/2+1)]]
        self.bodySize = 3

        # Orientations
        self.bodyDirections= [self.directions.UP,self.directions.UP,self.directions.UP]
        self.turningPoints = {}

    def oppositeDirection(self):
        if self.bodyDirections[0] == self.directions.UP:
            return self.directions.DOWN
        elif self.bodyDirections[0] == self.directions.DOWN:
            return self.directions.UP
        elif self.bodyDirections[0] == self.directions.RIGHT:
            return self.directions.LEFT
        elif self.bodyDirections[0] == self.directions.LEFT:
            return self.directions.RIGHT

    def printSnake(self):
      #  print("Body:", self.bodyLocations)
        print("Score: ", self.bodySize)
       # print("Turning Points:", self.turningPoints)