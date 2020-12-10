
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

WIDTH = 1000
HEIGHT = 800

class GameWindow(QWidget):

    roundNumber = 0
    qBitsNumber = 0
    Plays = None
    Circuits = None

    def __init__(self, roundNumber, qBitsNumber, Plays, Circuits):
        super().__init__()
        self.roundNumber = roundNumber
        self.qBitsNumber = qBitsNumber
        self.Plays = Plays
        self.Circuits = Circuits

        print(f"Nombre de Round : {self.roundNumber} | Nombre de QBit :{self.qBitsNumber} \n")
        self.initUi()

    def initUi(self):

        #Grid
        grid = QGridLayout()
        grid.setSpacing(10)



        #label
        graphLabel = QLabel()
        circuitLabel = QLabel()

        # image
        pixMapPrb = QPixmap('state_prb.png').scaled(400,400,Qt.KeepAspectRatio)
        graphLabel.setPixmap(pixMapPrb)

        pixMapStage = QPixmap('stage.png')
        circuitLabel.setPixmap(pixMapStage)

        #button
        playerOneButton = QPushButton("Joueur 1")
        playerTwoButton = QPushButton("Joueur 2")

        grid.addWidget(circuitLabel,0,0,1,1)
        grid.addWidget(graphLabel,1,0,-1,5)
        grid.addWidget(playerOneButton,8,6)
        grid.addWidget(playerTwoButton, 8, 9)

        self.setLayout(grid)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('PokerQuantum Jeu')

        self.show()
