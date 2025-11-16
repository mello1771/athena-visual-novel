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
    scene bg cafe normal # cutesy background
    with fade
    "You walk into the Fruit Cafe."

    "Warm light hits your face and your eyes automatically go to the menu, different fruit options being shown on the screen."

    you "Hello?"

    "You look around the cafe, but no one's there."

    "Just as you were about to leave, you hear a man's voice."

    o "I'll be right with you! Just place your order at the kiosk."

    "You stay silent as you look at the menu."

    menu:
        "Mango":
            $ fruit1 = "mangoes"
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
            scene bg cafe mango normal
            with fade
        "Kiwi":
            $ fruit1 = "kiwis"
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
            scene bg cafe kiwi normal
            with fade
        "Orange":
            $ fruit1 = "oranges"
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
            scene bg cafe orange normal
            with fade
        "Avocado":
            $ fruit1 = "avocados"
            "You're craving something smooth and neutral."
            "You put your head down as you wait for your order."
            "You recall something you heard about avocados..."
            "..."
            "'Round and creamy, green and dreamy,'"
            "'Avocados I want,'"
            "'To purchase in this restaurant.'"
            "..."
            "Your mind is filled with images of smooth, perfectly green avocados."
            "But wasn't there something else?"
            "There's something that you're forgetting."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your avocado."
            scene bg cafe avo normal
            with fade

    "You begin to eat your fruit, satisfaction warming your veins."
    "You've been waiting for this moment."
    "Before, it was as if there was a empty space in the center of your stomach, a hole that couldn't be filled."
    "The hunger gnawed and fed on your happiness and suffering, draining the feeling from the limbs of your heart."
    "But now, but now, you can finally be free."
    "..."
    "You look down at your plate."
    "You've finished your fruit."
    scene bg cafe normal
    with fade
    "Without something to do, the fact that you're alone in this cafe becomes more apparent to you."
    "You wonder why no one else would want to go here."
    "Maybe you're just different from everyone else. You always have been, haven't you?"
    "Something stirs within your memory, but refuses to surface."
    "..."
    "Your eyes drift towards the door in the corner, focusing on the words: 'Staff Only'."
    "You have no more food to appease your thoughts and your brain focuses on this door and this door only."
    "You feel your curiousity grasping it's hold on you, wondering what lies behind the door. Maybe it has fruit?"
    "The thought lights something within you, and you feel yourself walking towards the door and opening it."
    "..."
    "Your vision turns blurry, and you feel your legs turning numb."
    scene black
    with hpunch
    

    jump stage_two


label stage_two:

    scene black

    "."
    ".."
    "..."
    "You realize that you're starving."
    "."
    ".."
    "..."
    "...."

    scene bg cafe med

    "You walk into the cafe."

    "You notice a screen that the different fruit options are displayed on."

    you "..."

    "You begin to speak, but there's no one there, is there?"

    "Yet something tells you that maybe you should wait just a moment more."

    "Your gut feeling was correct, as a voice calls out."

    o "I'll be right with you! Just place your order at the kiosk."

    "It's time to choose."

    menu:
        "Mango":
            "The mango is the obvious option, isnt it?"
            if fruit1=="mangoes":
                "A feeling of familiarity settles upon your brain."
            $ fruit2 = "mangoes"
            "Your head falls into your arms, resting in a familiar spot on the table."
            "You recall something you heard about mangoes..."
            "..."
            "'Fruit of memory.'"
            "'A song of desperate childhood'"
            "'Confusion overrules.'"
            "..."
            "The image of a mango begins to come to your mind, but you brush it off."
            "You are forgetting something."
            "You know that there's something."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your... mango."
            scene bg cafe mango med
            with fade
        "Kiwi":
            "You're craving something tangy and sweet."
            if fruit1=="kiwis":
                "These thoughts feel familiar..."
            $ fruit2 = "kiwis"
            "Your head falls into your arms, resting in a familiar spot on the table."
            "You recall something you heard about kiwis..."
            "..."
            "'The kiwi, tart.'"
            "'Your hunger desperately amounts,'"
            "'Waiting for something to eat.'"
            "..."
            "The image of a kiwi begins to come to your mind, but you brush it off."
            "You are forgetting something."
            "You know that there's something."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your... kiwi."
            scene bg cafe kiwi med
            with fade
        "Orange":
            "You're craving something citrusy and tart."
            if fruit1=="oranges":
                "This sparks something deep in your mind, have you done this before?"
            $ fruit2 = "oranges"
            "You put your head down as you wait for your order."
            "You recall something you heard about oranges..."
            "..."
            "'The day has drained you,'"
            "'The sweet, round orange awaits you,'"
            "'To release you from the prison of your thoughts in which you're confined.'"
            "..."
            "The image of an orange begins to come to your mind, but you brush it off."
            "You are forgetting something."
            "You know that there's something."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your... orange."
            scene bg cafe orange med
            with fade
        "Avocado":
            "You're craving something smooth and neutral."
            if fruit1=="avocados":
                "These thoughts feel familiar..."
            $ fruit2 = "avocados"
            "You put your head down as you wait for your order."
            "You recall something you heard about avocados..."
            "..."
            "'Another fruit to be seen'"
            "'Avocados I need,'"
            "'To chase away the dreams.'"
            "..."
            "The image of an avocado begins to come to your mind, but you brush it off."
            "You are forgetting something."
            "You know that there's something."
            "Just as a thought begins to come to you, you hear a man place down your plate."
            "You lift up your head and see your... avocado."
            scene bg cafe avo med
            with fade

    "You continue to eat your fruit, unable to stop yourself from shoveling it into your mouth."
    "You've been waiting for this moment."
    "The hole can never be filled."
    "The hunger was eating you from the inside out."
    "But now, but now, you can finally be free."
    "But you've thought that before, haven't you?"
    "..."
    "The fruit is gone."
    "But it's okay, because you just ate, right? The hunger won't return."
    "Yet as you sit there, with no one around, the doubt begins to creep in once again, its tendrils wrapping around your brain, suffocating your thoughts."
    "You can't think, you start to wonder why you're even here."
    "..."
    "Your eyes arrive at the door. It sits there, an old friend."
    "You're still hungry. "
    "You need more food."
    "You stumble out of your seat towards the door, reaching for the satisfaction of the hunger that burns within you."
    "..."

    scene black
    with hpunch

    jump stage_three



