#-----------------
#Importing modules
#-----------------
import pygame
import random
from pygame import mixer

pygame.mixer.init()
wrong_sound = pygame.mixer.Sound(r'C:\Users\Admin\Desktop\Word-Guessing-Game\buzzer.wav')
correct_sound = pygame.mixer.Sound(r'C:\Users\Admin\Desktop\Word-Guessing-Game\correct.wav')

pygame.init()
mixer.music.load(r'C:\Users\Admin\Desktop\Word-Guessing-Game\background.mp3')
mixer.music.play(-1)


#---------------------
#Initializing the game
#---------------------[] u7
pygame.init()
sub2 = pygame.display.set_mode([650,570])
pygame.display.set_caption("Word Guessing Game")

#---------
#The Clock
#---------
clock = pygame.time.Clock()
FPS = 15

#------
#Colors
#------
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (40, 53, 88)
yellow = (255, 255, 0)
light_green = (0, 100, 0)
light_yellow = (200, 200, 0)
light_red = (150, 0, 0)

#--------------------
#Importing the Images
#--------------------
wordFrame = pygame.image.load("backframe.jpg")    #On which word would be printed
scoreButton = pygame.image.load("score.png")      #The score button
levelButton = pygame.image.load("level.png")      #The level button
heart = pygame.image.load("heart.jpg")            #The heart-- chances left for each word
inputText = pygame.image.load("input.png")        #Here the programmer will guess the word, and marks will be displayed for once
percent = pygame.image.load("percents.png")       #The background for marks
icon = pygame.image.load("icon.png")              #The game icon

#----------------
#Making the fonts
#----------------
wordGuessFont = pygame.font.SysFont("CopperPlate Gothic", 40)   #Font for the to be guessed word
wordType = pygame.font.SysFont("Calibri", 40)                   #Font for the word to be typed by user
scoreFont = pygame.font.SysFont("Comic Sans MS", 20)            #Font for score and level
hintFont = pygame.font.SysFont("Comic Sans MS", 20)             #Font for the hint
helpFont = pygame.font.SysFont("Comic Sans MS", 20)             #Font for start screen help
ratioFont = pygame.font.SysFont("CopperPlate Gothic",20)        #Font for displaying marks (5 out of 10)
msgFont = pygame.font.SysFont("CopperPlate Gothic",20)          #Font for displaying scores at the end
answerFont = pygame.font.SysFont("Juice ITC", 40)               #Font for displaying "Correct Answer" and the correct answer

#-----------------
#Setting the icon
#-----------------
pygame.display.set_icon(icon)
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#Level 1 lists
lst1 = ["apple","banana","guava","watermelon","grapes","mango","lichi","strawberry","pear","kiwi"]
lst2 = ["rose","jasmine","orchid","daisy","marigold","lily","sunflower","lotus"]

#Level 2 lists
lst3 = ["buffalo","tiger","giraffe","elephant","kangaroo","koala","dog","monkey"]
lst4 = ["bat","cock","eagle","parrot","ostrich","sparrow","vulture","dove","peacock","pigeon","swan"]
lst5 = ["butterfly","lizard","grasshopper","honeybee","snail","earthworm","ant","spider","ladybug","dragonfly","mosquito"]

#Level 3 lists
lst6 = ["marathi","english","hindi","maths","chemistry","physics","art","economics","history"]
lst7 = ["cricket","football","hockey","baseball","basketball","swimming","chess","boxing","wrestling","polo","tennis"]
lst8 = ["paper","pencil","compass","crayon","divider","eraser","file","magazine","tape","ruler","slate","glue","colour","sheet","marker"]

#Level 4 lists
lst9 = ["eyes","nose","tongue","teeth","hands","legs","neck","hair","foot","face","mouth"]
lst10 = ["cookie","pizza","salad","sandwich","mayonnaise","yogurt","cornflakes","popcorn","donut","omelette","rice"]
lst11 = ["brinjal","tomato","cauliflower","cucumber","ginger","jackfruit","ladyfinger","mushroom","pumpkin","spinach","chillies","cabbage","onion","radish","peas","carrot","garlic"]
lst12 = ["cheese","biscuit","butter","pancake","egg","loaf","bread","cake","cream","yeast","milk","honey"]

