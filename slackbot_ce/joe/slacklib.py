
import led
import time

# Put your commands here
COMMAND1 = "are you awake?"
COMMAND2 = "what is your full name?"
COMMAND3 = "what is your favorite snack???"
COMMAND4 = "blue led"
COMMAND3 = "what is your favorite snack?"
COMMAND4 = "green led"
COMMAND5 = "how do you clean your hands?"
COMMAND6 = "red led"
COMMAND7 = "blue led"
#COMMAND8 = "blink green"

def blink_green():
    for i in range(2):
        led.green_led(1)
        time.sleep(0.2)
        led.green_led(0)
        time.sleep(0.2)
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""

    if command.find(COMMAND1) >= 0:
        response = "just barely..."

    elif command.find(COMMAND2) >= 0:
        response = "sirexa Watson Siri-Alexa."

    elif command.find(COMMAND3) >= 0:
        response = "electrons!"

    elif command.find(COMMAND4) >= 0:

        if command.find("on") >= 0:
            led.green_led(1)
            response = "ok"
        elif command.find("off") >= 0:
            led.green_led(0)
            response = "ok"
    elif command.find(COMMAND6) >= 0:

        if command.find("on") >= 0:
            led.red_led(1)
            response = "ok"
        elif command.find("off") >= 0:
            led.red_led(0)
            response = "ok"
           
    elif command.find(COMMAND7) >= 0:

        if command.find("on") >= 0:
            led.blue_led(1)
            response = "ok"
        elif command.find("off") >= 0:
            led.blue_led(0)
            response = "ok"
        else:
            response = "I'm not sure what to do with the green led."
            
    elif command.find(COMMAND5) >= 0:
        response = "well, this is embarassing... I don't have hands."

#    elif command.find(COMMAND8) >= 0:
#        blink_green()
#        response = "ok"
        
        


<<<<<<< HEAD

=======
>>>>>>> 2ef5191d4e3525b635e4372c024db0651a29756f
    return response
