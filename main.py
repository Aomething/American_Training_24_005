# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *



WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

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


        def StartGame():
            print("--Test--")
            programRunning = False
            
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


        self.SettingsStartButton.clicked.connect(StartGame)
        self.ShapeSlider.valueChanged.connect(updateShapeLabel)
        self.ColorSlider.valueChanged.connect(updateColorLabel)
        self.TimerSlider.valueChanged.connect(updateTimerLabel)
        self.PromptSlider.valueChanged.connect(updatePromptLabel)

class WindowSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Settings = SettingsWidget()
        self.Settings.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)
        self.Settings.show()

        

if __name__ == "__main__":
    app = QApplication([])
    
    window = WindowSystem()

    sys.exit(app.exec())
