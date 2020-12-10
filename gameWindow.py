
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from circuit_generator import *

WIDTH = 1000
HEIGHT = 800

start = False

Circuits = None
Plays = None
no_qubits = None
no_rounds = None
current_round = 0
unveil = False
display_empty = False
demo = False

class GameWindow(QWidget):

    roundNumber = 0
    qBitsNumber = 0
    Plays = None
    Circuits = None

    def __init__(self, roundNumber, qBitsNumber):
        super().__init__()
        self.roundNumber = roundNumber
        self.qBitsNumber = qBitsNumber

        #Button
        self.playerOneButton = QPushButton("Joueur 1")
        self.playerTwoButton = QPushButton("Joueur 2")


        print(f"Nombre de Round : {self.roundNumber} | Nombre de QBit :{self.qBitsNumber} \n")

        #Generate All Data
        # On Charge le jeu

        self.Circuits, self.Plays = generate_game(int(self.qBitsNumber), int(self.qBitsNumber), demo=demo)

        #StartGame
        self.initUi()

    def generateData(self):
        pass

    def openDialogPlayerOne(self):

        text, okPressed = QInputDialog.getText(self, "Selection du circuit", "Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

    def openDialogPlayerTwo(self):
        text, okPressed = QInputDialog.getText(self, "Selection du circuit", "Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)
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
        self.playerOneButton.clicked.connect(self.openDialogPlayerOne)
        self.playerOneButton.clicked.connect(self.openDialogPlayerTwo)

        grid.addWidget(circuitLabel,0,0,1,1)
        grid.addWidget(graphLabel,1,0,-1,5)
        grid.addWidget(self.playerOneButton,8,6)
        grid.addWidget(self.playerTwoButton, 8, 9)

        self.setLayout(grid)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('PokerQuantum Jeu')

        self.show()

