
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

IMAGE_NAME = 'stage.png'
IMAGE_NAME_PRB = 'state_prb.png'

class GameWindow(QWidget):

    roundNumber = 0
    qBitsNumber = 0

    Plays = None
    Circuits = None

    choicePlayerOne = ""
    choicePlayerTwo = ""

    hand_0 = ""
    hand_1 = ""

    state = None

    def __init__(self, roundNumber, qBitsNumber):
        super().__init__()
        self.roundNumber = int(roundNumber)
        self.qBitsNumber = int(qBitsNumber)

        #Button
        self.playerOneButton = QPushButton("Joueur 1")
        self.playerTwoButton = QPushButton("Joueur 2")
        self.play = QPushButton("Play !")

        print(f"Nombre de Round : {self.roundNumber} | Nombre de QBit :{self.qBitsNumber} \n")

        #Generate All Data
        # On Charge le jeu
        #StartGame

        self.initUi()

    def generateGame(self):
        pass

    def onClickPlay(self):
        self.roundNumber -= 1
        print(self.roundNumber)
        if self.roundNumber == 0 :
            print("FINI  !")



    def openDialogPlayerOne(self):

        hand_0_str = '  '.join(['%s: %s   ' % (key, value) for (key, value) in self.hand_0.items()])
        self.choicePlayerOne, okPressed = QInputDialog.getText(self, "Selection du circuit", hand_0_str, QLineEdit.Normal, "")
        if okPressed and self.choicePlayerOne != '':
            print(self.choicePlayerOne.upper())

    def openDialogPlayerTwo(self):

        hand_1_str = '  '.join(['%s: %s   ' % (key, value) for (key, value) in self.hand_1.items()])
        self.choicePlayerTwo, okPressed = QInputDialog.getText(self, "Selection du circuit", hand_1_str, QLineEdit.Normal, "")
        if okPressed and  self.choicePlayerTwo != '':
            print(self.choicePlayerTwo.upper())

    def updateGame(self):

        self.Plays = play_round(current_round, self.Plays, self.choicePlayerOne, self.choicePlayerTwo)
        draw_game(self.Circuits, self.Plays, unveil=unveil, display_empty=display_empty)
        init_circuit = get_played_game(self.Circuits, self.Plays)
        self.state = compute_state(init_circuit)

    def initUi(self):

        start = False

        self.Circuits, self.Plays = generate_game(int(self.qBitsNumber), int(self.roundNumber), demo=demo)
        draw_game(self.Circuits, self.Plays, unveil=unveil, display_empty=display_empty)
        self.hand_0, self.hand_1 = distribute_cards(int(self.roundNumber), demo=demo)
        init_circuit = get_played_game(self.Circuits, self.Plays)
        self.state = compute_state(init_circuit)
        state_draw(self.state)

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

        #button action
        self.playerOneButton.clicked.connect(self.openDialogPlayerOne)
        self.playerTwoButton.clicked.connect(self.openDialogPlayerTwo)
        self.play.clicked.connect(self.onClickPlay)

        #addingWidget
        grid.addWidget(circuitLabel,0,0,1,1)
        grid.addWidget(graphLabel,1,0,-1,5)
        grid.addWidget(self.playerOneButton,8,6)
        grid.addWidget(self.playerTwoButton, 8, 9)
        grid.addWidget(self.play,9,6,1,6)

        self.setLayout(grid)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('PokerQuantum Jeu')

        ##Game


        self.show()

