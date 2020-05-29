print("▄███▄     ▄▄▄▄▄   ▄█▄    ██   █ ▄▄  ▄███▄   ")
print("█▀   ▀   █     ▀▄ █▀ ▀▄  █ █  █   █ █▀   ▀  ")
print("██▄▄   ▄  ▀▀▀▀▄   █   ▀  █▄▄█ █▀▀▀  ██▄▄    ")
print("█▄   ▄▀ ▀▄▄▄▄▀    █▄  ▄▀ █  █ █     █▄   ▄▀ ")
print("▀███▀             ▀███▀     █  █    ▀███▀   ")
print("                           █    ▀           ")
print("                          ▀                 ")
import time

# Tzankas Code

def final_scene2():

    # ascii code here 
    start_game()
def final_scene():
    print()
    print("Well done you reached the top floor \n")
    time.sleep(1)
    print("Take the helicopter \n")
    time.sleep(1)
    print("Take a glass of shampagne and off you go away from any trouble \n")
    time.sleep(1)
    print("Thank you for completing the game! \n")
    time.sleep(1)
    final_scene2()
    



def floor_2():
    print(" ######   ###     ######  ######  ####      #####")
    print(" ######   ###     ##  ##  ##  ##  ## ###   ##  ### ")
    print(" ##       ###     ##  ##  ##  ##  ##  ##     ###  ")
    print(" #####    ###     ##  ##  ##  ##  #####     ###    ") 
    print(" ##       ###     ##  ##  ##  ##  ## ##    ###   ")
    print(" ##       ######  ######  ######  ##  ##  ######## \n")
    print("You have reached the final floor of the game!.")
    time.sleep(1.5)
    print()
    time.sleep(2)
    tzanka_option1 = input("[1] Elevator option \n"
                           "[2] Picture with ducks option \n"
                           "[3] Ladder option \n")
    if tzanka_option1 == "1":
        print()
        time.sleep(2)
        print("You are going back to the basement")
        time.sleep(1)
        print("You need to start from the begining!!!")
        time.sleep(1.5)
        ground_floor()
    elif tzanka_option1 == "2":
        time.sleep(2)
        final_scene()
    elif tzanka_option1 == "3":
        print()
        time.sleep(2)
        print("Ladder broke so did your neck! Game over! Sorry Mate")
        time.sleep(1.5)
        start_game()

    else:
        print("WRONG ANSWER! TRY AGAIN!")
        tzanka_option1()  

# Clives code #

def clock():
    print("You go and investigate the clock. You can press a red or green button.")
    red_or_green = input("Do you choose red or green? [R/G]").lower().strip()
    if red_or_green == "r" or red_or_green == "red":
        print("Nothing happened, try again.")
        clock()
    elif red_or_green == "g" or red_or_green == "green":
        print("great - a secret door has been opened and you can continue on to the next level.")
        floor_2() 
    else:
        print("Invalid input, try again.")
        clock()

def lever():
    print("You see a lever. that says on it pull me Do you pull it up or down?")
    lever_choice = input("[Up/Down]?>").lower().strip()
    if lever_choice == "up" or lever_choice == "u":
        print("The lever doesn't seem to budge up, it must pull down.")
        lever()
    elif lever_choice == "down" or lever_choice == "d":
        print("That seems to be the right choice - a grandfather clock has appeared.")
        clock()
    else:
        print("Invalid input, try again.")
        lever()

def floor_one():
    
    print("Your decision to make, do you want to go left or right?")
    left_or_right = input("[L/R]?>").lower().strip()
    if left_or_right == "l" or left_or_right == "left":
        print("Oops, that's a dead end, try again to get out.")
        floor_one()
    elif left_or_right == "r" or left_or_right == "right" :
        print("Great, this looks the right way to go.")
        lever()
    else:
        print("Invalid input, try again.")
        floor_one()

# Johns code 

def ground_floor_2():
    print("Which door do you take? \n")
    print("[F] The fire symbol. \n"
            "[G] The gun symbol. \n"
            "[L] The lion symbol. \n"
            "[I] Investigate the area. \n")
    door_choice = input("")
    if door_choice == "f" or door_choice == "F":
        print()
        time.sleep(2)
        print("You hear a click and a jet of flame engulfs you.")
        time.sleep(2)
        print("You are dead. Game Over \n")
        time.sleep(1)
        start_game()
    elif door_choice == "L" or door_choice == "l":
        print()
        time.sleep(2)
        print("You step over the dead lions and see a stairwell heading up to the next floor.")
        time.sleep(1)
        floor_one() #takes you to the start of Clives code
    elif door_choice == "G" or door_choice == "g":
        print()
        time.sleep(2)
        print("You are riddled with bullets by a shark with a gun for a mouth.")
        time.sleep(1)
        print("You just about escape with your life in tact.") 
        time.sleep(1)
        ground_floor_2()
    elif door_choice == "I" or door_choice == "i":
        print()
        print("Scratched on the wall it reads, one has raging fires, one has armed assassins, one has lions that haven't eaten for three years. \n")
        time.sleep(1)
        ground_floor_2()


