import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QTimer, QTimerEvent

class Kwadrat(QRect):
    def __init__(self,x_cord, y_cord):
        super().__init__(x_cord * 10,y_cord * 10,10,10)

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
        Timer = QTimer()
        Timer.setInterval(1000)
        Timer.start()
        self.show()
    
    def timerEvent(self,event):
        self.repaint()
    
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
                elif y_cord == 1:
                    qp.setBrush(QColor(0, 0, 0))
                elif y_cord == -1:
                    qp.setBrush(QColor(79, 70, 50))    
                qp.drawRect(Kwadrat(CurrentRectangle.x_cord,CurrentRectangle.y_cord))
                CurrentRectangle.incrCordY()
            CurrentRectangle.zeroY()  
            CurrentRectangle.incrCordX()    
app = QApplication(sys.argv)
boardMatrix = [[0,0,1],[1,0,0],[1,-1,1]]
mainWindow = MainWindow(boardMatrix)
mainWindow.resize(700, 700)
mainWindow.move(100, 100)
mainWindow.setWindowTitle('Piasek')
mainWindow.show()
boardMatrix = [[1,1,1],[1,1,1],[1,-1,1]]
boardMatrix = [[0,0,1],[-1,0,-1],[1,-1,1]]
boardMatrix = [[0,0,1],[0,0,0],[0,0,0]]
sys.exit(app.exec_())                