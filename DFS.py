from Solver import Solver
import queue
import time
import copy
import random
import pygame
play_time = 180

class DFS(Solver):
    def __init__(self,game):
        super().__init__(game)
        pygame.init()
        self.timex = copy.deepcopy(game.timex)
        print("timex is")
        print(self.timex)
        self.game.printStatus()

    def calculateMoves(self):
        # Calculate moves to get to food
        q = queue.LifoQueue()

        expanded = set()
        root = tuple(self.tempBodyLocations[0])
        currentVertex = [root,[],False]
        coordinatePathDict = {}
        q.put(currentVertex)

        while q.empty() == False:
            self.tempBodyLocations = copy.deepcopy(self.game.snake.bodyLocations)
            currentNode = q.get()
            coord = currentNode[0]
            actions = currentNode[1]

            for i in range(len(actions)):
                # self.drawTempState()
                self.updateTemp(actions[i])

            if self.isGoalState(coord):
                return actions

            if coord in coordinatePathDict.keys():
                if set(actions) in coordinatePathDict[coord]:
                    continue
                else:
                    currentPaths = coordinatePathDict[coord]
                    currentPaths.append(set(actions))
                    coordinatePathDict[coord] = currentPaths
            else:
                coordinatePathDict[coord] = [tuple(actions)]
            moves = self.getAvailableMoves(coord)
            random.shuffle(moves)
            for move in moves:
                # print(move)
                # Get new head coordinates of snake with the move
                newCoordinates = tuple(self.getCoordinates(coord,move))

                if newCoordinates not in expanded:
                    q.put([newCoordinates,actions+[move],False])

        print("NO SOLUTION FOUND")
        return None

    def refresh(self):
        self.game.generateFood()
        self.game.snake.bodySize += 1
        self.game.score += 1
        self.moves = []
        self.tempBodyLocations = self.game.snake.bodyLocations

    def run(self):
        while self.game.alive():
            # self.game.printStatus()
            moves = self.calculateMoves()
            self.timey = pygame.time.get_ticks()
            overTime = (self.timex + (play_time * 1000) <= self.timey)
            if (moves == None) or overTime:
                self.printState()
                print("Score is " + str(self.game.score))
                print()
                timed = self.timey - self.timex
                print("Time is " + str(timed / 1000) + " Seconds")
                print(self.game.score)
                print("GAME OVER")
                break
            self.setCurrentMoves(moves)
            self.animate()
            self.refresh()