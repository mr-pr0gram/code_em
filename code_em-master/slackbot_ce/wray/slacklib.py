import random
import json
import urllib3

import temp_humidity
import led

COMMAND1 = "who are you"
COMMAND2 = "what can you do"
COMMAND3 = "temp"
COMMAND4 = "name an animal"
COMMAND5 = "green led"

def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "I am a simpleton bot."
    elif command.find(COMMAND2) >= 0:
        response = "Not much right now... waiting for students to teach me."
    elif command.find(COMMAND3) >= 0:
        try:
            temp_c,temp,humidity = temp_humidity.read_temp_humidity()
            response = "At my location, the temperature is " + str(temp) + " and the relative humidity is " + str(humidity)
        except:
            response = "At my location, there is a sensor malfunction."

    elif command.find(COMMAND4) >= 0:
        http = urllib3.PoolManager()
        animals = json.loads(http.request('GET','https://www.randomlists.com/data/animals.json').data.decode('utf-8'))['data']
        response = animals[random.randint(0,len(animals)-1)]
    elif command.find(COMMAND5) >= 0:
        if command.find("on") >= 0:
            led.green_led(1)
            response = "ok"
        elif command.find("off") >= 0:
            led.green_led(0)
            response = "ok"
        else:
            response = "I'm not sure what to do with the green led."
    return response

