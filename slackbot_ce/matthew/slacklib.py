# Put your commands here

COMMAND1 = "who is sirtomato"
COMMAND2 = "talk in binary"
COMMAND3 = "i dont like you"
COMMAND4 = "brit"
COMMAND5 = "Slack_Stripper V1"
COMMAND6 = "leaderboard"
COMMAND7 = "where did you get that taco"
COMMAND8 = "do you kno de wae"
COMMAND9 = "who is WBAgames"
# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """

    response = ""
    if command.find(COMMAND1) >= 0:
        response = "A cuber/coder that loves Arch Linux and tiling window managers."
    elif command.find(COMMAND2) >= 0:
        response = """01000111 01101111 00100000 01100001 01110111 01100001 01111001 00101110 00100000 01000100 01101111 01101110 00100111 01110100 00100000 01110100 01100001 01110101 01101110 01110100 00100000 01101101 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 01110010 00100000 01100100 01100101 01101101 01100001 01101110 01100100 01110011 00101110"""
    elif command.find(COMMAND3) >= 0:
        response = "Well, I don't like you either!"
    elif command.find(COMMAND4) >= 0:
        response = "'Ello Chump, do you want some tea!'"
    elif command.find(COMMAND5) >= 0:
        response="""
        Hacking user @MACos...%%%%done.%%

        downloading fs...%%
        '/home' -- DONE%%
        '/bin' -- DONE%%
        '/usr' -- DONE%%%%%%
        '/etc' -- DONE%%%%
        '/boot' -- DONE %%

        searching for passwords...%%DONE
        DELETING SYSTEM32 AND BOOT FILES 
        OOooh Browser history!!! EWWWWW NEVERMIND YOU ARE DISGUSTING
        [*] All done. Have a nice day, you hacked fool. Ha Ha Ha! :)"""
    elif command.find(COMMAND6):
        # Custom commandhandler for sirexa
        
        leaderboard_command = command.split()
        leaderboard_command = leaderboard_command[1]
        
        if leaderboard_command == "help":
            response = """sirexa leaderboard v0.0.1
                give point: `@sirexa leaderboard +username`
                example: `@sirexa leaderboard +sirtomato`
                
                take point: `@sirexa leaderboard -username`
                example: `@sirexa leaderboard -notsirtomato`
                
                leaderboard: `@sirexa leaderboard points`"""
        response = ""
    if command.find(COMMAND7) >= 0:
        response = "ayee you know bois got his free taco"
        response = ""
    if command.find(COMMAND8) >= 0:
        response = "https://youtu.be/qt8MQRFqxVk  watch me!"
    if command.find(COMMAND9) >= 0:
        response = "WBAgames is mostly known west or WBAcubing and is a youtuber who does lots of fun stuff" 
    return response
