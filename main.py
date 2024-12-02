# This Python file uses the following encoding: utf-8
import sys
import time
import random
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

# GAME SETTINGS and Global Variables

# track which objects are in each slot
starSlot = None
circleSlot = None
triangleSlot = None
squareSlot = None

# current shape and color being prompted
promptObject = None

# general settings
shapeNumber = None
colorNumber = None
timePerRound = None
totalPrompts = None

# shape IDs
redStar = None
redCircle = None
redTriangle = None
redSquare = None

yellowStar = None
yellowCircle = None
yellowTriangle = None
yellowSquare = None

greenStar = None
greenCircle = None
greenTriangle = None
greenSquare = None

blueStar = None
blueCircle = None
blueTriangle = None
blueSquare = None

redList = redStar, redCircle, redTriangle, redSquare
yellowList = yellowStar, yellowCircle, yellowTriangle, yellowSquare
greenList = greenSquare, greenCircle, greenTriangle, greenSquare
blueList = blueStar, blueCircle, blueTriangle, blueSquare

starList = redStar, yellowStar, greenStar, blueStar
circleList = redCircle, yellowCircle, greenCircle, blueCircle
triangleList = redTriangle, yellowTriangle, greenTriangle, blueTriangle
squareList = redSquare, yellowSquare, greenSquare, blueSquare

shapeListConst = [0,1,2,3]
colorListConst = [0,1,2,3]

shapeListPool = [0]
colorListPool = [0]

# SHAPES:
# 0 = Star
# 1 = Circle
# 2 = Triangle
# 3 = Square

# COLORS:
# 0 = Red
# 1 = Yellow
# 2 = Green
# 3 = Blue