#Level 5 lists
lst13 = ["sickle","hammer","axe","lance","sword","blade","waterpot","spear","screwdriver","spade","chisel"]
lst14 = ["azure","crimson","indigo","saffron","scarlet","vermillion","purple","maroon","golden","mauve","pale","lemon"]
lst15 = ["anklet","bracelet","necklace","earring","locket","brooch","chain","silver","emerald","topaz","sapphire","turquoise","diamond","amethyst","aquamarine","platinum","pearl"]
lst16 = ["library","university","temple","orphanage","museum","factory","church","theatre","attic","courtyard","foundation","terrace","verandah","storey","railing","chimney","kitchen","bathroom","basement"]

#Globalizing the lists
global level_1_list
global level_2_list
global level_3_list
global level_4_list
global level_5_list

#Compiling them into individuals lists
level_1_list = lst1+lst2
level_2_list = lst3+lst4+lst5
level_3_list = lst6+lst7+lst8
level_4_list = lst9+lst10+lst11+lst12
level_5_list = lst13+lst14+lst15+lst16
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#Function to choose a random word
def chooseWord(level,randomWords):                  #randomWords is supplied so that the word should not be repeated.
    while True:
        if level == 1:
            word = random.choice(level_1_list)
            if word in lst1:
                hint = "Fruit"
            elif word in lst2:
                hint = "Flower"

        elif level == 2:
            word = random.choice(level_2_list)
            if word in lst3:
                hint = "Animal"
            elif word in lst4:
                hint = "Bird"
            elif word in lst5:
                hint = "Insect"

        elif level == 3:
            word = random.choice(level_3_list)
            if word in lst6:
                hint = "Subject"
            elif word in lst7:
                hint = "Sport"
            elif word in lst8:
                hint = "Stationary"

        elif level == 4:
            word = random.choice(level_4_list)
            if word in lst9:
                hint = "Body Part"
            elif word in lst10:
                hint = "Food Item"
            elif word in lst11:
                hint = "Vegetable"
            elif word in lst12:
                hint = "Dairy Product"

        elif level == 5:
            word = random.choice(level_5_list)
            if word in lst13:
                hint = "Weapon or Tool"
            elif word in lst14:
                hint = "Colour"
            elif word in lst15:
                hint = "Body Accessory or a Gem"
            elif word in lst16:
                hint = "A type of a building or a part of a building"

        if word in randomWords:      #Checks if the guessed word has already been used
            continue                 #if used continue
        else:                        #
            break                    #else break
                                     #
    randomWords.append(word)         #append the word into the list so it couldn't be used again
                                     #
    return [word,hint]               #returns the list to the process as ['apple', 'fruit']

#Function to display the random word on the screen
def displayWord(word, letters):                       #If the guessed letter is present, it is printed else * is printed
    HiddenWord = ""
    for i in range(len(word)):
        if (i == 0) or (i == len(word)-1):
            HiddenWord += " "+word[i]+" "
        elif word[i] in letters:
            HiddenWord += " "+word[i]+" "
        else:
            HiddenWord += " * "

    wordText = wordGuessFont.render(HiddenWord, True, yellow)
    sub2.blit(wordText, [20,200])

#Function to display the hint on the screen
def displayHint(hint):
    hintText = hintFont.render("Hint: "+hint, True, blue)
    sub2.blit(hintText, [50,300])

#Function to display the score on the screen
def displayScore(score):
    scoreText = scoreFont.render("Score: "+str(score), True, black)
    sub2.blit(scoreText, [25,20])

#Function to display the level on the screen
def displayLevel(level):
    levelText = scoreFont.render("Level: "+str(level), True, black)
    sub2.blit(levelText, [490,25])

#Function to display marks on the screen
def displayRatio(correctAnswers, Total):
    ratioText = ratioFont.render(str(int(correctAnswers))+" out of "+str(int(Total)), True, black)
    sub2.blit(ratioText, [300,110])

