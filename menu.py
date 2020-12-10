from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from circuit_generator import generate_game
from  gameWindow import  *



start = False

Circuits = None
Plays = None
no_qubits = None
no_rounds = None
current_round = 0
unveil = False
display_empty = False
demo = False

class Window(QWidget):

    def __init__(self):
        super().__init__()

        # param
        self.roundNumber = 0
        self.qBitsNumber = 0
        self.isGameStarted = False
        self.game = None

        # lineEdit
        self.roundNumberEdit = QLineEdit()
        self.qbitsNumberEdit = QLineEdit()

        self.roundNumberEdit.setValidator(QIntValidator())
        self.qbitsNumberEdit.setValidator(QIntValidator())

        self.initUI()
        # show
        # self.show()

    def initUI(self):
        # label
        roundNumber = QLabel("Nombre de round")
        qbitsNumber = QLabel("Nombre QBits")
        imageLabel = QLabel()

        # image
        pixmap = QPixmap('poker.jpg')
        imageLabel.setPixmap(pixmap)

        # Button
        quitButton = QPushButton("Quit")
        startButton = QPushButton("Start")

        # Grid
        grid = QGridLayout()
        grid.setSpacing(10)

        # adding Widget
        grid.addWidget(roundNumber, 8, 8)
        grid.addWidget(self.roundNumberEdit, 8, 9)
        grid.addWidget(qbitsNumber, 7, 8)
        grid.addWidget(self.qbitsNumberEdit, 7, 9)
        grid.addWidget(startButton, 9, 8)
        grid.addWidget(quitButton, 9, 9)
        grid.addWidget(imageLabel, 0, 0, 7, 10)

        # onClick
        startButton.clicked.connect(self.onClickStart)
        quitButton.clicked.connect(self.onClickQuit)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PokerQuantum Menu')

        self.show()

    def onClickStart(self):
        # self.roundNumber = self.roundNumberEdit.text()
        # self.qBitsNumber = self.qbitsNumberEdit.text()

        self.setRoundNumber(self.roundNumberEdit.text())
        self.setQBitsNumber(self.qbitsNumberEdit.text())

        #On Charge le jeu
        while not start:
            Circuits, Plays = generate_game(int(self.qBitsNumber), int(self.qBitsNumber), demo=demo)
            start = True

        if not self.isGameStarted:
            self.game = GameWindow(self.roundNumber, self.qBitsNumber, Plays, Circuits)
        self.showGame()

    def getRoundNumber(self):
        return self.roundNumber

    def getQBitsNumber(self):
        return self.qBitsNumber

    def setRoundNumber(self, roundNumber):
        self.roundNumber = roundNumber

    def setQBitsNumber(self, qBitsNumber):
        self.qBitsNumber = qBitsNumber

    def onClickQuit(self):
        #self.hide()
        self.close()

    def showGame(self):
        self.game.show()



def create_menu():
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()
    # start the app

    app.exec()
