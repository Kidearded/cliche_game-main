# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg black = "#000000"
define ys = Character("Yuri San")
define yuri_man = Character("Yuri Man")
define sune = Character("Sune Derei")
define kaorin = Character("Karoin Hearteyes")
define cf = Character("Vin Cere Condition")

default day_number = 1
default points = 0
image Vin Cere Angry = "Vin Cere Angry.png"
# If we have time make this look nicer
screen day_screen:
    frame:
        xalign 1.0
        ypos 0

        vbox:
            text "Day: [day_number]" 

label dream:
    scene bg cliff with fade

    kaorin "MISS PRESIDENT HELP ME!"

    cf "I DONT WANT TO DIE\n I LIED\n I LIED\n I LIKE GIRLS\n I LIKE WOMEN"

    sune "W-well it's not like I want to live"

label scene_two:
    yuri_man " Off to the yuri club, of which you are president. Hip Hip Hooray for the President of Yuri"
    
    scene bg school hallway with fade

    ys " I cant wait to lead the Yuri Girl Love Manga Club to another year of resounding success "

    scene bg book club room with fade
#linux boy show kaorin happy at right side
    kaorin "Q-queen Yuri!"
    kaorin "I'm not worthy"

    ys "Its just president Kaorin. "
    ys "This is a democracy."
    ys "And all who love Wuh Luh Wuh are worthy. Even the most hateful of wretches may find comfort within these hallowed halls"

    "*knock knock*"
#linux boy show sune neutral on right side
    sune "Is this the Anti-Stupid Pole of Stupidity club?"

    menu:
        "Yes, it is":
            sune "That sign says I <3 Yuri."

            ys "were multitasking"

            sune "I think im going to go-"

            ys "PLEASE PLEASE PLEASE STAY"
            ys "I finally became president of yuri but ill get demoted if we dont get any members"

            sune "okay? I guess?"

        "No this is the Yuri club, but your not going anywhere":
            sune "Says who?"

            kaorin "FOOL!"
            kaorin "You speak to the president of Yuri!"

            sune "Oh crap, do I have to bow or something?"

            ys "No your fine\n For Now."
#linux boy show vin cere in middle
    cf "Yuri-san. you called me?"

    ys "Welcome to the Yuri club my childhood best friend"

    cf "Uhh I don't like girls actually"

    ys "Yeah, thats what they all say"

    cf "I think im going to leave"

    menu:
        "can't, doors locked":
            cf "Who has the key?"

            ys "Kaorin! Window! NOW"
            #open window image linux boy
            kaorin "Yes miss president!"

            # Key flys here linux boy
            show key at Transform(xalign=0.0, yalign=0.5)
            with None

            show key at Transform(xalign=1.0, yalign=0.5)
            with move
            ys "I have no clue where the keys are actually."

        "I love you":
            cf "I love you too sister!"

            kaorin "Yowch"

            sune "Yikes"

            ys "I'm working on it"

            cf "Working on what?"

    ys "On to more important matters!\n What Yuri Girl Love Manga are we reading this month?"

    sune derei "Can we do the Green Yuri"

    kaorin "We always do the green yuri"

    cf "GUys can I please leave"

    menu:
        "Green Yuri again":
            sune "I-its not like I want to though!"

        "Pink Yuri":
            kaorin "I love the Pink Yuri!"

        "What if we did our own Yuri":
            kaorin "Great idea miss president!"




label cere_condition_route:
    yuri_man "This is a classic"
    
    # Add shaking of road
    scene bg road with vpunch
    "*running*"
    scene bg road with vpunch
    "*running*"
    scene bg road with vpunch
    "*running*"

    scene bg bang with vpunch
    "BANG!" # Possible sound effect her
    
    cf "Oww"
    
    scene bg road with fade
    show Vin Cere Neutral

    ys "Vin Cere? Are you okay??"

    cf "I'm fine I'm okay!"

    # No effects in this choice
    menu:
        "Are you sure? I heard something crack?":
            # Move her to the side and cracked concrete png
            

            cf "That was the concrete, see?"

            scene bg concrete crack with fade 

        "If you say so":
            # She holds her out
            pass
    scene bg road 
    cf "Help me up please?"
    
    ys "As you wish"
    #put a screen shake here linux boy
    
    cf "You can let go now"
    menu:
        "'No I think this is fine'":
            show Vin Cere Angry
            cf "Don't be silly we're late for school"
            ys "We can run together"
            ys "While holding hands"
            cf "Shut up stop messing with me"
        "'Do you want me to let go?'":
            show Vin Cere Blush
            cf "What kind of question is that! Of course I do, we have to run!"
    "*you let go*"
    ys "why were you running anyway?"
    show Vin Cere Angry
    cf "I'm late for the first day of school!"
    cf "And so are you!"
    cf "RUN!"

    jump scene_two



