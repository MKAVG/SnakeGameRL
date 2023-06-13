from Game import SnakeGame
from DFS import DFS
from BFS import BFS

if __name__ == "__main__":
    snakeGame = SnakeGame(rows=20, cols=20)
    #bfsSolver = BFS(snakeGame).run()
    dfsSolver = DFS(snakeGame).run()