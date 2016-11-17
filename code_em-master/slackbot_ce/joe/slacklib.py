
import led
# Put your commands here
COMMAND1 = "Are you awake?"
COMMAND2 = "What is your full name?"
COMMAND3 = "what is your favorite snack?"
COMMAND4 = "green led"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""

    if command.find(COMMAND1) >= 0:
        response = "Just barely..."

    elif command.find(COMMAND2) >= 0:
        response = "Sirexa Watson Siri-Alexa."

    elif command.find(COMMAND3) >= 0:
        response = "electrons!"

    elif command.find(COMMAND4) >= 0:

        if command.find("on") >= 0:
            led.green_led(1)
            response = "ok"
        elif command.find("off") >= 0:
            led.green_led(0)
            response = "ok"
        else:
            response = "I'm not sure what to do with the green led."
        
    return response