label stage_three:

    scene black

    "."
    ".."
    "..."
    "you are ravenous."
    "."
    ".."
    "..."
    "...."

    scene bg cafe weird
    "it's the cafe."

    "you see the fruits... the food..."

    you "please... just serve me..."

    "the voice taunts you"

    o "I'll be right with you! Just place your order at the kiosk."

    if fruit2=="mangoes":
        "you want the mango, don't you?"
        "it's calling to you, familiar somehow"
        "memories come to you in snippets..."
        "..."
        "'a song of joyous childhood'"
        "..."
        "'confusion overrules?'"
        "..." 
        "you find the taste lingering on your tongue, as if you've already ordered and ate"
        "confused, you ignore the thought and order anyway"
        "you sit down, wondering where all the other customers are, but the hunger is too strong to care"
        "footsteps approach, placing down your mango. you look up, wondering how someone could make your order so quickly"
        "..."
        "no ones there."

        scene bg cafe mango weird
        with hpunch

    elif fruit2=="kiwis":
        "you want the kiwi, don't you?"
        "it's calling to you, familiar somehow"
        "memories come to you in snippets..."
        "..."
        "'waiting for something to eat'"
        "..."
        "'your hunger desperately amounts?'"
        "..." 
        "you find the taste lingering on your tongue, as if you've already ordered and ate"
        "confused, you ignore the thought and order anyway"
        "you sit down, wondering where all the other customers are, but the hunger is too strong to care"
        "footsteps approach, placing down your mango. you look up, wondering how someone could make your order so quickly"
        "..."
        "no ones there."

        scene bg cafe kiwi weird
        with hpunch

    elif fruit2=="oranges":
        "you want the orange, dont you?"
        "it's calling to you, familiar somehow"
        "memories come to you in snippets..."
        "..."
        "'despite a day of fatigue'"
        "..."
        "'to release you from the prison of your thoughts?'"
        "..." 
        "you find the taste lingering on your tongue, as if you've already ordered and ate"
        "confused, you ignore the thought and order anyway"
        "you sit down, wondering where all the other customers are, but the hunger is too strong to care"
        "footsteps approach, placing down your mango. you look up, wondering how someone could make your order so quickly"
        "..."
        "no ones there."

        scene bg cafe orange weird
        with hpunch

    elif fruit2=="avocados":
        "you want the avocado, don't you?"
        "it's calling to you, familiar somehow"
        "memories come to you in snippets..."
        "..."
        "'avocados I want'"
        "..."
        "'to chase away the dreams?'"
        "..." 
        "you find the taste lingering on your tongue, as if you've already ordered and ate"
        "confused, you ignore the thought and order anyway"
        "you sit down, wondering where all the other customers are, but the hunger is too strong to care"
        "footsteps approach, placing down your mango. you look up, wondering how someone could make your order so quickly"
        "..."
        "no ones there."

        scene bg cafe avo weird
        with hpunch

      
    

    "you need it. you eat and you eat and you eat and you eat and you eat and you eat."
    "it's as if the hunger is peeling the tissues from your stomach, the skin from your bones."
    "..."
    "there's no more."
    "in a frenzy, you push yourself out of your seat"
    "this time it will work."
    "this time, you will get more."
    "there will be no worry. you will never have to think again."
    "you will never have to feel hungry again."
    "..."
    "you open the door."


    scene bg storage
    with hpunch

    o "..."

    you "no... no..."
    you "please... i can't be hungry any longer..."

    o "..."
    
    scene black
    with fade

    jump backstory


label backstory:

    scene bg backstory
    with fade

    you "Fruit."
    you "The one thing I thought I could have."

    you "For years, all other foods had evaded me."
    you "I could never feel happy with myself when I would eat."

    you "But there would always be fruit."
    you "I could eat [fruit1] and [fruit2]... these wouldn't affect me in the way other foods did."

    "..."

    you "Yet it wasn't enough."
    you "I would always feel hungry, and it grew worse each day."

    you "I would never be happy eating the other foods, but I wouldn't be happy if I was hungry either."

    you "There was no chance for a good ending."

    scene black
    with fade

    jump chef_backstory

label chef_backstory:

    scene bg storage
    with fade

    o "I always wanted to help you- yet I could never find a way"
    o "First, I tried to buy some more fruits for you, yet you were never full afterwards."
    o "My money ran out quickly, and I couldn't keep up with your hunger"
    o "Then, I thought that I could grow fruits for you myself, but the seeds that I have come from another world"
    o "I think those fruits made it worse for you, and you lost your memory."
    o "I'm sorry I was never able to save you."

    scene black
    with fade

    "End?"

    menu:
        "The End":
            return

#Shyla, Chloe, Shurui