label karoin_route:
    yuri_man "Better late than hungry as they say"
    
    # Add shake scene
    scene bg road with vpunch
    scene bg road with vpunch
    scene bg bang with vpunch
    "BANG!" # Possible sound effect her
 
    ys "Yowch!!"

    scene bg sky
    show kaorin neutral

    kaorin "Oh my gosh! Yuri-San are you okay?"
    # screen blur
    
    ys "ow ow ow owch"

    kaorin "I’M SO SORRY YURI SAN! PLEASE FORGIVE ME"

    ys "Urgh."

    ys "How come your fine"

    kaorin "I was born hard headed. "
    kaorin "My nurse dropped me when I was born and it left a crack in the hospital floor."
    kaorin "I'm sorry"
    scene bg road with fade

    show kaorin neutral

    ys "Explains a lot"

    ys "Run to school with me?"
    show kaorin happy
    kaorin "C-can I?!"

    menu kaorin_first_meeting:
        "I don't see why not?":
            kaorin " Thank you thank you thank youthank youthank youthank youthank you thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you  thank you thank you thank you thank you thank you tha-"

        
        "No I was just messing with you":
            # send back to beginning of this scnee
            #have this shit jump to black linux boy
            yuri_man "Nope. you cant be mean. Not allowed. Try again"
            jump kaorin_first_meeting

        "I'd appreciate it":
            kaorin "I-I'll do my best!"
            ys "Sure?"
    jump scene_two



menu senu_nested_menu:

    "Whats with the racket":
        sune "What's it to you?"
                
        ys "It sounded like someone was getting hurt"

        sune "Then it sounded wrong. Piss off"
        
        return

    "You good?":
        sune "None of your business, go eat rocks"

        ys "Rocks dont taste very good"
    
    "This is a family friendly game you shouldn't be swearing":
        sune "What the fuck are you talking about"

        ys "I said this is a family friendly game you shouldn't be swearing"

        sune "Are you all there mentally?"

        ys " Isn't that the Himejoshi High uniform? Your a bit late for class don’t you think"

        sune " Are you always this concerned with other peoples business or am I getting special treatment "

    " Whats with the welt on your head":
        sune "The stupid pole of stupidity thats what"

        ys "  People actually run into poles? I thought that was like, a Tom and Jerry thing"

        sune " Apparently they do. I wasn’t even going to be late today but some idiot put the Stupid Pole of Stupidity here, and knocked me out cold."

label senu_nested_menu_wrapper:
    jump senu_nested_menu

label sune_route:
    "You decide running burns to many calories, and would thus ruin your bulk"

    yuri_man "Your lazy bum"
    
    # Make this shake slowly
    scene bg road with vpunch
    scene bg road with hpunch
    
    # Stop shake here?
    sune "Stupid "
    sune "*WHANG*"
    sune "fucking"
    sune "*WHANG*"
    sune "pole "
    sune "*WHANG* "
    sune "*CRACK*"
    
    ys "not touching that can of worms"
    #cut to black when ever Yuri Man is speaking linux boy
    yuri_man "Go check on that noise you joyless fool"

    menu:
        "Check the noise":
            # Still scene
            scene bg road
            show sune angry
            
            jump senu_nested_menu_wrapper
        
    ys "Need me to walk you to the nurses office?"

    sune "Huh?\n But you'll be even more late."
            
    menu:
        "I don't mind if its for you":
            yuri_man "Wow. Is this what the kids call 'game'"

        "Don't mind":
            sune "o-okay if you say so"

        "Good point. I'll be off then":
            sune Derei "Huh?"


    $ day_number = 2
    jump scene_two

menu late_to_school_options:
    
    "run to school":
        jump cere_condition_route
        return

    "Grab food and run to school":
        jump karoin_route

    "Walk to school":
        jump sune_route

label day_one:
    show screen day_screen
    show bg black
    yuri_man "Two days. Its all you get. Make your choices, and your sacrifices."

    ys "Oh No! I’m late!!"

    call late_to_school_options


label day_two:
    show screen day_screen

    scene bg black screen

    yuri_man "Day two"

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    if day_number == 1:
        jump day_one
    elif day_number == 2:
        jump day_two 

    # This ends the game.
    return
