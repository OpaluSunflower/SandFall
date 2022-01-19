import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QTimer

class Kwadrat(QRect):
    def __init__(self,x_cord, y_cord):
        super().__init__(y_cord * 10,x_cord * 10,10,10)

#Klasa reprezentująca pozycję na planszy
class Position:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
    
    def incrCordX(self):
        self.x_cord +=1

    def incrCordY(self):
        self.y_cord +=1

    def zeroY(self):
        self.y_cord = 0        

class MainWindow(QWidget):
    def __init__(self,boardMatrix):
        super().__init__()
        self.boardMatrix=boardMatrix
        self.setTimer(1000)
        self.show()
        self.pusher = 0
        print("__init__ test")

    def setTimer(self,interval):
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.timerEvent)
        self.Timer.setInterval(interval)
        self.Timer.start()
    
    def timerEvent(self):
        self.changeBoard()
        self.repaint()

    def changeBoard(self):
        print(self.pusher)
        x = self.pusher
        while x < (len(self.boardMatrix)-1):
            print(x,'xxx')
            y = self.pusher
            while y < (len(self.boardMatrix[0])-1):
                if self.pusher == 1:
                    if self.boardMatrix[x][0] == 1 and self.boardMatrix[x+1][0] == 0:
                        self.boardMatrix[x][0] = 0
                        self.boardMatrix[x+1][0] = 1
                self.Margolus(x,y)
                y = y+2
                if y == (len(self.boardMatrix[0])-1):
                    if self.boardMatrix[x][y] == 1 and self.boardMatrix[x+1][y] == 0:
                        self.boardMatrix[x][y] = 0
                        self.boardMatrix[x+1][y] = 1
            x = x + 2    
        if self.pusher == 0:
            self.pusher = 1
        else:
            self.pusher = 0            


    def Margolus(self,x,y):
        if self.boardMatrix[x][y] == 1:
            if self.boardMatrix[x+1][y] == 0:
                self.boardMatrix[x][y] = 0
                self.boardMatrix[x+1][y] = 1
            elif self.boardMatrix[x][y+1] == 0:
                if self.boardMatrix[x+1][y+1] == 0:
                    self.boardMatrix[x][y] = 0
                    self.boardMatrix[x+1][y+1] = 1
        if self.boardMatrix[x][y+1] == 1:
            if self.boardMatrix[x+1][y+1] == 0:
                self.boardMatrix[x][y+1] = 0
                self.boardMatrix[x+1][y+1] = 1
            elif self.boardMatrix[x+1][y] == 0:
                if self.boardMatrix[x][y] == 0:
                    self.boardMatrix[x+1][y] = 1
                    self.boardMatrix[x][y+1] = 0


    
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        print("paintEvent test")
        self.refreshBoard(qp)
        qp.end()

    def refreshBoard(self,qp):
        CurrentRectangle = Position()   
        for x_cord in self.boardMatrix:
            for y_cord in x_cord:
                if y_cord == 0:
                    qp.setBrush(QColor(255, 255, 255))
                elif y_cord == -1:
                    qp.setBrush(QColor(0, 0, 0))
                elif y_cord == 1:
                    qp.setBrush(QColor(79, 70, 50))    
                qp.drawRect(Kwadrat(CurrentRectangle.x_cord+10,CurrentRectangle.y_cord+10))
                CurrentRectangle.incrCordY()
            CurrentRectangle.zeroY()  
            CurrentRectangle.incrCordX()    

app = QApplication(sys.argv)
boardMatrix = [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
mainWindow = MainWindow(boardMatrix)
mainWindow.resize(700, 700)
mainWindow.move(100, 100)
mainWindow.setWindowTitle('Piasek')
mainWindow.show()
#boardMatrix = [[1,1,1],[1,1,1],[1,1,1]]
#boardMatrix = [[0,0,1],[-1,0,-1],[1,-1,1]]
#boardMatrix = [[0,0,1],[0,0,0],[0,0,0]]
sys.exit(app.exec_())                