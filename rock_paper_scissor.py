from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    rock_image = "rock image.JPG"
    paper_image = "paper image.JPG"
    scissor_image = "scissor image.JPG"

    choices = ["r","p","s"]
    chances = 10
    user_points = 0
    comp_points = 0
    comp_image = None

    detailStatement = "Welcome to Rock-Paper-Scissors Game\nPlease click any button to start"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 752)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(10, 10, 771, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.headingLabel.setFont(font)
        self.headingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headingLabel.setObjectName("headingLabel")

        self.compLabel = QtWidgets.QLabel(self.centralwidget)
        self.compLabel.setGeometry(QtCore.QRect(20, 140, 231, 221))
        self.compLabel.setText("")
        self.compLabel.setPixmap(QtGui.QPixmap("C:\\Users\\HP\\Codings\\Python\\Self_exercises\\Rock paper scissors\\Computer_image.png"))
        self.compLabel.setScaledContents(True)
        self.compLabel.setObjectName("compLabel")
        
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(540, 140, 231, 221))
        self.userLabel.setText("")
        self.userLabel.setPixmap(QtGui.QPixmap("C:\\Users\\HP\\Codings\\Python\\Self_exercises\\Rock paper scissors\\User_image.png"))
        self.userLabel.setScaledContents(True)
        self.userLabel.setObjectName("userLabel")

        self.chancesLabel = QtWidgets.QLabel(self.centralwidget)
        self.chancesLabel.setGeometry(QtCore.QRect(300, 150, 191, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.chancesLabel.setFont(font)
        self.chancesLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.chancesLabel.setObjectName("chancesLabel")

        self.rockButton = QtWidgets.QPushButton(self.centralwidget)
        self.rockButton.setGeometry(QtCore.QRect(270, 470, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rockButton.setFont(font)
        self.rockButton.setObjectName("rockButton")
        self.rockButton.clicked.connect(self.rock_click)

        self.paperButton = QtWidgets.QPushButton(self.centralwidget)
        self.paperButton.setGeometry(QtCore.QRect(440, 470, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.paperButton.setFont(font)
        self.paperButton.setObjectName("paperButton")
        self.paperButton.clicked.connect(self.paper_click)

        self.scissorButton = QtWidgets.QPushButton(self.centralwidget)
        self.scissorButton.setGeometry(QtCore.QRect(610, 470, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.scissorButton.setFont(font)
        self.scissorButton.setObjectName("scissorButton")
        self.scissorButton.clicked.connect(self.scissor_click)

        self.detailLabel = QtWidgets.QLabel(self.centralwidget)
        self.detailLabel.setGeometry(QtCore.QRect(10, 540, 771, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detailLabel.setFont(font)
        self.detailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.detailLabel.setObjectName("detailLabel")

        self.compPoints = QtWidgets.QLabel(self.centralwidget)
        self.compPoints.setGeometry(QtCore.QRect(20, 380, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.compPoints.setFont(font)
        self.compPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.compPoints.setObjectName("compPoints")

        self.userPoints = QtWidgets.QLabel(self.centralwidget)
        self.userPoints.setGeometry(QtCore.QRect(540, 380, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.userPoints.setFont(font)
        self.userPoints.setAlignment(QtCore.Qt.AlignCenter)
        self.userPoints.setObjectName("userPoints")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @classmethod
    def change_user_points(cls):
        cls.detailStatement = "You got a Point !!!"
        cls.user_points = cls.user_points + 1

    @classmethod
    def change_comp_points(cls):
        cls.detailStatement = "Computer won a Point !!!"
        cls.comp_points = cls.comp_points + 1
    
    @classmethod
    def drawStatement(cls):
        cls.detailStatement = "Thats a Draw !!!"

    @classmethod
    def change_chances(cls):
        cls.chances = cls.chances - 1
        if cls.chances == 0 :
            if cls.user_points > cls.comp_points :
                cls.detailStatement = "You won against the computer !!!"
            elif cls.user_points < cls.comp_points :
                cls.detailStatement = "You Lose to the computer !!!"
            else :
                cls.detailStatement = "Its a Draw Game"
        elif cls.chances < 0 :
            quit()

    def update(self):
        self.retranslateUi(MainWindow)

    def computer_choice(self):
        comp_choice = random.choice(self.choices)
        if comp_choice == "r":
            self.comp_image = self.rock_image
        elif comp_choice == "p":
            self.comp_image = self.paper_image
        else :
            self.comp_image = self.scissor_image
        return self.comp_image

    def rock_click(self):
        self.compChoice = self.computer_choice()
        self.compLabel.setPixmap(QtGui.QPixmap(self.compChoice))
        self.userLabel.setPixmap(QtGui.QPixmap(self.rock_image))

        if self.compChoice == self.rock_image :
            self.drawStatement()
        elif self.compChoice == self.paper_image :
            self.change_comp_points()
        else :
            self.change_user_points()

        self.change_chances()
        self.update()
        print(self.chances)

    def paper_click(self):
        self.compChoice = self.computer_choice()
        self.compLabel.setPixmap(QtGui.QPixmap(self.compChoice))
        self.userLabel.setPixmap(QtGui.QPixmap(self.paper_image))

        if self.compChoice == self.rock_image :
            self.change_user_points()
        elif self.compChoice == self.paper_image :
            self.drawStatement()
        else :
            self.change_comp_points()

        self.change_chances()
        self.update()
        print(self.chances)
        
    def scissor_click(self):
        self.compChoice = self.computer_choice()
        self.compLabel.setPixmap(QtGui.QPixmap(self.compChoice))
        self.userLabel.setPixmap(QtGui.QPixmap(self.scissor_image))

        if self.compChoice == self.rock_image :
            self.change_comp_points()
        elif self.compChoice == self.paper_image:
            self.change_user_points()
        else :
            self.drawStatement()

        self.change_chances()
        self.update()
        print(self.chances)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headingLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Rock Paper Scissors</span></p></body></html>"))
        self.chancesLabel.setText(_translate("MainWindow", f"Chances Left :\n{self.chances}"))
        self.rockButton.setText(_translate("MainWindow", "Rock"))
        self.paperButton.setText(_translate("MainWindow", "Paper"))
        self.scissorButton.setText(_translate("MainWindow", "Scissors"))
        self.detailLabel.setText(_translate("MainWindow", f"{self.detailStatement}"))
        self.compPoints.setText(_translate("MainWindow", f"Points : {self.comp_points}"))
        self.userPoints.setText(_translate("MainWindow", f"Points : {self.user_points}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
