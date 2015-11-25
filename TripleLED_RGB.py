import RPi.GPIO as GPIO
import time
 
#TripleLED_RGB Object
#The constructor allows you to specify the GPIO pins for the red, blue, and green diodes.
#The GPIO must have been initialized previously, except for the pins used here
class TripleLED_RGB(object):
 
        __diodePinRed = 0
        __diodePinBlue = 0
        __diodePinGreen = 0
 
        currentColor = 0
 
        #Initialize the GPIO outputs
        def __init__(self, redPin, bluePin, greenPin):
                self._TripleLED_RGB__diodePinRed = redPin
                self._TripleLED_RGB__diodePinBlue = bluePin
                self._TripleLED_RGB__diodePinGreen = greenPin
                GPIO.setup(self._TripleLED_RGB__diodePinRed, GPIO.OUT)
                GPIO.setup(self._TripleLED_RGB__diodePinBlue, GPIO.OUT)
                GPIO.setup(self._TripleLED_RGB__diodePinGreen, GPIO.OUT)
 
        def ToggleDiode(self, diodePin, turnOn):
                if turnOn:
                        GPIO.output(diodePin, GPIO.HIGH)
                else:
                        GPIO.output(diodePin, GPIO.LOW)
 
        def ToggleLED(self, redOn, blueOn, greenOn):
                self.ToggleDiode(self._TripleLED_RGB__diodePinRed, redOn)
                self.ToggleDiode(self._TripleLED_RGB__diodePinBlue, blueOn)
                self.ToggleDiode(self._TripleLED_RGB__diodePinGreen, greenOn)
 
        #Set Color by Number
        def SetColor(self, colorNumber):
                if (colorNumber >= 0 & colorNumber <= 7):
                        self.currentColor = colorNumber
                elif (colorNumber > 7):
                        self.currentColor = 0
                elif (colorNumber < 0):
                        self.currentColor = 7
                bit0 = (self.currentColor & 1)
                bit1 = (self.currentColor & 2) >> 1
                bit2 = (self.currentColor & 4) >> 2
                self.ToggleLED(bit2, bit1, bit0)
 
        #Change to the next color
        def NextColor(self):
                if (self.currentColor == 7):
                        self.currentColor = 0
                self.SetColor(self.currentColor + 1)
 
        #Change to the previous color
        def PreviousColor(self):
                if (self.currentColor == 1):
                        self.currentColor = 8
                self.SetColor(self.currentColor - 1)
 
        #Turn the LED Off
        def TurnOff(self):
                self.SetColor(0)
 
        #Turn the LED Green
        def TurnGreen(self):
                self.SetColor(1)
 
        #Turn the LED Blue
        def TurnBlue(self):
                self.SetColor(2)
 
        #Turn the LED Aqua
        def TurnAqua(self):
                self.SetColor(3)
 
        #Turn the LED Red
        def TurnRed(self):
                self.SetColor(4)
 
        #Turn the LED Yellow
        def TurnYellow(self):
                self.SetColor(5)
 
        #Turn the LED Purple
        def TurnPurple(self):
                self.SetColor(6)
 
        #Turn the LED White
        def TurnWhite(self):
                self.SetColor(7)
 
        #Cycle Through All of the Colors
        #The timespan represents the time to wait until switching to the next color
        def Cycle(self, timespan):
                self.currentColor = 0
                count = 0
                while(count < 7):
                        self.NextColor()
                        time.sleep(timespan)
                        count = count + 1
