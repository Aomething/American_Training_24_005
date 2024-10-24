Nicholaus Linn
Oct 24, 2024

# General Functionality: 
## GUI
This system will prompt the user with a colored shape, detect the given shape (using RFID), and give appropriate feedback (correct vs incorrect match with the prompt)
The graphics is handled by a QT Project

## RFID
Wiring from the pi is controlled using the open source wiring_pi library, so that GPIO pins can be accessed

## NOTES
this will all be updated later, at the moment I just want to get the basic files up so I can clone them to the RPi we are using to control everything

Also note, I was torn on whether the GUI and GPIO would be controlled separately using multithreading, but for now I am going to attempt to use GPIO in the QT program and see how it goes
