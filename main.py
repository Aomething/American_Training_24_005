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
promptObject = 0
promptColor = 0
promptShape = 0

# general settings
shapeNumber = None
colorNumber = None
timePerRound = None
totalPrompts = None

currentRound = 1
currentTimer = 0
useTimer = True

programRunning = False


# shape IDs
redStar = 16
redCircle = 1
redTriangle = 2
redSquare = 3

yellowStar = 4
yellowCircle = 5
yellowTriangle = 6
yellowSquare = 7

greenStar = 8
greenCircle = 9
greenTriangle = 10
greenSquare = 11

blueStar = 12
blueCircle = 13
blueTriangle = 14
blueSquare = 15

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
        self.SettingsStartButton.setFixedSize(150, 50)
        self.SettingsStartButton.move(325,300)
        self.SettingsStartButton.show()
        self.SettingsStartButton.setParent(self)
        self.testFont = self.SettingsStartButton.font()
        self.testFont.setPointSize(15)
        self.SettingsStartButton.setFont(self.testFont)
        


        # Settings Menu Slider 1 - number of shapes
        self.ShapeSlider = QSlider(parent=self) #initialize slider
        self.ShapeSlider.setRange(2,4)  #set range of slider
        self.ShapeSlider.show() #enable disp
        self.ShapeSlider.move(100,100)   #move to appropriate spot in window
        self.ShapeSlider.resize(200,50) #change size
        self.ShapeSlider.setTickInterval(4) #set amount of intervals
        self.ShapeSlider.setSliderPosition(1)   #set base position
        self.ShapeSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 1 - number of shapes
        self.ShapeLabel = QLabel("Number of Shapes: 2")
        self.testFont = self.ShapeLabel.font()
        self.testFont.setPointSize(15)
        self.ShapeLabel.setFont(self.testFont)
        self.ShapeLabel.setFixedSize(200,50)
        self.ShapeLabel.move(108,25)
        self.ShapeLabel.show()
        self.ShapeLabel.setParent(self)

        # Settings Menu Slider 1 - End Labels ('2' and '4')
        self.ShapeLabelLeft = QLabel("2")
        self.ShapeLabelLeft.setFixedSize(100,50)
        self.testFont = self.ShapeLabelLeft.font()
        self.testFont.setPointSize(15)
        self.ShapeLabelLeft.setFont(self.testFont)
        self.ShapeLabelLeft.move(75,70)
        self.ShapeLabelLeft.show()
        self.ShapeLabelLeft.setParent(self)
        self.ShapeLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ShapeLabelRight = QLabel("4")
        self.ShapeLabelRight.setFixedSize(100,50)
        self.testFont = self.ShapeLabelRight.font()
        self.testFont.setPointSize(15)
        self.ShapeLabelRight.setFont(self.testFont)
        self.ShapeLabelRight.move(310,70)
        self.ShapeLabelRight.show()
        self.ShapeLabelRight.setParent(self)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ShapeLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # Settings Menu Slider 2 - number of colors 2 - 4 (increments of 1)
        self.ColorSlider = QSlider(parent=self) #initialize slider
        self.ColorSlider.setRange(2,4)  #set range of slider
        self.ColorSlider.show() #enable disp
        self.ColorSlider.move(500,100)   #move to appropriate spot in window
        self.ColorSlider.resize(200,50) #change size
        self.ColorSlider.setTickInterval(4) #set amount of intervals
        self.ColorSlider.setSliderPosition(1)   #set base position
        self.ColorSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 2 - number of colors
        self.ColorLabel = QLabel("Number of Colors: 2")
        self.ColorLabel.setFixedSize(200,50)
        self.testFont = self.ColorLabel.font()
        self.testFont.setPointSize(15)
        self.ColorLabel.setFont(self.testFont)
        self.ColorLabel.move(510, 25)
        self.ColorLabel.show()
        self.ColorLabel.setParent(self)

        # Settings Menu Slider 2 - End Labels ('2' and '4')
        self.ColorLabelLeft = QLabel("2")
        self.ColorLabelLeft.setFixedSize(50,50)
        self.testFont = self.ColorLabelLeft.font()
        self.testFont.setPointSize(15)
        self.ColorLabelLeft.setFont(self.testFont)
        self.ColorLabelLeft.move(475,70)
        self.ColorLabelLeft.show()
        self.ColorLabelLeft.setParent(self)
        self.ColorLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ColorLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.ColorLabelRight = QLabel("4")
        self.ColorLabelRight.setFixedSize(50,50)
        self.testFont = self.ColorLabelRight.font()
        self.testFont.setPointSize(15)
        self.ColorLabelRight.setFont(self.testFont)
        self.ColorLabelRight.move(710,70)
        self.ColorLabelRight.show()
        self.ColorLabelRight.setParent(self)
        self.ColorLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.ColorLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)



        # Settings Menu Slider 3 - time per prompt - 30s - 120s (increments of 15s) --> next tick after 120s is 'no limit'
        self.TimerSlider = QSlider(parent=self) #initialize slider
        self.TimerSlider.setRange(2,9)  #set range of slider
        self.TimerSlider.show() #enable disp
        self.TimerSlider.move(100,255)   #move to appropriate spot in window
        self.TimerSlider.resize(200,50) #change size
        self.TimerSlider.setSliderPosition(2)   #set base position
        self.TimerSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 3 - time per prompt
        self.TimerLabel = QLabel("Time Per Round: 30 sec")
        self.TimerLabel.setFixedSize(300, 50)
        self.TimerLabel.move(90,180)
        self.TimerLabel.show()
        self.TimerLabel.setParent(self)
        self.testFont = self.TimerLabel.font()
        self.testFont.setPointSize(15)
        self.TimerLabel.setFont(self.testFont)


        # Settings Menu Slider 3 - End Labels ('1' and '4')
        self.TimerLabelLeft = QLabel("30 Sec")
        self.TimerLabelLeft.setFixedSize(100,50)
        self.TimerLabelLeft.move(30, 215)
        self.TimerLabelLeft.show()
        self.TimerLabelLeft.setParent(self)
        self.TimerLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TimerLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.testFont = self.TimerLabelLeft.font()
        self.testFont.setPointSize(15)
        self.TimerLabelLeft.setFont(self.testFont)

        self.TimerLabelRight = QLabel("No Limit")
        self.TimerLabelRight.setFixedSize(100,50)
        self.TimerLabelRight.move(310,215)
        self.TimerLabelRight.show()
        self.TimerLabelRight.setParent(self)
        self.TimerLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.TimerLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.testFont = self.TimerLabelRight.font()
        self.testFont.setPointSize(15)
        self.TimerLabelRight.setFont(self.testFont)



        # Settings Menu Slider 4 - number of prompts - 3 - 10 (increments of 1)
        self.PromptSlider = QSlider(parent=self) #initialize slider
        self.PromptSlider.setRange(3,10)  #set range of slider
        self.PromptSlider.show() #enable disp
        self.PromptSlider.move(500,255)   #move to appropriate spot in window
        self.PromptSlider.resize(200,50) #change size
        self.PromptSlider.setTickInterval(8) #set amount of intervals
        self.PromptSlider.setSliderPosition(1)   #set base position
        self.PromptSlider.setOrientation(Qt.Orientation.Horizontal)  #set orientation

        # Settings Menu Slider Label 4 - number of prompts
        self.PromptLabel = QLabel("Number of Rounds: 3")
        self.PromptLabel.setFixedSize(200, 50)
        self.PromptLabel.move(500, 180)
        self.PromptLabel.show()
        self.PromptLabel.setParent(self)
        self.testFont = self.PromptLabel.font()
        self.testFont.setPointSize(15)
        self.PromptLabel.setFont(self.testFont)

        # Settings Menu Slider 4 - End Labels ('3' and '10')
        self.PromptLabelLeft = QLabel("3")
        self.PromptLabelLeft.setFixedSize(50,50)
        self.PromptLabelLeft.move(475, 215)
        self.PromptLabelLeft.show()
        self.PromptLabelLeft.setParent(self)
        self.PromptLabelLeft.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.PromptLabelLeft.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.testFont = self.PromptLabelLeft.font()
        self.testFont.setPointSize(15)
        self.PromptLabelLeft.setFont(self.testFont)

        self.PromptLabelRight = QLabel("10")
        self.PromptLabelRight.setFixedSize(50,50)
        self.PromptLabelRight.move(710, 215)
        self.PromptLabelRight.show()
        self.PromptLabelRight.setParent(self)
        self.PromptLabelRight.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.PromptLabelRight.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.testFont = self.PromptLabelRight.font()
        self.testFont.setPointSize(15)
        self.PromptLabelRight.setFont(self.testFont)
            
        def updateShapeLabel():
            self.ShapeLabel.setText("Number of Shapes: " + str(self.ShapeSlider.value()))

        def updateColorLabel():
            self.ColorLabel.setText("Number of Shapes: " + str(self.ColorSlider.value()))
            
        def updateTimerLabel():
            if (self.TimerSlider.value() < 9):
                self.TimerLabel.setText("Time Per Round: " + str(self.TimerSlider.value()*15) + " sec")    
            else:
                self.TimerLabel.setText("Time Per Round: No Limit")

        def updatePromptLabel():
            self.PromptLabel.setText("Number of Rounds: " + str(self.PromptSlider.value()))

        self.ShapeSlider.valueChanged.connect(updateShapeLabel)
        self.ColorSlider.valueChanged.connect(updateColorLabel)
        self.TimerSlider.valueChanged.connect(updateTimerLabel)
        self.PromptSlider.valueChanged.connect(updatePromptLabel)

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.roundChangeBuffer = QLineEdit()
        self.roundChangeBuffer.setParent(self)
        self.roundChangeBuffer.hide()

        self.starImage = QLabel(parent=self)
        self.circleImage = QLabel(parent=self)
        self.triangleImage = QLabel(parent=self)
        self.squareImage = QLabel(parent=self)

        self.debug_button = QPushButton("Next Prompt (Debug)")
        self.debug_button.setFixedSize(150, 50)
        self.debug_button.move(325, 200)
        self.debug_button.setParent(self)
        self.debug_button.show()
        
        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
        self.colorStar2 = self.colorStar.scaled(150,150)
        self.starImage.setPixmap(self.colorStar2)
        self.starImage.show()
        self.starImage.setFixedSize(150,150)
        self.starImage.move(125,37)

        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
        self.colorCircle2 = self.colorCircle.scaled(150,150)
        self.circleImage.setPixmap(self.colorCircle2)
        self.circleImage.show()
        self.circleImage.setFixedSize(150,150)
        self.circleImage.move(525,37)

        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
        self.colorTriangle2 = self.colorTriangle.scaled(150,150)
        self.triangleImage.setPixmap(self.colorTriangle2)
        self.triangleImage.show()
        self.triangleImage.setFixedSize(150,150)
        self.triangleImage.move(125,225)

        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
        self.colorSquare2 = self.colorSquare.scaled(150,150)
        self.squareImage.setPixmap(self.colorSquare2)
        self.squareImage.show()
        self.squareImage.setFixedSize(150,150)
        self.squareImage.move(525,225)

        self.RoundsLabel = QLabel("Current Round: 1 / 10")
        self.RoundsLabel.setFixedSize(150, 50)
        self.RoundsLabel.move(325, 312)
        self.RoundsLabel.setParent(self)
        self.RoundsLabel.show()
        self.RoundsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.TimerLabel = QLabel(parent=self)
        self.TimerLabel.setFixedSize(150, 50)
        self.TimerLabel.move(325, 375)
        self.TimerLabel.show()
        self.TimerLabel.setText("Time Remaining: ")
        self.TimerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.RoundTimer = QTimer(parent=self)
        self.RoundTimer.setInterval(1000)

        def updateTimer():
            #print("Timer event triggered!")
            global programRunning
            global currentTimer
            global useTimer
            global timePerRound

            if (not programRunning):
                programRunning = True
                currentTimer = 0
                newPrompt()

            if useTimer and timePerRound < 121:
                if currentTimer <= timePerRound:
                    self.TimerLabel.setText("Time Remaining: " + str(timePerRound - currentTimer) + " sec")
                else:
                    newPrompt()
                currentTimer += 1
            else:
                self.TimerLabel.setText("Time Remaining: No Limit")

            print("Current Timer: " + str(currentTimer))
            


        # generates a new random shape and color
        def newPrompt():

            global shapeListPool
            global colorListPool

            global currentRound

            global redList
            global yellowList
            global greenList
            global blueList

            global starList
            global circleList
            global triangleList
            global squareList

            global promptObject
            global promptColor
            global promptShape

            global currentTimer
            global useTimer

            global timePerRound

            lastPrompt = promptObject
            lastColor = promptColor
            lastShape = promptShape

            currentTimer = 0


            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            self.roundChangeBuffer.setText("keepPlaying")

