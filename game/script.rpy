# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mango = Character("Mango")




# The game starts here.

label start:

    # STAGE ONE

    "."
    ".."
    "..."
    "suddenly, you're hungry."
    "."
    ".."
    "..."
    "...."
    "....."
    scene bg room # cutesy background
    with fade
    "You walk into the Fruit Cafe."

    show eileen happy


    return


"suddenly, you're ravenous."