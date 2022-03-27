from turtle import Screen, Turtle
import random
import time

class Game(Screen):

    def __init__(self):
        super().__init__()
        self.title("Game")
        self.setup(600, 600)
        self.bg('black')
    
        