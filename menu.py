from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtGui

from circuit_generator import generate_game
from gameWindow import *

IMAGE_POKER = 'images/poker.jpg'
class Window(QWidget):

    def __init__(self):
        super().__init__()

        # param
        self.roundNumber = 0
        self.qBitsNumber = 0
        self.isGameStarted = False
        self.game = None

        self.styleSheet = """
        
        QPushButton{
            background-color : rgb(180,255,255);
            
        }
        
        """

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
        pixmap = QPixmap(IMAGE_POKER)
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

        self.setStyleSheet(self.styleSheet)
        self.setLayout(grid)
        self.setStyle(QStyleFactory.create('Fusion'))
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('PokerQuantum Menu')

        self.show()

    def onClickStart(self):
        self.setRoundNumber(self.roundNumberEdit.text())
        self.setQBitsNumber(self.qbitsNumberEdit.text())

        if not self.isGameStarted:
            self.game = GameWindow(self.roundNumber, self.qBitsNumber)
        self.showGame()

    def setRoundNumber(self, roundNumber):
        self.roundNumber = int(roundNumber)

    def setQBitsNumber(self, qBitsNumber):
        self.qBitsNumber = int(qBitsNumber)

    def onClickQuit(self):
        # self.hide()
        self.close()

    def showGame(self):
        self.game.show()


def create_menu():
    # create pyqt5 app
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = Window()

    # start the app
    app.exec()
