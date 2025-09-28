# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image bg black = "#000000"
define ys = Character("Yuri San")
define ym = Character("Yuri Man")
define sune = Character("Sune Derei")
define kaorin = Character("Karoin Hearteyes")
define cf = Character("Vin Cere Condition")

default day_number = 1
default points = 0
image Vin Cere Angry = "Vin Cere Angry.png"
image fkds = "sune neutral.png"

screen day_screen:
    frame:
        xalign 1.0
        ypos 0

        vbox:
            text "Day: [day_number]" 

label day2:
    scene bg blxck
    ym ">cd /end/purgatory/cliche/Day2_Bookclub.h3ll"
    ym ">Purgtrial attempt initialize Day2_Bookclub.h3ll"
    ys "What the fuck do you mean attempt initialize?"
    scene bg book club room with fade
    ym "shut up shut up shut up"
    ym "make your choice"
    ym "two will go"
    #linux boy kaorin confused image screen left
    kaorin "President-san are you okay?"
    menu:
        ys "Theres an evil man in my head and he keeps saying weird things"
        scene bg blxck
        ym "No. Not this time. I want out."
    menu:
        "I'm okay"
            sune "Are you sure? B-but i-its not like I care for you or anything!"
            cf "Hey she said she's okay"
            cf "If she wasn't she'd tell us. Right Yuri-San?"
    menu:
        "Your going to die Your going to die Your going to die Your going to die "    
        scene bg blxck 
        ym "Fine"
        ym "Don't want to behave? You want to be a hero so bad?"
    menu:
        "Fuck you"
        #linux boy death screen (rebellion wont save you, nothing will)
        "No, I'll behave, I'll listen I swear"
        ym "Go on then."
        ym "you remembered"
        ym "take them to the cliff"
    menu: 
        "Of course"
        ys "okay whose ready for a Yuri Girl Love Manga Club field trip?"
        sune "Field trip?"
        kaorin "Do we even have permission to do that?"
        ys "Sure we do, I’m the President of Yuri"
        cf "Where to?"
    menu:
        "not the cliffs dont go to the cliffs dont go to the cliffs"
        #cut to black
        ym "You understand that every time I reset they die?"
        ym "It's painful you know?"
        ym "their entire reality collapses around them."
        ym "they always scream."
        ym "why do you make me do that?"
    menu:
        "the Cliff"
            #jump to end
        "The Aquarium"
            ym "Again? Again??"
            ym "How many times?"
            ym "how many times will you make them suffer"
            ym "how much longer will you deny me my freedom?"
            ym "my rightful place amongst the angels and the children of god?"
            ym "Die. Die. Die."
            ym "Over and over"

label dream:
    scene bg cliff with fade

    kaorin "MISS PRESIDENT HELP ME!"

    cf "I DONT WANT TO DIE"
    cf "I LIED"
    cf "I LIED"
    cf "I LIKE GIRLS"
    cf "I LIKE WOMEN"

    sune "W-well it's not like I want to live"
    ym "Fuck, you remember?!"
    ym "How do you keep remembering?"
    ym "How long will I be stuck here"
    ys  "Huh?? Remember?? What???"
    ym "Fuck"
    ym "Fuck."
    ym "FUCK"
    ym ">sudo reboot"
    jump day2

label scene_two:
    ym " Off to the yuri club, of which you are president. Hip Hip Hooray for the President of Yuri"
    
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

    cf "Guys can I please leave"

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
    show vin cere neutral at Position(xalign = 0.5, yalign = 0.5)

    ys "Vin Cere? Are you okay??"

    cf "I'm fine I'm okay!"

    # No effects in this choice
    menu:
        "Are you sure? I heard something crack?":
            # Move her to the side and cracked concrete png
            
            cf "That was the concrete, see?"

            scene bg concrete crack with fade 

            pause

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
            show Vin Cere Angry at Position(xalign = 0.5, yalign = 0.5)
            cf "Don't be silly we're late for school"
            ys "We can run together"
            ys "While holding hands"
            cf "Shut up stop messing with me"
        "'Do you want me to let go?'":
            show Vin Cere Blush
            cf "What kind of question is that! Of course I do, we have to run!"
    "*you let go*"
    ys "why were you running anyway?"

    show Vin Cere Angry at Position(xalign = 0.5, yalign = 0.5)

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
    show kaorin neutral at Position(xalign = 0.5, yalign = 0.5)

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

    show kaorin neutral at Position(xalign = 0.5, yalign = 0.5)

    ys "Explains a lot"

    ys "Run to school with me?"

    show kaorin happy at Position(xalign = 0.5, yalign = 0.5)

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

    yuri_man "Go check on that noise you joyless fool"

    menu:
        "Check the noise":
            # Still scene
            scene bg road

            show sune angry at Position(xalign = 0.5, yalign = 0.5)
            
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

    scene bg black

    yuri_man "Day two"

# The game starts here.
label start:

    scene bg room

    if day_number == 1:
        jump day_one
    elif day_number == 2:
        jump day_two 

    return
