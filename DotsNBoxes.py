from random import *
import collections
from Algorithm import *
from Board import *
from Nodes import *


class DotsNBoxes: 
    def __init__(self, Board_Xdim, Board_Ydim, Ply_num):
        currentState = Game([], Board_Xdim, Board_Ydim)
        currentState.Initiate()
        self.State = Thing(currentState)
        self.Ply_num = Ply_num
        self.Score = 0

    def Human(self):
        self.State.Draw()

        HumanX = int(input("Please enter the 'X' coordinate of your choice (an integer such as 4): "))
        HumanY = int(input("Please enter the 'Y' coordinate of your choice (an integer such as 4): "))
        if (HumanX, HumanY) not in self.State.children:
            self.State.Make(HumanX, HumanY, False)
            self.State = self.State.children[(HumanX, HumanY)]
        else:
            self.State = self.State.children[(HumanX, HumanY)]

        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore),end ="\n\n\n")

        self.Computer()


    def Computer(self): 
        self.State.Draw()

        move = Algo.miniMax(self.State, self.Ply_num)

        self.State = self.State.children[(move[0], move[1])]

        print("AI selected the following coordinates to play:\n" + "(" ,str(move[0]), ", " + str(move[1]), ")", end = "\n\n")

        print("Current Score =====>> Your Score - AI Score = " + str(self.State.CurrentScore), end = "\n\n\n")

        if len(self.State.children) == 0:
            self.State.Draw()
            self.Evaluation()
            return

        self.Human()

    def Evaluation(self): 
        print("Stop this Madness!!!\n")
        if self.State.CurrentScore > 0:
            print("You won you crazy little unicorn!! You are the new hope for the mankind!")
            exit()
        elif self.State.CurrentScore < 0:
            print("!!! Inevitable Doom!!! You were crushed by the AI!! ")
            exit()
        else:
            print("Draw! Well Congratulations! you are as smart as the AI!")
            exit()

    def start(self):
        self.Human()