class SettingsWidget(QWidget):
    def __init__(self):
        super().__init__() 

        programRunning = True

        # Settings Menu Start Button
        self.SettingsStartButton = QPushButton("Start Game")
        self.SettingsStartButton.setFixedSize(100, 50)
        self.SettingsStartButton.move(350,350)
        self.SettingsStartButton.show()
        self.SettingsStartButton.setParent(self)
        


        # Settings Menu Slider 1 - number of shapes
        self.ShapeSlider = QSlider(parent=self) #initialize slider
        self.ShapeSlider.setRange(1,4)  #set range of slider
        self.ShapeSlider.show() #enable disp
        self.ShapeSlider.move(100,100)   #move to appropriate spot in window
        self.ShapeSlider.resize(200,50) #change size
        self.ShapeSlider.setTickInterval(4) #set amount of intervals
        self.ShapeSlider.setSliderPosition(1)   #set base position
        self.ShapeSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 1 - number of shapes
        self.ShapeLabel = QLabel("Number of Shapes: 1")
        self.ShapeLabel.setFixedSize(150,25)
        self.ShapeLabel.move(150,25)
        self.ShapeLabel.show()
        self.ShapeLabel.setParent(self)

        # Settings Menu Slider 1 - End Labels ('1' and '4')
        self.ShapeLabelLeft = QLabel("1")
        self.ShapeLabelLeft.setFixedSize(50,50)
        self.ShapeLabelLeft.move(75,70)
        self.ShapeLabelLeft.show()
        self.ShapeLabelLeft.setParent(self)
        self.ShapeLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ShapeLabelRight = QLabel("4")
        self.ShapeLabelRight.setFixedSize(50,50)
        self.ShapeLabelRight.move(310,70)
        self.ShapeLabelRight.show()
        self.ShapeLabelRight.setParent(self)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # Settings Menu Slider 2 - number of colors 1 - 4 (increments of 1)
        self.ColorSlider = QSlider(parent=self) #initialize slider
        self.ColorSlider.setRange(1,4)  #set range of slider
        self.ColorSlider.show() #enable disp
        self.ColorSlider.move(500,100)   #move to appropriate spot in window
        self.ColorSlider.resize(200,50) #change size
        self.ColorSlider.setTickInterval(4) #set amount of intervals
        self.ColorSlider.setSliderPosition(1)   #set base position
        self.ColorSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 2 - number of colors
        self.ColorLabel = QLabel("Number of Colors: 1")
        self.ColorLabel.setFixedSize(150,25)
        self.ColorLabel.move(525, 25)
        self.ColorLabel.show()
        self.ColorLabel.setParent(self)

        # Settings Menu Slider 2 - End Labels ('1' and '4')
        self.ColorLabelLeft = QLabel("1")
        self.ColorLabelLeft.setFixedSize(50,50)
        self.ColorLabelLeft.move(475,70)
        self.ColorLabelLeft.show()
        self.ColorLabelLeft.setParent(self)
        self.ColorLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ColorLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ColorLabelRight = QLabel("4")
        self.ColorLabelRight.setFixedSize(50,50)
        self.ColorLabelRight.move(710,70)
        self.ColorLabelRight.show()
        self.ColorLabelRight.setParent(self)
        self.ColorLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ColorLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # Settings Menu Slider 3 - time per prompt - 30s - 120s (increments of 15s) --> next tick after 120s is 'no limit'
        self.TimerSlider = QSlider(parent=self) #initialize slider
        self.TimerSlider.setRange(30,120)  #set range of slider
        self.TimerSlider.show() #enable disp
        self.TimerSlider.move(100,325)   #move to appropriate spot in window
        self.TimerSlider.resize(200,50) #change size
        self.TimerSlider.setTickInterval(9) #set amount of intervals
        self.TimerSlider.setSliderPosition(30)   #set base position
        self.TimerSlider.setSingleStep(15)
        self.TimerSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 3 - time per prompt
        self.TimerLabel = QLabel("Time Per Round: 30 sec")
        self.TimerLabel.setFixedSize(150,25)
        self.TimerLabel.move(150,250)
        self.TimerLabel.show()
        self.TimerLabel.setParent(self)

        # Settings Menu Slider 3 - End Labels ('1' and '4')
        self.TimerLabelLeft = QLabel("30 Sec")
        self.TimerLabelLeft.setFixedSize(50,50)
        self.TimerLabelLeft.move(75, 295)
        self.TimerLabelLeft.show()
        self.TimerLabelLeft.setParent(self)
        self.TimerLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TimerLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.TimerLabelRight = QLabel("No Limit")
        self.TimerLabelRight.setFixedSize(50,50)
        self.TimerLabelRight.move(310,295)
        self.TimerLabelRight.show()
        self.TimerLabelRight.setParent(self)
        self.TimerLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TimerLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # Settings Menu Slider 4 - number of prompts - 3 - 10 (increments of 1)
        self.PromptSlider = QSlider(parent=self) #initialize slider
        self.PromptSlider.setRange(3,10)  #set range of slider
        self.PromptSlider.show() #enable disp
        self.PromptSlider.move(500,325)   #move to appropriate spot in window
        self.PromptSlider.resize(200,50) #change size
        self.PromptSlider.setTickInterval(8) #set amount of intervals
        self.PromptSlider.setSliderPosition(1)   #set base position
        self.PromptSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 4 - number of prompts
        self.PromptLabel = QLabel("Number of Rounds: 3")
        self.PromptLabel.setFixedSize(150,25)
        self.PromptLabel.move(525, 250)
        self.PromptLabel.show()
        self.PromptLabel.setParent(self)

        # Settings Menu Slider 4 - End Labels ('3' and '10')
        self.PromptLabelLeft = QLabel("3")
        self.PromptLabelLeft.setFixedSize(50,50)
        self.PromptLabelLeft.move(475, 295)
        self.PromptLabelLeft.show()
        self.PromptLabelLeft.setParent(self)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.PromptLabelRight = QLabel("10")
        self.PromptLabelRight.setFixedSize(50,50)
        self.PromptLabelRight.move(710, 295)
        self.PromptLabelRight.show()
        self.PromptLabelRight.setParent(self)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)
            
        def updateShapeLabel():
            self.ShapeLabel.setText("Number of Shapes: " + str(self.ShapeSlider.value()))

        def updateColorLabel():
            self.ColorLabel.setText("Number of Shapes: " + str(self.ColorSlider.value()))
            
        def updateTimerLabel():
            if (self.TimerSlider.value() < 120):
                self.TimerLabel.setText("Timer per Round: " + str(self.TimerSlider.value()) + " sec")    
            else:
                self.TimerLabel.setText("Timer per Round: No Limit")

        def updatePromptLabel():
            self.PromptLabel.setText("Number of Rounds: " + str(self.PromptSlider.value()))

        self.ShapeSlider.valueChanged.connect(updateShapeLabel)
        self.ColorSlider.valueChanged.connect(updateColorLabel)
        self.TimerSlider.valueChanged.connect(updateTimerLabel)
        self.PromptSlider.valueChanged.connect(updatePromptLabel)

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.starImage = QLabel(parent=self)
        self.circleImage = QLabel(parent=self)
        self.triangleImage = QLabel(parent=self)
        self.squareImage = QLabel(parent=self)

        self.debug_button = QPushButton("Next Prompt (Debug)")
        
        self.colorStar = QPixmap("./grayStar.png")
        self.colorStar2 = self.colorStar.scaled(100,100)
        self.starImage.setPixmap(self.colorStar2)
        self.starImage.show()
        self.starImage.setFixedSize(150,150)
        self.starImage.move(125,37.5)

        self.colorCircle = QPixmap("./grayCircle.png")
        self.colorCircle2 = self.colorCircle.scaled(100,100)
        self.circleImage.setPixmap(self.colorCircle2)
        self.circleImage.show()
        self.circleImage.setFixedSize(150,150)
        self.circleImage.move(525,37.5)

        self.colorTriangle = QPixmap("./grayTriangle.png")
        self.colorTriangle2 = self.colorTriangle.scaled(100,100)
        self.triangleImage.setPixmap(self.colorTriangle2)
        self.triangleImage.show()
        self.triangleImage.setFixedSize(150,150)
        self.triangleImage.move(125,225)

        self.colorSquare = QPixmap("./graySquare.png")
        self.colorSquare2 = self.colorSquare.scaled(100,100)
        self.squareImage.setPixmap(self.colorSquare2)
        self.squareImage.show()
        self.squareImage.setFixedSize(150,150)
        self.squareImage.move(525,225)

        # generates a new random shape and color
        def newPrompt():
            global shapeListPool
            global colorListPool

            global redList
            global yellowList
            global greenList
            global blueList

            global starList
            global circleList
            global triangleList
            global squareList

            randomColor = shapeListPool[random.randint(0,len(shapeListPool)-1)]
            randomShape = colorListPool[random.randint(0,len(colorListPool)-1)]

            print("-----------------")
            if (randomColor == 0):
                print("Color: Red")
            elif (randomColor == 1):
                print("Color: Yellow")
            elif (randomColor == 2):
                print("Color: Green")
            elif (randomColor == 3):
                print("Color: Blue")

            if (randomShape == 0):
                print("Shape: Star")
            elif (randomShape == 1):
                print("Shape: Circle")
            elif (randomShape == 2):
                print("Shape: Triangle")
            elif (randomShape == 3):
                print("Shape: Square")


        def read_RFID_daemon():
            print("test")


        def checkSlot(slot):
            print("test")
            # shape IDs
            global starSlot
            global circleSlot
            global triangleSlot
            global squareSlot

            global redStar
            global redCircle
            global redTriangle
            global redSquare

            global yellowStar
            global yellowCircle
            global yellowTriangle
            global yellowSquare

            global blueStar
            global blueCircle
            global blueTriangle
            global blueSquare

            global greenStar
            global greenCircle
            global greenTriangle
            global greenSquare
        
        self.debug_button.clicked.connect(newPrompt)

    

class WindowSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Manager
        # Make an instance of the settings menu
        self.Settings = SettingsWidget()
        self.Settings.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.Settings.show()

        # Make an instance of the game menu
        self.Game = GameWidget()
        self.Game.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.Game.hide() 

        def StartGame():

            # hide settings menu, show game menu, grab appropriate globals and constants to set up the game with
            print("--Test 1--")
            programRunning = True
            self.Game.show()
            self.Settings.hide()

            global shapeListConst
            global colorListConst

            global shapeListPool
            global colorListPool

            tempColorList = colorListConst
            tempShapeList = shapeListConst

            global shapeNumber
            global colorNumber
            global timePerRound
            global totalPrompts

            colorNumber = self.Settings.ColorSlider.value()
            shapeNumber = self.Settings.ShapeSlider.value()
            totalPrompts = self.Settings.PromptSlider.value()
            timePerRound = self.Settings.TimerSlider.value()

            tempColor = random.randint(0,3)
            tempShape = random.randint(0,3)

            print("Number of Colors: ", colorNumber)
            print("Numnber of Shapes: ", shapeNumber)
            print("Time Per Round: ", timePerRound)
            print("Number of Rounds: ", totalPrompts)

            

            #print("\nColors Options:")
            #for i in colorListPool:
            #    print(colorListPool[i])

            #print("\nShape Options:")
            #for i in shapeListPool:
            #    print(shapeListPool[i])



        def EndGame():
            print("--Test 2--")
            programRunning = False
            self.Game.hide()
            self.Settings.show()

        self.Settings.SettingsStartButton.clicked.connect(StartGame)
        #self.Game.button1.clicked.connect(EndGame)

        

if __name__ == "__main__":
    app = QApplication([])
    
    window = WindowSystem()

    sys.exit(app.exec())
