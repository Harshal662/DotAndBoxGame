from random import *

class Game: 
    def __init__(self, Mat, dimX, dimY):
        self.Mat = Mat
        self.dimX = dimX
        self.dimY = dimY

    def Initiate(self): 
        for i in range(0, self.dimY):
            R = []
            for j in range (0, self.dimX):
                if i % 2 == 1 and j % 2 == 1:
                    R.append(randint(1, 9))  
                elif i % 2 == 0 and j % 2 == 0:
                    R.append('*') 
                else:
                    R.append(' ') 
            self.Mat.append(R)

    def Get_matrix(self):
        ans = []
        for i in range(0, self.dimY):
            R = []
            for j in range(0, self.dimX):
                R.append(self.Mat[i][j])
            ans.append(R)
        return ans

    def Draw_mat(self):
        
        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX):
            print(str(i), end='  ')
        print()

        if self.dimX > 9:
            print(" ", end='')
        print("   ", end='')
        for i in range(0, self.dimX + 1):
            print("___", end='')
        print()
        for j in range(self.dimY):
            if self.dimX > 9 and j < 10:
                print(" ", end='')
            print(str(j) + "| ", end='')
            for z in range(self.dimX):
                print(str(self.Mat[j][z]), end='  ')
            print()
        print("   _________________________\n")

    def Get_currentState(self):
        return Game(self.Get_matrix(), self.dimX, self.dimY)

    def action(self, i, j):
        Sum = 0

        if(self.Mat[j][i]!=' ' or i>(self.dimX) or j>(self.dimY)):
            print("\nError!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            X = int(input("Please enter the 'X' coordinate of the blank space only: "))
            Y = int(input("Please enter the 'Y' coordinate of your blank space only: "))
            self.action(X,Y)

        if j % 2 == 0 and i % 2 == 1:
            self.Mat[j][i] = '-'
            if j < self.dimY - 1:
                if self.Mat[j+2][i] == '-' and self.Mat[j+1][i+1] == '|' and self.Mat[j+1][i-1] == '|':
                    Sum += self.Mat[j+1][i]
            if j > 0:
                if self.Mat[j-2][i] == '-' and self.Mat[j-1][i+1] == '|' and self.Mat[j-1][i-1] == '|':
                    Sum += self.Mat[j-1][i]

        elif(j%2==1 and i%2==0):
            self.Mat[j][i] = '|'
            if i < self.dimX - 1:
                if self.Mat[j][i+2] == '|' and self.Mat[j+1][i+1] == '-' and self.Mat[j-1][i+1] == '-':
                    Sum += self.Mat[j][i+1]
            if i > 0:
                if self.Mat[j][i-2] == '|' and self.Mat[j+1][i-1] == '-' and self.Mat[j-1][i-1] == '-':
                    Sum += self.Mat[j][i-1]        
        
        return Sum