def ground_floor():
    time.sleep(2)
    print("  ________                                    ___ ___________  __                       ")
    print(" /  _____/   _____   ____  __ __   ____    __| _/ \_   _____/ |  |   ____   ____   ______")
    print("/   \  __   |_  __| /  _ \ |  |  \/    \  / __ |   |    __)   |  |  /  _ \ /  _ \ |_  __ |")
    print("\    \_\  \ |   |  (  <_> )|  |  /   |  \/ /_/ |   |     \    |  |_(  <_> |  <_> )| \/")
    print(" \______  / |__ |   \____/ |____/|___|  /\____ |   \___  /    |____/\____/ \____/ |__|   \n")
    print("You emerge from the darkness into a well lit room.")
    time.sleep(1)
    print ("The door slams shut behind you. \n")
    time.sleep(2)
    print("There are three doors in front of you adorned with symbols.")
    time.sleep (2)
    print("Which door do you take? \n")
    time.sleep(2)
    ground_floor_2()
    


# Joe's Code
def escape_door():
    print("You walk towards the only door in the room. You try to open it but it seems to be jammed. \n")
    time.sleep(2)
    print("How do you wish to proceed? \n")
    time.sleep(2)
    open_door = input("[1] Take a crowbar off the floor and pry open the door. \n"
                      "[2] You see a key on the wall next to the door. Use the key. \n"
                      "[3] Kick down the door with brute force. \n")                  
    if open_door == "1":
        print()
        time.sleep(2)
        print("The door prys open. You can just about fit through the gap. \n")
        time.sleep(1)
        print("You enter the next room. \n")
        time.sleep(1.5)
        ground_floor()
    elif open_door == "2":
        print()
        time.sleep(2)
        print("The key gets jammed. The door doesn't open.")
        time.sleep(1.5)
        escape_door()
    elif open_door == "3":
        print()
        time.sleep(2)
        print("You attempt to kick down the door but don't have enough strength to do so.")
        time.sleep(1.5)
        escape_door()





def escape_pipe():
    print("You notice a flashing red light in the corner of the room, beeping. You get up and walk towards it.")
    time.sleep(1.5)
    anwser_radio = input("It's a radio. Press ENTER to answer the radio. \n")
    if anwser_radio == "":
        print("This is the US Military! Our equipment has detected a bomb inside this building.")
        time.sleep(1.5)
        print("You must escape the building NOW before the bomb detonates! \n")
        time.sleep(1.5)
        escape_door()
    else:
        print("Answer the radio, please. \n")
        time.sleep(1.5)
        escape_pipe()

def basement_2():
        print("Which action do you wish to take? \n")
        time.sleep(2)
        handcuffed_pipe = input("[1] Break the pipe with a nearby brick. \n" 
                                "[2] Try pulling your hand out of the handcuffs. \n"
                                "[3] Scream for help. \n")
        if handcuffed_pipe == "1":
            print()
            time.sleep(2)
            print("That worked! You are now free and can move around. \n")
            time.sleep(1.5)
            escape_pipe()
        elif handcuffed_pipe == "2":
            print()
            time.sleep(2)
            print("That hurts too much. There must be another way to break free.")
            time.sleep(1.5)
            basement_2()
        elif handcuffed_pipe == "3":
            print()
            time.sleep(2)
            print("No one is answering... The building must be vacant.")
            time.sleep(1.5)
            basement_2()
        else:
            basement_2()

    

def basement():
    print("       ▄▄▄▄▀ ▄  █ ▄███▄       ███   ██      ▄▄▄▄▄   ▄███▄   █▀▄▀█ ▄███▄      ▄     ▄▄▄▄▀ ")
    print("▀▀▀ █   █   █ █▀   ▀      █  █  █ █    █     ▀▄ █▀   ▀  █ █ █ █▀   ▀      █ ▀▀▀ █    ")
    print("    █   ██▀▀█ ██▄▄        █ ▀ ▄ █▄▄█ ▄  ▀▀▀▀▄   ██▄▄    █ ▄ █ ██▄▄    ██   █    █    ")
    print("   █    █   █ █▄   ▄▀     █  ▄▀ █  █  ▀▄▄▄▄▀    █▄   ▄▀ █   █ █▄   ▄▀ █ █  █   █     ")
    print("  ▀        █  ▀███▀       ███      █            ▀███▀      █  ▀███▀   █  █ █  ▀      ")
    print("          ▀                       █                       ▀           █   ██         ")
    print("                                 ▀                                                   \n")

    print("You wake up in what seems to be a basement.")
    time.sleep(1.5)
    print("You find yourself handcuffed to a pipe. \n")
    time.sleep(1.5)
    basement_2()



def start_game():

    print("Welcome To Our Game - Escape. \n")
    time.sleep(2)
    
    user_responce = input("Are you ready to start? [Y/N] \n").lower().strip()
    if user_responce == "y" or user_responce == "yes":
        print()
        print("LET THE GAME BEGIN! \n")
        time.sleep(2)
        basement()
    elif user_responce == "n" or user_responce == "no":
        print("Wrong choice.. \n")
        time.sleep(1.5)
        start_game()
    else:
        print("Try again, I didn't recognise that.")
        time.sleep(1.5)
        start_game()

start_game()
