import RPi.GPIO as GPIO
import time
 
#TripleLED_RGB Object
#The constructor allows you to specify the GPIO pins for the red, blue, and green diodes.
#The GPIO must have been initialized previously, except for the pins used here
class TripleLED_RGB(object):
 
        __diodePinRed = 0
        __diodePinBlue = 0
        __diodePinGreen = 0
 
        #Initialize the GPIO outputs
        def __init__(self, redPin, bluePin, greenPin):
                self._TripleLED_RGB__diodePinRed = redPin
                self._TripleLED_RGB__diodePinBlue = bluePin
                self._TripleLED_RGB__diodePinGreen = greenPin
                GPIO.setup(self._TripleLED_RGB__diodePinRed, GPIO.OUT)
                GPIO.setup(self._TripleLED_RGB__diodePinBlue, GPIO.OUT)
                GPIO.setup(self._TripleLED_RGB__diodePinGreen, GPIO.OUT)
 
        #Toggle A Diode
        def ToggleDiode(self, diodePin, turnOn):
                if turnOn:
                        GPIO.output(diodePin, GPIO.HIGH)
                else:
                        GPIO.output(diodePin, GPIO.LOW)
 
        def ToggleRed(self, turnOn):
                self.ToggleDiode(self._TripleLED_RGB__diodePinRed, turnOn)
 
        def ToggleBlue(self, turnOn):
                self.ToggleDiode(self._TripleLED_RGB__diodePinBlue, turnOn)
 
        def ToggleGreen(self, turnOn):
                self.ToggleDiode(self._TripleLED_RGB__diodePinGreen, turnOn)
 
        def ToggleLED(self, redOn, blueOn, greenOn):
                self.ToggleRed(redOn)
                self.ToggleBlue(blueOn)
                self.ToggleGreen(greenOn)
 
        #Turn the LED Red
        def TurnRed(self):
                self.ToggleLED(1,0,0)
 
        #Turn the LED Blue
        def TurnBlue(self):
                self.ToggleLED(0,1,0)
       
        #Turn the LED Green
        def TurnGreen(self):
                self.ToggleLED(0,0,1)
 
        #Turn the LED Purple
        def TurnPurple(self):
                self.ToggleLED(1,1,0)
 
        #Turn the LED Yellow
        def TurnYellow(self):
                self.ToggleLED(1,0,1)
 
        #Turn the LED Aqua
        def TurnAqua(self):
                self.ToggleLED(0,1,1)
 
        #Turn the LED White
        def TurnWhite(self):
                self.ToggleLED(1,1,1)
 
        #Turn the LED Off
        def TurnOff(self):
                self.ToggleLED(0,0,0)
 
        #Cycle Through All of the Colors
        #The timespan represents the time to wait until switching to the next color
        def Cycle(self, timespan):
                self.TurnRed()
                time.sleep(timespan)
                self.TurnBlue()
                time.sleep(timespan)
                self.TurnGreen()
                time.sleep(timespan)
                self.TurnAqua()
                time.sleep(timespan)
                self.TurnPurple()
                time.sleep(timespan)
                self.TurnYellow()
                time.sleep(timespan)
                self.TurnWhite()
                time.sleep(timespan)
                self.TurnOff()
