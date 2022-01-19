import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QTimer

class Kwadrat(QRect):
    def __init__(self,x_cord, y_cord,a,b):
        super().__init__(y_cord * 10,x_cord * 10,a,b)

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
    def __init__(self,boardMatrix,method):
        super().__init__()
        self.boardMatrix=boardMatrix
        self.method = method
        self.setTimer(1000)
        self.show()
        self.pusher = 0
        
        print("__init__ test")

    def setTimer(self,interval):
        self.Timer = QTimer()
        if self.method == 0:
            self.Timer.timeout.connect(self.timerEvent)
        else:
            self.x = 0
            self.y = 0
            self.Timer.timeout.connect(self.changeBoardPartial)     
        self.Timer.setInterval(interval)
        self.Timer.start()
    
    def timerEvent(self):
        self.changeBoardFull()    
        self.repaint()

    def changeBoardFull(self):
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

    def changeBoardPartial(self):
        if self.x < (len(self.boardMatrix)-1):
            if self.y < (len(self.boardMatrix[0])-1):
                if self.pusher == 1:
                    if self.boardMatrix[self.x][0] == 1 and self.boardMatrix[self.x+1][0] == 0:
                        self.boardMatrix[self.x][0] = 0
                        self.boardMatrix[self.x+1][0] = 1
                self.Margolus(self.x,self.y)
                self.y = self.y+2
                if self.y == (len(self.boardMatrix[0])-1):
                    if self.boardMatrix[self.x][self.y] == 1 and self.boardMatrix[self.x+1][self.y] == 0:
                        self.boardMatrix[self.x][self.y] = 0
                        self.boardMatrix[self.x+1][self.y] = 1
            else:
                self.y = self.pusher            
                self.x = self.x + 2    
        else:
            if self.pusher == 0:
                self.pusher = 1
            else:
                self.pusher = 0
            self.x = self.pusher
        self.repaint()
        
        

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
                qp.drawRect(Kwadrat(CurrentRectangle.x_cord+10,CurrentRectangle.y_cord+10,10,10))
                CurrentRectangle.incrCordY()
            CurrentRectangle.zeroY()  
            CurrentRectangle.incrCordX()    
        if self.method == 1:
            kolor = QColor(0,0,0)
            kolor.setAlpha(0)
            qp.setBrush(kolor)
            qp.setPen(QColor(255,0,0))
            qp.drawRect(Kwadrat(self.x+10,self.y+10,20,20))
            kolor.setAlpha(255)
            qp.setBrush(kolor)
            qp.setPen(QColor(255,255,255))
app = QApplication(sys.argv)
boardMatrix = []
Sandfile = open('sand.txt')
for line in Sandfile:
    line = line.split('\n')[0]
    newline = []
    for x in line.split(','):
        newline.append(int(x))
    boardMatrix.append(newline)
print(boardMatrix)
mainWindow = MainWindow(boardMatrix,1)
mainWindow.resize(700, 700)
mainWindow.move(100, 100)
mainWindow.setWindowTitle('Piasek')
mainWindow.show()
#boardMatrix = [[1,1,1],[1,1,1],[1,1,1]]
#boardMatrix = [[0,0,1],[-1,0,-1],[1,-1,1]]
#boardMatrix = [[0,0,1],[0,0,0],[0,0,0]]
sys.exit(app.exec_())                