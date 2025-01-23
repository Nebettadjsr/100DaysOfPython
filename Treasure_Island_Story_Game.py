from xml.dom.minidom import ProcessingInstruction

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
begin = input("Are you read to begin?\n Yes(Y) or No(N)?")
if begin == "N" or begin == "n":
    print("Too bad you miss out on the Treasure!")
elif begin == "Y" or begin == "y":
    print("You stand at the start of a narrow jungle path.\n"
          "the air smells of adventure... and banana peels.\n"
          "You arrive at a fork in the path.\n")
    path = input("Do you go Left(L) or Right(R)?\n")
    if path == "R" or path == "r":
        print("You turn right, the path seems calm.\n"
            "Suddenly, zombies leap out, singing, 'Don't stop me now!' by Queen.\n"
            "They think your brain is karaoke night.\nGAME OVER.\n")
        print('''
                                        (()))
                               /|x x|
                              /\( - )
                      ___.-._/\/
                     /=`_'-'-'/  !!
                     |-{-_-_-}     !
                     (-{-_-_-}    !
                      \{_-_-_}   !
                       }-_-_-}
                       {-_|-_}
                       {-_|_-}
                       {_-|-_}
                       {_-|-_}  ZOT
                   ____%%@ @%%_______
        ''')
    elif path == "L" or path == "l":
        print("You choose left, the jungle grows thicker.\n"
              "Birds squawk as if yelling, 'Good choice, mate!'\n"
              "You find yourself at the edge of a sparkling lake.\n")
        swim = input("Do you Swim(S) across or Wait(W)?")
        if swim == "S" or swim == "s":
            print("You dive into the lake, water feels nice at first.\n"
                  "But then a shark appears in sunglasses, holding a cocktail.\n"
                  "He grins: 'Dinner AND a show!' \nGAME OVER.\n")
            print('''
                                             ^`.                     o
                 ^_              \  \                  o  o
                 \ \             {   \                 o
                 {  \           /     `~~~--__
                 {   \___----~~'              `~~-_     ______          _____
                  \                         /// a  `~._(_||___)________/___
                  / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \ 
                  \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \ 
                                   /   /            / /
                                  '._.'           _/_/
                                                  ';|\ 
                        -David "TAZ" Baltazar-
            ''')
        elif swim == "W" or swim == "w":
            print("You sit by the lake, noticing ripples on the water.\n"
                  "A small boat drifts toward you, seemingly from nowhere.\n"
                  "You board the boat, rowing toward a mysterious island in the middle.\n"
                  "The boat docks near a little hut with three colorful doors.\n")
            door = input("You approach the hut and read a sign: 'Choose wisely, only one door leads to treasure.'\n"
                        "Which door will you choose? Red(R), Blue(B), or Yellow?(Y)\n")
            if door == "R" or door == "r":
                print("You open the red door. A dragon sits doing hot yoga.\n"
                      "'Interrupt me again,' it growls, 'and you're toast!' \nGAME OVER.\n")
                print('''
                                                      ,-,-      
                                     / / |      
                   ,-'             _/ / /       
                  (-_          _,-' `Z_/        
                   "#:      ,-'_,-.    \  _     
                    #'    _(_-'_()\     \ " |    
                  ,--_,--'                 |    
                 / ""                      L-'\ 
                 \,--^---v--v-._        /   \ | 
                   \_________________,-'      | 
                                    \           
                                     \          
                       Wny            \         
                                                

                ''')
            elif door == "B" or door == "b":
                print("You open the blue door. A room full of clowns emerges.\n"
                      "They laugh hysterically. You can't stop laughing. \nGAME OVER.\n")
                print('''
                     )               (
                    / \  .-"""""-.  / \ 
                   (   \/ __   __ \/   )
                    )  ; / _\ /_ \ ;  (
                   (   |  / \ / \  |   )
                    \ (,  \o/_\o/  ,) /
                     \_|   /   \   |_/
                       | (_\___/_) |
                       .\ \ -.- / /.
                      {  \ `===' /  }
                     {    `.___.'    }
                  jgs {             }
                       `"="="="="="`
                ''')
            elif door == "Y" or door == "y":
                print("You open the yellow door. A treasure chest sparkles in the sunlight.\n"
                      "'Congratulations!' a parrot screeches. 'You're rich!' \nYOU WIN!\n")
                print('''
                                                              _.--.
                                    _.-'_:-'||
                                _.-'_.-::::'||
                           _.-:'_.-::::::'  ||
                         .'`-.-:::::::'     ||
                        /.'`;|:::::::'      ||_
                       ||   ||::::::'     _.;._'-._
                       ||   ||:::::'  _.-!oo @.!-._'-.
                       \ .  ||:::::.-!()oo @!()@.-'_.|
                        '.'-;|:.-'.&$@.& ()$%-'o.'\ ||
                          `>'-.!@%()@'@_%-'_.-o _.|'||
                           ||-._'-.@.-'_.-' _.-o  |'||
                           ||=[ '-._.-\ /.-'    o |'||
                           || '-.]=|| |'|      o  |'||
                           ||      || |'|        _| ';
                           ||      || |'|    _.-'_.-'
                           |'-._   || |'|_.-'_.-'
                        jgs '-._'-.|| |' `_.-'
                                '-.||_/.-'
                    ''')


else:
    print("Answer not accepted")

