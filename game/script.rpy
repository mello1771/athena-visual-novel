# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mango = Character("Mango")
define orange = Character("Orange")
define avocado = Character("avocado")
define kiwi = Character("kiwi")

define you = Character("You")
define owner = Character("Owner")



# The game starts here.

label start:

    # STAGE ONE

    "."
    ".."
    "..."
    "You're hungry."
    "."
    ".."
    "..."
    "...."
    "....."
    scene bg room # cutesy background
    with fade
    "You walk into the Fruit Cafe."

    "Warm light hits your face and your eyes automatically go to the menu, different fruit options shown on the screen."

    you "Hello?"

    "You look around the cafe, but no one's there"

    "Just as you were about to leave, you hear a man's voice."

    owner "I'll be right with you! Just place your order at the kiosk."

    



    show eileen happy


    return


"suddenly, you're ravenous."