#            if timePerRound > 120: 
#                useTimer = False
#            else:
#                useTimer = True
#
#            self.RoundsLabel.setText("Current Round "+ str(currentRound + 1) + " / " + str(totalPrompts))
#
#            if useTimer:
#                self.TimerLabel.setText("Time Remaining: " + str(timePerRound - currentTimer) + " sec")
#            else:
#                self.TimerLabel.setText("Time Remaining: No Limit")

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

            if (currentRound < totalPrompts):
                #until you have a new unique item...

                while(True):
                    # randomize item
                    randomShape = shapeListPool[random.randint(0,len(shapeListPool)-1)]
                    randomColor = colorListPool[random.randint(0,len(colorListPool)-1)]
                    
                    # identify which item was chosen
                    # RED SHAPES
                    if (randomColor == 0 and randomShape == 0):
                        #print("Prompt: Red Star")
                        promptObject = redStar
                        promptColor = 0
                        promptShape = 0
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/RedStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 0 and randomShape == 1):
                        #print("Prompt: Red Circle")
                        promptObject = redCircle
                        promptColor = 0
                        promptShape = 1
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/RedCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 0 and randomShape == 2):
                        #print("Prompt: Red Triangle")
                        promptObject = redTriangle
                        promptColor = 0
                        promptShape = 2
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/RedTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 0 and randomShape == 3):
                        #print("Prompt: Red Square")
                        promptObject = redSquare
                        promptColor = 0
                        promptShape = 3
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/RedSquare.png")

                    # YELLOW SHAPES
                    elif (randomColor == 1 and randomShape == 0):
                        #print("Prompt: Yellow Star")
                        promptObject = yellowStar
                        promptColor = 1
                        promptShape = 0
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/YellowStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 1 and randomShape == 1):
                        #print("Prompt: Yellow Circle")
                        promptObject = yellowCircle
                        promptColor = 1
                        promptShape = 1
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/YellowCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 1 and randomShape == 2):
                        #print("Prompt: Yellow Triangle")
                        promptObject = yellowTriangle
                        promptColor = 1
                        promptShape = 2
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/YellowTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 1 and randomShape == 3):
                        #print("Prompt: Yellow Square")
                        promptObject = yellowSquare
                        promptColor = 1
                        promptShape = 3
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/YellowSquare.png")

                    # GREEN SHAPES
                    elif (randomColor == 2 and randomShape == 0):
                        #print("Prompt: Green Star")
                        promptObject = greenStar
                        promptColor = 2
                        promptShape = 0
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GreenStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 2 and randomShape == 1):
                        #print("Prompt: Green Circle")
                        promptObject = greenCircle
                        promptColor = 2
                        promptShape = 1
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GreenCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 2 and randomShape == 2):
                        #print("Prompt: Green Triangle")
                        promptObject = greenTriangle
                        promptColor = 2
                        promptShape = 2
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GreenTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 2 and randomShape == 3):
                        #print("Prompt: Green Square")
                        promptObject = greenSquare
                        promptColor = 2
                        promptShape = 3
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GreenSquare.png")

                    # BLUE SHAPES
                    elif (randomColor == 3 and randomShape == 0):
                        #print("Prompt: Blue Star")
                        promptObject = blueStar
                        promptColor = 3
                        promptShape = 0
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/BlueStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 3 and randomShape == 1):
                        #print("Prompt: Blue Circle")
                        promptObject = blueCircle
                        promptColor = 3
                        promptShape = 1
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/BlueCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 3 and randomShape == 2):
                        #print("Prompt: Blue Triangle")
                        promptObject = blueTriangle
                        promptColor = 3
                        promptShape = 2
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/BlueTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GraySquare.png")
                    elif (randomColor == 3 and randomShape == 3):
                        #print("Prompt: Blue Square")
                        promptObject = blueSquare
                        promptColor = 3
                        promptShape = 3
                        self.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayStar.png")
                        self.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayCircle.png")
                        self.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/GrayTriangle.png")
                        self.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/BlueSquare.png")

                    # update the images
                    self.colorStar2 = self.colorStar.scaled(150,150)
                    self.starImage.setPixmap(self.colorStar2)
                    self.colorCircle2 = self.colorCircle.scaled(150,150)
                    self.circleImage.setPixmap(self.colorCircle2)
                    self.colorTriangle2 = self.colorTriangle.scaled(150,150)
                    self.triangleImage.setPixmap(self.colorTriangle2)
                    self.colorSquare2 = self.colorSquare.scaled(150,150)
                    self.squareImage.setPixmap(self.colorSquare2)

                    # debugging print statements

                    #print("promptObject: ", promptObject)
                    #print("lastPrompt: ", lastPrompt)
                    #print("lastColor: ", lastColor)
                    #print("lastShape: ", lastShape)

                    if (lastPrompt != promptObject):
                        break
                    if (lastColor != promptColor):
                        break
                    if (lastShape != promptShape):
                        break

                currentRound += 1
                self.roundChangeBuffer.setText("keepPlaying")
                self.RoundsLabel.setText("Current Round "+ str(currentRound) + " / " + str(totalPrompts))
            else:
                self.roundChangeBuffer.setText("stopPlaying")
        
                


            
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
        self.RoundTimer.timeout.connect(updateTimer)
        

    

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

        def EndGame():
            global currentRound
            global totalPrompts
            if (currentRound >= totalPrompts and self.Game.roundChangeBuffer.text() == "stopPlaying"):
                self.Game.hide()
                self.Settings.show()
                resetGame()

        def StartGame():

            # hide settings menu, show game menu, grab appropriate globals and constants to set up the game with
            global programRunning

            self.Game.show()
            self.Settings.hide()

            global shapeListConst
            global colorListConst

            global shapeListPool
            global colorListPool

            global currentRound
            global currentTimer

            global shapeNumber
            global colorNumber
            global timePerRound
            global totalPrompts

            colorListPool = [0]
            shapeListPool = [0]

            tempColorList = colorListConst
            tempShapeList = shapeListConst

            colorNumber = self.Settings.ColorSlider.value()
            shapeNumber = self.Settings.ShapeSlider.value()
            totalPrompts = self.Settings.PromptSlider.value()
            timePerRound = self.Settings.TimerSlider.value() * 15

            tempColor = -1
            tempShape = -1

            # debug print statements
            print("Number of Colors: ", colorNumber)
            print("Numnber of Shapes: ", shapeNumber)
            print("Time Per Round: ", timePerRound)
            print("Number of Rounds: ", totalPrompts)

            # copy a temp list of colors
            # randomly grab an item from that list, add it to the pool (used in newPrompt())
            # remove item from temp list to prevent picking the same item twice
            # do this N times, where N = colorNumber
            # repeat for shapes

            for i in range(colorNumber):
                #print("color number: \t", i)
                tempColor = tempColorList[random.randint(0, len(tempColorList)-1)]
                if (i == 0):
                    colorListPool[0] = tempColor
                else:
                    colorListPool.append(tempColor)
                #print("tempColor: \t",tempColor)
                tempColorList.remove(tempColor)

            for i in range(shapeNumber):
                #print("shape number: \t", i)
                tempShape = tempShapeList[random.randint(0, len(tempShapeList)-1)]
                if (i == 0):
                    shapeListPool[0] = tempShape
                else:
                    shapeListPool.append(tempShape)
                #print("tempColor: \t",tempShape)
                tempShapeList.remove(tempShape)

            colorListConst = [0,1,2,3]
            shapeListConst = [0,1,2,3]

            currentRound = 0

            if (not programRunning):
                currentTimer = timePerRound - 2

            programRunning = False

            self.Game.RoundTimer.start()

            self.Game.roundChangeBuffer.setText("keepPlaying")

            if timePerRound > 120: 
                useTimer = False
            else:
                useTimer = True

            self.Game.RoundsLabel.setText("Current Round "+ str(currentRound + 1) + " / " + str(totalPrompts))

            if useTimer:
                self.Game.TimerLabel.setText("Time Remaining: " + str(timePerRound - currentTimer) + " sec")
            else:
                self.Game.TimerLabel.setText("Time Remaining: No Limit")
            

        def resetGame():

            global shapeListConst
            global colorListConst

            global shapeListPool
            global colorListPool

            colorListPool = [0]
            shapeListPool = [0]

            global currentRound
            global currentTimer

            global shapeNumber
            global colorNumber
            global timePerRound
            global totalPrompts

            colorListConst = [0,1,2,3]
            shapeListConst = [0,1,2,3]
            currentRound = 0
            currentTimer = 0

            self.Game.colorStar = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/grayStar.png")
            self.Game.colorCircle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/grayCircle.png")
            self.Game.colorTriangle = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/grayTriangle.png")
            self.Game.colorSquare = QPixmap("/home/nickl/pi-rfid/American_Training_24_005/graySquare.png")

            # update the images
            self.Game.colorStar2 = self.Game.colorStar.scaled(150,150)
            self.Game.starImage.setPixmap(self.Game.colorStar2)
            self.Game.colorCircle2 = self.Game.colorCircle.scaled(150,150)
            self.Game.circleImage.setPixmap(self.Game.colorCircle2)
            self.Game.colorTriangle2 = self.Game.colorTriangle.scaled(150,150)
            self.Game.triangleImage.setPixmap(self.Game.colorTriangle2)
            self.Game.colorSquare2 = self.Game.colorSquare.scaled(150,150)
            self.Game.squareImage.setPixmap(self.Game.colorSquare2)
            

        self.Settings.SettingsStartButton.clicked.connect(StartGame)
        self.Game.roundChangeBuffer.textChanged.connect(EndGame)
        

       


        

if __name__ == "__main__":
    app = QApplication([])
    
    window = WindowSystem()

    sys.exit(app.exec())