#Function to display user entered letters on the screen
def typeChar(char):
    TypeChar = wordType.render(char, True, green)
    sub2.blit(TypeChar, [50,395])
    pygame.display.update()

#Function to display the "Correct" or the correct answer
def printAnswer(word,chances):
    if chances == 0:
        msgAnswer = answerFont.render("The correct answer is: "+word[0], True, yellow)
        pygame.draw.rect(sub2, green, [0,500,650,570])
        sub2.blit(msgAnswer, [160,510])
        wrong_sound.play()
    else:
        msgAnswer = answerFont.render("Correct!", True, yellow)
        pygame.draw.rect(sub2, green, [0,500,650,570])
        sub2.blit(msgAnswer, [260,510])
        correct_sound.play()


    pygame.display.update()

    pExit = False

    while not pExit:
        for event_3 in pygame.event.get():
            if event_3.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_3.type == pygame.KEYDOWN:
                if event_3.key == pygame.K_RETURN:
                    pExit = True
                    break


#Function to be called after the game is complete
def gameComplete(score, correctAnswers, Total):                                                 #Screen Up animation
    for printRect in range(0,610,10):
        pygame.draw.rect(sub2, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    clock.tick(1)                                                                               #Waiting

    cExit = False

    msgOver = msgFont.render("YOU COMPLETED THE GAME", True, black)
    finalScore = msgFont.render("WITH SCORE: "+str(score), True, black)
    finalMarks = msgFont.render("And marks: "+str(int(correctAnswers))+" OUT OF "+str(int(Total)), True, black)
    playAgain = helpFont.render("Play Again", True, black)
    quitGame = helpFont.render("Quit", True, black)

    sub2.fill(blue)                                                                      #Making background and displaying results
    pygame.draw.rect(sub2, yellow, [0,100,800,400])
    pygame.draw.rect(sub2, green, [0,0,800,100])
    pygame.display.update()
    clock.tick(5)

    sub2.blit(msgOver, [100,200])
    pygame.display.update()
    clock.tick(5)

    sub2.blit(finalScore, [100,300])
    pygame.display.update()
    clock.tick(5)

    sub2.blit(finalMarks, [100,350])
    pygame.display.update()
    clock.tick(5)

    while not cExit:                                                                        #Waiting for the answer is user wants to
        sub2.fill(blue)                                                              #play again or quit
        pygame.draw.rect(sub2, yellow, [0,100,800,400])
        pygame.draw.rect(sub2, green, [0,0,800,100])
        sub2.blit(msgOver, [100,200])
        sub2.blit(finalScore, [100,300])
        sub2.blit(finalMarks, [100,350])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#PLAY AGAIN BUTTON
        if 100+175 > cur[0] > 100 and 400+50 > cur[1] > 400:                                #Adding play again or quit button
            pygame.draw.rect(sub2, light_green, [100,400,175,50])
            if click[0] == 1:
                for printRect in range(0,610,10):
                    pygame.draw.rect(sub2, blue, [0,600-(printRect),800,50+(printRect)])
                    pygame.display.update()
                    clock.tick(70)
                gameLoop()
        else:
            pygame.draw.rect(sub2, green, [100,400,175,50])

#QUIT BUTTON
        if 500+100 > cur[0] > 500 and 400+50 > cur[1] > 400:
            pygame.draw.rect(sub2, light_red, [500,400,100,50])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(sub2, red, [500,400,100,50])

        sub2.blit(playAgain, [125,405])
        sub2.blit(quitGame, [525,405])

        pygame.display.update()

        for event_2 in pygame.event.get():
            if event_2.type == pygame.QUIT:
                pygame.quit()
                quit()


#Start Screen
def startScreen():
    clock.tick(1)

    sExit = False
    helpLine1 = helpFont.render("You need to guess the word that appears on the screen", True, yellow)
    helpLine2 = helpFont.render("You will be given 5 chances for each word", True, yellow)
    helpLine3 = helpFont.render("There is no time limit", True, yellow)
    helpLine4 = helpFont.render("If you think that the word contains certain letter", True, green)
    helpLine5 = helpFont.render("Enter that letter and press Enter", True, green)
    helpLine6 = helpFont.render("If the word contains it, it would be displayed", True, green)
    helpLine7 = helpFont.render("There are 5 levels, and 5 words per level", True, red)
    helpLine8 = helpFont.render("Plus 100 points for each correct word multiplied by the level", True, red)
    helpLine9 = helpFont.render("plus 10 for each chance left", True, red)
    helpLine0 = helpFont.render("100 points deducted if you couldn't guess the word", True, red)

    quitGame = helpFont.render("Quit the game", True, red)

    playGame = helpFont.render("Play Game!", True, green)

    button1 = helpFont.render("Play", True, black)
    button2 = helpFont.render("Help", True, black)
    button3 = helpFont.render("Quit", True, black)

    Level1Start = wordGuessFont.render("LEVEL 1", True, green)

    sub2.fill(blue)                                                          #Making BG and displaying the heading
    pygame.display.update()
    clock.tick(1)

    heading = wordGuessFont.render("WORD GUESSING GAME", True, yellow)
    sub2.blit(heading, [50,100])
    pygame.display.update()
    clock.tick(1)


    while not sExit:
        sub2.fill(blue)
        sub2.blit(heading, [50,100])

        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#PLAY BUTTON
        if 100+100 > cur[0] > 100 and 200+50 > cur[1] > 200:
            pygame.draw.rect(sub2, light_green, [75,200,100,50])
            sub2.blit(playGame, [300,300])
            if click[0] == 1:
                sub2.fill(blue)
                sub2.blit(heading, [50,100])
                pygame.display.update()
                break
        else:
            pygame.draw.rect(sub2, green, [75,200,100,50])

#HELP BUTTON
        if 250+100 > cur[0] > 270 and 200+50 > cur[1] > 200:
            pygame.draw.rect(sub2, light_yellow, [270,200,100,50])

            sub2.blit(helpLine1, [50,300])
            sub2.blit(helpLine2, [50,325])
            sub2.blit(helpLine3, [50,350])
            sub2.blit(helpLine4, [50,375])
            sub2.blit(helpLine5, [50,400])
            sub2.blit(helpLine6, [50,425])
            sub2.blit(helpLine7, [50,450])
            sub2.blit(helpLine8, [50,475])
            sub2.blit(helpLine9, [50,500])
            sub2.blit(helpLine0, [50,525])

        else:
            pygame.draw.rect(sub2, yellow, [270,200,100,50])

#QUIT BUTTON
        if 450+100 > cur[0] > 470 and 200+100 > cur[1] > 200:
            pygame.draw.rect(sub2, light_red, [470,200,100,50])
            sub2.blit(quitGame, [300,300])
            if click[0] == 1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(sub2, red, [470,200,100,50])

#DISPLAYING THE WORDS ON BUTTONS
        sub2.blit(button1, [100,205])
        sub2.blit(button2, [300,205])
        sub2.blit(button3, [500,205])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#ANIMATION
    for printRect in range(0,610,10):
        pygame.draw.rect(sub2, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    sub2.blit(Level1Start, [230,250])
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0,610,10):
        sub2.blit(Level1Start, [230,250])
        pygame.draw.rect(sub2, blue, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(70)


#Function to perform animation at the time of level upgrade
def levelTransition(level):
    for printRect in range(0,610,10):
        pygame.draw.rect(sub2, yellow, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(50)

    textLevelStart = wordGuessFont.render("LEVEL "+str(level), True, green)             #This displayes level's name
    sub2.blit(textLevelStart, [230,250])                                         #Loop above and below for animation
    pygame.display.update()
    clock.tick(1)

    for printRect in range(0,610,10):
        sub2.blit(textLevelStart, [230,250])
        pygame.draw.rect(sub2, blue, [0,600-(printRect),800,50+(printRect)])
        pygame.display.update()
        clock.tick(70)

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
#The main game loop
def gameLoop():
    startScreen()       #Showing Start Screen
    gameExit = False
    string = ""         #The answer of user is stored in "string"
    letters = []        #Letters guessed by user
    chances = 5         #Chances per word
    score = 0           #Score

    correctAnswers = 0.0    #Correct Answers
    Total = 0.0             #Total words

    randomWords = []        #Words already displayed are placed in this
    level = 1               #Level
    level_up_check = 0      #If level_up_check reaches 5, level up, level_up_check is raised by 1 after every correct answer

    firstWord = True

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if len(string) < 16:
                    char = (chr(event.key))
                    string += char

                if event.key == pygame.K_RETURN:
                    if len(string) == 2:                #If there is only one letter, it is added into letters (\n is also counted)
                        letters.extend(string[0])
                    string = ""                         #Every time enter is pressed, string is reseted
                    chances -= 1                        #and a chance is minused.

                    if chances == 0:
                        printAnswer(word,chances)       #Prints the correct answer
                        string = ""                     #string, letters, chances are reseted
                        letters = []
                        chances = 5
                        del randomWords[-1]             #If you couldn't guess the word it won't be added into the randomWords list
                        word = chooseWord(level,randomWords)    #Word will be choosen again
                        Total += 1
                        score -= 100
                        if score < 0:
                            score = 0

                if event.key == pygame.K_BACKSPACE:
                    if string[-1] != chr(8):            #When Backspace is pressed
                        string = string[:-1]            #If string's length is equal to the limit, one character from end is deleted
                    else:                               #else two are deleted as when the string is less than the limit, backspace
                        string = string[:-2]            #char is also added in the end

        if firstWord == True:                           #This prints the first word, works only once
            word = chooseWord(1,randomWords)
            displayWord(word[0],letters)
            displayHint(word[1])
            firstWord = False

        if word[0] == string:                           #If the answer is correct
            typeChar(string)
            pygame.display.update()
            score += (100*level)+(chances*10)

            if correctAnswers != 25:                    #Checks for game over
                printAnswer(word, chances)
                if level_up_check >= 5:                 #Checks for level up
                    level += 1
                    level_up_check = 0
                    clock.tick(5)
                    levelTransition(level)
                word = chooseWord(level,randomWords)    #Choosing another word

                Total += 1
                correctAnswers += 1
                string = ""
                level_up_check += 1
                letters = []
                chances = 5

            else:
                printAnswer(word, chances)
                gameComplete(score, correctAnswers, Total)


        sub2.fill(blue)                      #Filling the background with the blue color
        sub2.blit(scoreButton, [0,0])        #Displaying the score button
        sub2.blit(levelButton, [430,0])      #Displaying the level button
        displayScore(score)                         #Displaying the score
        displayLevel(level)                         #Displaying the level



        try:                                                                                    #Checking the marks
            if ((correctAnswers/Total)*100 >= 60):                                              #Since at first Total = 0, ZeroDivisionError,
                sub2.blit(percent, [0,80], [0,0,800,90])                                 #So, white screen would be printed
            elif ((correctAnswers/Total)*100 >= 40) and ((correctAnswers/Total)*100 < 60):      #instead of a colored background
                sub2.blit(percent, [0,80], [0,90,800,90])                                #
            elif ((correctAnswers/Total)*100 < 40):                                             #Cropping and displaying the percent image,
                sub2.blit(percent, [0,80], [0,180,800,90])                               #according to the marks
        except:
            sub2.blit(inputText, [0,80])


        displayRatio(correctAnswers, Total)         #Displaying the marks

        sub2.blit(wordFrame, [0,160])        #Displaying the background for the to be guessed word
        displayWord(word[0],letters)                #Displaying the to be guessed word
        displayHint(word[1])                        #Displaying the hint

        for i in range(chances):                    #Displaying the hearts
            sub2.blit(heart, [20+(i*50),500])#depending on the chances left

        sub2.blit(inputText, [0,375])        #Displaying the background for the letters to be typed by the user
        typeChar(string)                            #Displaying the letters typed by the user


        clock.tick(FPS)                             #Clock ticking
        pygame.display.update()                     #Updating the screen................................

    pygame.quit()
    quit()

#Let's play the game...!
gameLoop()
