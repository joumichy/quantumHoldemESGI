
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

IMAGE_NAME = 'images/stage.png'
IMAGE_NAME_PRB = 'images/state_prb.png'

class GameWindow(QWidget):

    roundNumber = 0
    qBitsNumber = 0

    Plays = None
    Circuits = None

    choicePlayerOne = ""
    choicePlayerTwo = ""

    hand_0 = ""
    hand_1 = ""

    current_round = 0

    state = None

    def __init__(self, roundNumber, qBitsNumber):
        super().__init__()
        self.roundNumber = int(roundNumber)
        self.qBitsNumber = int(qBitsNumber)

        #stylesheet
        self.styleSheet = """
                
                background-color: rgb(200,200,200);
                
                QPushButton{
                    background-color : rgb(180,255,255);
                    width : 100%;
                    height : 50%;
                }
                
                QLabel{
                    border: 1rem solid;
                }
                
                """
        #Button
        self.playerOneButton = QPushButton("Joueur 1")
        self.playerTwoButton = QPushButton("Joueur 2")
        self.play = QPushButton("Play !")

        #Label
        self.graphLabel = QLabel()
        self.circuitLabel = QLabel()

        #Grid
        self.grid = QGridLayout()

        #StartGame
        self.setStyleSheet(self.styleSheet)
        self.initUi()



    def onClickPlay(self):

        #Mise à jour de la partie

        self.updateGame()
        self.updateHandsPlayers()
        self.current_round += 1

        #Dernier tour
        print(self.current_round)
        if self.roundNumber == self.current_round:
            final_circuit = get_played_game(self.Circuits, self.Plays)
            state_draw(self.state)
            self.state = compute_state(final_circuit)
            print("FINI  !")
            score_1 = int(score_counts(self.state))
            score_0 = 100 - score_1
            if score_1 < score_0 :

                QMessageBox.about(self, "Resultat", "Le vainqueur est : Joueur 1 | %s/100"%score_0)
            elif score_1 > score_0:

                QMessageBox.about(self, "Resultat", "Le vainqueur est : Joueur 2 | %s/100"%score_1)
            else :
                QMessageBox.about(self, "Resultat !", "Egalité !")

    #Mise à jour des 'Cartes'
    def updateHandsPlayers(self):
        if self.choicePlayerOne in self.hand_0:
            self.hand_0[self.choicePlayerOne] = self.hand_0[self.choicePlayerOne] - 1

        if self.choicePlayerTwo in self.hand_1:
            self.hand_1[self.choicePlayerTwo] = self.hand_1[self.choicePlayerTwo] - 1

    #Selection joueur 1
    def openDialogPlayerOne(self):

        hand_0_str = '  '.join(['%s: %s   ' % (key, value) for (key, value) in self.hand_0.items()])
        self.choicePlayerOne, okPressed = QInputDialog.getText(self, "Selection du circuit", hand_0_str, QLineEdit.Normal, "")
        if okPressed and self.choicePlayerOne != '':
            print(self.choicePlayerOne.upper())

    # Selection joueur 2
    def openDialogPlayerTwo(self):

        hand_1_str = '  '.join(['%s: %s   ' % (key, value) for (key, value) in self.hand_1.items()])
        self.choicePlayerTwo, okPressed = QInputDialog.getText(self, "Selection du circuit", hand_1_str, QLineEdit.Normal, "")
        if okPressed and  self.choicePlayerTwo != '':
            print(self.choicePlayerTwo.upper())

    #Mise à jour de la partie
    def updateGame(self):

        self.Plays = play_round(self.current_round, self.Plays, self.choicePlayerOne, self.choicePlayerTwo)
        draw_game(self.Circuits, self.Plays, unveil=unveil, display_empty=display_empty)
        init_circuit = get_played_game(self.Circuits, self.Plays)
        self.state = compute_state(init_circuit)
        state_draw(self.state)

        # image
        pixMapPrb = QPixmap(IMAGE_NAME_PRB).scaled(600, 400, Qt.KeepAspectRatio)
        self.graphLabel.setPixmap(pixMapPrb)

        pixMapStage = QPixmap(IMAGE_NAME).scaled(800,600, Qt.KeepAspectRatio)
        self.circuitLabel.setPixmap(pixMapStage)

        #Update Grid
        self.grid.addWidget(self.circuitLabel, 0, 0, 1, 1)
        self.grid.addWidget(self.graphLabel, 1, 0, -1, 5)

        self.show()

    #Generation des données
    def generateData(self):
        self.Circuits, self.Plays = generate_game(int(self.qBitsNumber), int(self.roundNumber), demo=demo)
        draw_game(self.Circuits, self.Plays, unveil=unveil, display_empty=display_empty)
        self.hand_0, self.hand_1 = distribute_cards(int(self.roundNumber), demo=demo)
        init_circuit = get_played_game(self.Circuits, self.Plays)
        self.state = compute_state(init_circuit)
        state_draw(self.state)

    #Generation interface graphique
    def initUi(self):

        self.generateData()

        # image
        pixMapPrb = QPixmap(IMAGE_NAME_PRB).scaled(600,400, Qt.KeepAspectRatio)
        self.graphLabel.setPixmap(pixMapPrb)
        pixMapStage = QPixmap(IMAGE_NAME).scaled(800,600, Qt.KeepAspectRatio)
        self.circuitLabel.setPixmap(pixMapStage)

        #button action
        self.playerOneButton.clicked.connect(self.openDialogPlayerOne)
        self.playerTwoButton.clicked.connect(self.openDialogPlayerTwo)
        self.play.clicked.connect(self.onClickPlay)

        #addingWidget
        # Grid
        self.grid.setSpacing(10)
        self.grid.addWidget(self.circuitLabel,0,0,1,1)
        self.grid.addWidget(self.graphLabel,1,0,-1,5)
        self.grid.addWidget(self.playerOneButton,8,6)
        self.grid.addWidget(self.playerTwoButton, 8, 9)
        self.grid.addWidget(self.play,9,6,1,6)

        self.setLayout(self.grid)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle('PokerQuantum Jeu')

        ##Game
        self.show()

