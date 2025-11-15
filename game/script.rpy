# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define you = Character("You")
define o = Character("Owner")



# The game starts here.

label start:

    # STAGE ONE

    "."
    ".."
    "..."
    "You feel something in your stomach... you're hungry..."
    "."
    ".."
    "..."
    "...."
    "....."
    scene bg cafe # cutesy background
    with fade
    "You walk into the Fruit Cafe."

    "Warm light hits your face and your eyes automatically go to the menu, different fruit options being shown on the screen."

    you "Hello?"

    "You look around the cafe, but no one's there."

    "Just as you were about to leave, you hear a man's voice."

    o "I'll be right with you! Just place your order at the kiosk."

    "You stay silent as you look at the menu."

    menu:
        "mango":
            "You're craving something sweet and tropical."
            "You put your head down as you wait for your order."
            "You recall something you heard about mangoes..."
            "..."
            "'Bright, sweet juicy fruit.'"
            "'A song of joyous childhood'"
            "'Happiness overrules.'"
            "..."
            "Your mind is filled with images of glistening, fragrant mangoes."
            "But wasn't there something else?"
            "There's something that you're forgetting."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your mango."
            scene bg mango
            with fade
        "kiwi":
            "You're craving something tangy and sweet."
            "You put your head down as you wait for your order."
            "You recall something you heard about kiwis..."
            "..."
            "'The kiwi, tart and sweet,'"
            "'Your hunger amounts,'"
            "'Waiting for something to eat.'"
            "..."
            "Your mind is filled with images of glistening, fragrant mangoes."
            "But wasn't there something else?"
            "There's something that you're forgetting."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your kiwi."
            scene bg kiwi
            with fade
        "orange":
            "You're craving something citrusy and tart."
            "You put your head down as you wait for your order."
            "You recall something you heard about oranges..."
            "..."
            "'Despite a day of fatigue,'"
            "'The sweet, round orange awaits you,'"
            "'To release you from the thoughts in which you're contained.'"
            "..."
            "Your mind is filled with images of glistening, fragrant oranges."
            "But wasn't there something else?"
            "There's something that you're forgetting."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your orange."
            scene bg orange
            with fade
        "avocado":
            "You're craving something smooth and neutral."
            "You put your head down as you wait for your order."
            "You recall something you heard about avocados..."
            "..."
            "'Bright May afternoons-'"
            "'mango trees in the garden'"
            "'echoed with cuckoo calls'"
            "..."
            "Your mind is filled with images of smooth, perfectly green avocados."
            "But wasn't there something else?"
            "There's something that you're forgetting."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your avocado."
            scene bg orange
            with fade

    

    jump stage_two


label stage_two:

    scene

    "."
    ".."
    "..."
    "You realize that you're starving."
    "."
    ".."
    "..."
    "...."
    "....."

    scene bg cafe


    jump stage_three



label stage_three:

    scene

    "."
    ".."
    "..."
    "you are ravenous."
    "."
    ".."
    "..."
    "...."
    "....."

    scene bg cafe




    scene bg storage
    with hpunch
    with fade
    scene bg placeholder

    return


#Shyla, Chloe, Shurui
#other: Meeta Ahluwalia (mango poem), Roisin Kelly (orange poem)