# ------ Simha and Paul worked on importing modules and variables -------

# import all of the neccesary libaries of the program
import sys, os
sys.path.insert(0, os.path.abspath('..'))
import pygame, random, pygame.gfxdraw, pygbutton
from pygame.locals import *
import pandas as pd
from pandas import DataFrame
import random

# Initiallize pygame
pygame.init()

# loading all of the various images that will be used in the program
background_image = pygame.image.load("images/Background.fw.png")
background_floor = pygame.image.load("images/dungeon_floor.fw.png")
winscreen = pygame.image.load("images/end screen.png")
scorescreen1 = pygame.image.load("images/score_screen.png")
losescreen = pygame.image.load("images/youlose.png")
initial_background = pygame.image.load("images/initial_background.png")
logo = pygame.transform.scale((pygame.image.load("images/logo.png")), (300,300))
Spidersound = pygame.mixer.Sound("sounds/Spidermusic.wav")


# Images of the characters
badguy1 = pygame.image.load("images/badguy 1.png")
badguy2 = pygame.image.load("images/badguy 2.png")
badguy3 = pygame.image.load("images/badguy 3.png")
goodguy = pygame.image.load("images/goodguy.png")


#transforming image sizes
bigboss = pygame.transform.scale(pygame.image.load("images/bigboss.png"),(300, 400))
computer_img = pygame.image.load("images/computer_img.png")
bobbyJenkins = pygame.transform.scale(computer_img,(1212,713))
jeff = pygame.transform.scale(goodguy, (255,510))
win1 = pygame.transform.scale(winscreen, (713,713))
lose1 = pygame.transform.scale(losescreen, (713,713))
scorescreen = pygame.transform.scale(scorescreen1,(1212,713))

#  inputting screen height and width
(width, height) = (1212, 713)

# inputting colours used in the game
black = [0,0,0]
white = [255, 255, 255]
green = [0, 255, 0]
blue = (100,50,255)
red = (255,0,0)
light_red = (255, 100, 100)
grey = (100,100,100)
lightgrey = (200,200,200)

# Intiallizing the font used in the game
font = pygame.font.Font(None, 90)
smallfont = pygame.font.SysFont("Calibri", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
#largefont = pygame.font.SysFont("Arialbold", 85)
largefont = pygame.font.SysFont("Arialbold", 100)
semimidfont = pygame.font.SysFont("Calibri", 30)

# Initiallizing variables
ctr = 0
score_cnt = 0
incorrectscore = 0
AnswerA = 0
c = 0
d = 0
bob = 0
newcorrectscore = 0


# Initiallizing screen using width and height
screen = pygame.display.set_mode((width, height))

# setting he caption of the window
pygame.display.set_caption('BataQuiz')

# setting  empty array called mylist
mylist = []

# Importing images for walk down function of spider
walkDown = [pygame.image.load('images/Spider.png'),
            pygame.image.load('images/Spider - Copy (2).png'),
            pygame.image.load('images/Spider - Copy (3).png'),
            pygame.image.load('images/Spider - Copy (4).png'),
            pygame.image.load('images/Spider.png'),
            pygame.image.load('images/Spider - Copy (2).png'),
            pygame.image.load('images/Spider - Copy (3).png'),
            pygame.image.load('images/Spider - Copy (4).png')]

# Importing images for walk side function of spider
walkSide = [pygame.transform.rotate(pygame.image.load('images/Spider.png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (2).png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (3).png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (4).png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider.png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (2).png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (3).png'),90),
            pygame.transform.rotate(pygame.image.load('images/Spider - Copy (4).png'),90)]





# ---------Paul Kokhanovs code ----------
# class spider for downward spider motion
class spider(pygame.sprite.Sprite):                     # create sprite class "player"
 def __init__(self, spider_x, spider_y, velocity):              # function "__init__" with parameters x,y,width,height
     self.x = spider_x                            # create variables that will be used in this class
     self.y = spider_y
     self.vel = velocity
     self.isJump = False
     self.down = True
     self.walkCount = 0
     #self.rect = pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) # create variable to draw a rectangle

 def down_walk(self):  # creating a function called "left_walk"
     self.y += self.vel    # substract self.vel from self.x
     if self.y >= 700:
         self.y = 0

 def draw(self, screen):       # creating a function called "draw"
     if self.walkCount + 1 >= 32:  # check if "walkcount" plus 1 becomes larger of equal to 27
         self.walkCount = 0        # reset varaible to 0
     if self.down:             # if self.left us true
         screen.blit(walkDown[self.walkCount // 4], (self.x, self.y))  # display certain image from "walkLeft" depending on the walkcount
         self.hitbox = (self.x + 20, self.y, 50, 65)
         self.surface = pygame.Rect(self.hitbox)
         self.rect = self.surface
         self.walkCount += 1 # add one to self.walkcount

# class spiderside for sideways spider motion
class spiderside(pygame.sprite.Sprite):                     # create sprite class "player"
 def __init__(self, spider_x, spider_y, velocity):              # function "__init__" with parameters x,y,width,height
     self.x = spider_x                            # create variables that will be used in this class
     self.y = spider_y
     self.vel = velocity
     self.isJump = False
     self.side = True
     self.walkCount = 0
     #self.rect = pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2) # create variable to draw a rectangle


 def side_walk(self):  # creating a function called "left_walk"
     self.x += self.vel    # substract self.vel from self.x
     if self.x >= 1300:
         self.x = 0


 def draw(self, screen):       # creating a function called "draw"
     if self.walkCount + 1 >= 32:  # check if "walkcount" plus 1 becomes larger of equal to 27
         self.walkCount = 0        # reset varaible to 0
     if self.side:             # if self.left us true
         screen.blit(walkSide[self.walkCount // 4], (self.x, self.y))  # display certain image from "walkLeft" depending on the walkcount
         self.hitbox = (self.x + 30, self.y, 50, 65)
         self.surface = pygame.Rect(self.hitbox)
         self.rect = self.surface
         self.walkCount += 1 # add one to self.walkcount




# ------- Simha Kalimipalli's code ----------

# class questionclass for processing questions and answers from CSVs
class QuestionClass:
    def __init__(self, question, length, correctans, answers):
        # Intitializing class variables
        self.question = question
        self.length = length
        self.correctans = correctans
        self.answerslist = answers.split('#')


    def print_Question(self): # prints question
        print(self.question)

    def print_Answers(self): # prints answers
        # print(self.answerslist)
        # print(self.answers)
        for i in range(len(self.answerslist)):
            print(self.answerslist[i])

# class bank class for processing questions from CSV
class BankClass:
    def __init__(self, fname):
        # initallize class variables
        self.bank = []
        self.fname = fname


    def createBank(self): # creates bank containing information from the CSV
        df = pd.read_csv(self.fname)
        Questionlist = df.values.tolist()
        for i in range(0,len(Questionlist)):
            Q = QuestionClass(Questionlist[i][0], Questionlist[i][1], Questionlist[i][2], Questionlist[i][3])
            self.bank.append(Q)

# Function for printing text on the screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(width / 2), int(height / 2) + y_displace)
    screen.blit(textSurf, textRect)

# class triviagame containing ctrs and len of words functions
class TriviaGame:
    def __init__(self,len1,len2):
        # initializing class variables
        self.ctr1 = 0
        self.ctr2 = 0
        self.len1 = len1
        self.len2 = len2

    def addctr1(self): # function for adding ctr1 to itself
        self.ctr1 = self.ctr1+ 1

    def addctr2(self):  # function for adding ctr2 to itself
        self.ctr2 = self.ctr2+ 1



# --------- Paul Kokhanov's code ---------
# class backround for placement of background
class background(pygame.sprite.Sprite):
  # initializing class variables
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("images/Background.fw.png").convert_alpha()
    self.background_mask = pygame.mask.from_surface(self.image)
    self.rect = self.image.get_rect()
    self.x = 0
    self.y = 0

# class enemy for controlling placement of enemy images
class enemy(pygame.sprite.Sprite):
  def __init__(self, x, y, picture):
      # initializing class variables
      pygame.sprite.Sprite.__init__(self)
      self.width = 50
      self.image = pygame.transform.scale(pygame.image.load(picture).convert_alpha(),(self.width, self.width))
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

# class boss for controlling placement of the boss
class boss(pygame.sprite.Sprite):
  def __init__(self, x, y, picture):
      # initializing class variables
      pygame.sprite.Sprite.__init__(self)
      self.width = 100
      self.image = pygame.transform.scale(pygame.image.load(picture).convert_alpha(),(self.width, self.width))
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y

# class player controlling placement and movement of the player
class player(pygame.sprite.Sprite):
 def __init__(self):
     # initializing class variables
     pygame.sprite.Sprite.__init__(self)
     self.width = 50
     self.image = pygame.transform.scale(pygame.image.load('images/Red_Circle(small).svg.png').convert_alpha(), (self.width, self.width))
     self.player_mask = pygame.mask.from_surface(self.image)
     self.rect = self.image.get_rect()
     self.rect.x = 100
     self.rect.y = 300
     self.vel = 5

 def left_move(self): # function for moving player left
     self.rect.x -= self.vel

 def right_move(self): # function for moving player right
     self.rect.x += self.vel

 def up_move(self): # function for moving player up
     self.rect.y -= self.vel

 def down_move(self): # function for moving player down
     self.rect.y += self.vel

 def checkcollision(self): # function for checking colision between player and the wall
     if self.rect.x <= 85:
         self.rect.x += self.vel
     if self.rect.x >= 1085:
         self.rect.x -= self.vel
     if self.rect.y <= 90 and self.rect.x <= 600:
         self.rect.y += self.vel
     if self.rect.y <= 75 and self.rect.x >= 830:
         self.rect.y += self.vel
     if self.rect.y >= 535 and self.rect.x <= 600:
         self.rect.y -= self.vel
     if self.rect.y >= 550 and self.rect.x >= 830:
         self.rect.y -= self.vel
     if self.rect.x >= 475 and self.rect.y >= 370 and self.rect.x <= 840:
         if keys[pygame.K_RIGHT] and self.rect.x >= 475 and self.rect.y > 370 and self.rect.x <= 840:
             self.rect.x -= self.vel
         if keys[pygame.K_LEFT] and self.rect.x >= 475 and self.rect.y > 370 and self.rect.x <= 840:
             self.rect.x += self.vel
         if keys[pygame.K_DOWN] and self.rect.y >= 370 and self.rect.x >= 475 and self.rect.x <= 840:
             self.rect.y -= self.vel
     if self.rect.x >= 475 and self.rect.y <= 225 and self.rect.x <= 840:
         if keys[pygame.K_RIGHT] and self.rect.x >= 475 and self.rect.y < 225 and self.rect.x <= 840:
             self.rect.x -= self.vel
         if keys[pygame.K_LEFT] and self.rect.x >= 475 and self.rect.y < 225 and self.rect.x <= 840:
             self.rect.x += self.vel
         if keys[pygame.K_UP] and self.rect.x >= 475 and self.rect.y <= 225 and self.rect.x <= 840:
             self.rect.y += self.vel



#------- Simha Kalimipalli's code --------
# function text_objects for defining aspects of small,medium and large text on screen
def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "semimed":
        textSurface = semimidfont.render(text, True, color)
    return textSurface, textSurface.get_rect()


# function text_to_botton places text on the button
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    screen.blit(textSurf, textRect)


# button function for controlling aspects of the buttons
def button(text, x, y, width, height, inactive_color, active_color, action=None):

    # initiallize global variables
    global score_cnt
    global visMode

    # initiallizing cur and click
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    # button condition
    if x + width > cur[0] > x and y + height > cur[1] > y:

        # draws button
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit": # actons performed if button action is quit
                pygame.quit()
                quit()

            if action == "incorrect": # actons performed if button action is incorrect
                incorrectscore = 0
                incorrectscore += 1
                bob = 0
                #print("bob is " + str(bob))
                #print("incorrect score is " + str(incorrectscore))
                score_list[ctr] = 0
                #print(score_list)
                # visMode = True

            if action == "correct": # actons performed if button action is correct
                score_cnt += 1
                #print(" New correct score is " + str(score_cnt))
                bob = 1
                #print("bob is " + str(bob))
                score_list[ctr] = 1
                #print(score_list)
                # visMode = True

                # score(1)
            if action == "controls": # actons performed if button action is controls
                pass

            if action == "play":
                print("Hello")
                game_tracker = 1
                draw = 0
    else:
        # makes the button the inactive colour
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    # places text (answers) on the button
    text_to_button(text, black, x, y, width, height)


# Function for drawing text on the screen that is coloured white
def display_text_color(message, setx_m, sety_m):
    my_text = message
    our_font = pygame.font.SysFont("Calibri", 28)
    produce_text = our_font.render(my_text, 1, white)
    screen.blit(produce_text, (setx_m, sety_m))

# Function for drawing text on the screen that can be multi coloured
def display_text(message, setx_m, sety_m, colour):
    my_text = message
    our_font = pygame.font.SysFont("Calibri", 28)
    produce_text = our_font.render(my_text, 1, colour)
    screen.blit(produce_text, (setx_m, sety_m))




# reduntant code for game intro
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        screen.fill(white)
        message_to_screen("Welcome to Trivia", green, -100, size="large")
        # message_to_screen("Press C to play, P to pause or Q to quit",black,180)

        button("play", 150, 500, 100, 50, green, green, action="play")
        #button("controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        #button("quit", 550, 500, 100, 50, red, light_red, action="quit")
        pygame.display.update()

        clock.tick(15)

# ______MAIN PROGRAM STARTS___________

# reading files to create four files
fname1 = "data/NEWQuestion1.csv"
fname2 = "data/NEWQuestion2.csv"
fname3 = "data/NEWQuestion3.csv"
fname4 = "data/Question4.csv"

# inputting four files to create 4 bankclass objects
B1 = BankClass(fname1)
B1.createBank()
B2 = BankClass(fname2)
B2.createBank()
B3 = BankClass(fname3)
B3.createBank()
B4 = BankClass(fname4)
B4.createBank()

# creating scorelist
global score_list
score_list = []
for i in range(0,len(B1.bank)):
    score_list.append(0)


#-------- Paul Kokhanov's code -------
# create sprites
player_one = player()
enemy_one = enemy(300, 80, "images/badguy 1 top.png")
enemy_two = enemy(470, 540, "images/badguy 2 top.png")
enemy_three = enemy(790, 300, "images/badguy 3 top.png")
boss = boss(970, 350, "images/bigboss top.png")

# Creating the downward moving spiders for the background screen
spider_one = spider(200, 0, 3)
spider_two = spider(540, 0, 4)
spider_three = spider(350, 0, 6)
spider_four = spider(640, 0, 8)
spider_five = spider(850, 0, 10)


# Creating the sideways moving spiders for the background screen
spiderside_one = spiderside(0,130, 13)
spiderside_two = spiderside(0,420, 20)

#background_one = background()

# Creating a sprite class group
draw_Group = pygame.sprite.Group()
#draw_Group.add(background_one)

# Adding the players and the enemies to the sprite group
draw_Group.add(player_one)
draw_Group.add(enemy_one)
draw_Group.add(enemy_two)
draw_Group.add(enemy_three)
draw_Group.add(boss)

# Text for starting ab= battle
battle_text = "Battle!"
initial_fight_text = "Escape?"




#------- Simha Kalimipalli's code --------
# Creating next button
buttonNext = pygbutton.PygButton((800, 400, 200, 100), 'Next')


# giving button text a font and size
buttonNext.font = pygame.font.SysFont('Arialbold', 44)  # Unfortunately, this line will only work on Windows machines.
buttonNext.buttonFgColor = blue

# making the button invisible
visMode = False

# variables required for the loop
ctr= 0
ctr1 = 0

# variable Draw for drawing different screens
#draw = -1 is the actual sequence
draw = -1
# test sequence
#draw = 3

killed = 0 # variable killed for spider collisions

# loading the music into the game
music1 = pygame.mixer.music.load('sounds/BackgroundMusic3.mp3')
pygame.mixer.music.play(-1)

# intiallizing game tracker as zero
game_tracker = 0

# initiallizing the gameover variables for telling when a quiz has been finished
quiz1_over = 0
quiz2_over = 0
quiz3_over = 0
quiz4_over = 0

# redundant - creating variabes for the computer score
#a2 = random.randint(0, len(B2.bank))
#a3 = random.randint(0, len(B3.bank))
#a4 = random.randint(0, len(B4.bank))

#creating variabes for the computer score
a2 = 0
a3 = 0
a4 = 0
#print(a2)
#print(a3)
#print(a4)
#print("ggggg")

# initiallizing variable running for while loop
running = True





#------- Paul Kokhanov's code ---------
# initialing pygame clock
clock = pygame.time.Clock()

# ____________ Main program while loop
while running:
 # intialling frames per second
 clock.tick(32)

 # Making next button invisible
 buttonNext.visible = False

# initialling variable keys for stimulus form keyboard
 keys = pygame.key.get_pressed()

 # _________Main program for loop
 for event in pygame.event.get():

     # quits game
     if event.type == pygame.QUIT:
         running = False

     # actions to be done if draw is 2 (first battle)



     # ------- Simha Kalimipalli's code --------
     if draw == 2:
         if ctr <= (len(B1.bank)) - 1:

             # generates random number for enemy score
             a1 = random.randint(0, len(B1.bank))

             # makes next button visible
             buttonNext.visible = True
             visMode = False

             screen.fill(black) # fills screen with the colour black

             # background picture for quiz
             screen.blit(bobbyJenkins, (0, 0))

             # prints quiz questions
             display_text_color(B1.bank[ctr].question, 200, 100)
             display_y = 200 # display_y for questions

             #for loop that goes through all of the answers in a list
             for i in range(0, len(B1.bank[ctr].answerslist)):

                 # decides whether an answer is right or wrong using data from CSV
                 if B1.bank[ctr].correctans == i:
                     correct_string = "correct"
                 else:
                     correct_string = "incorrect"

                 # draws option buttons
                 button(B1.bank[ctr].answerslist[i], 200, display_y, 500, 50, red, light_red, action=correct_string)
                 display_y = display_y + 100

                 # updates progress bar
                 display_text_color("Progress:", 850, 40)
                 pygame.draw.rect(screen, white, [850, 70, (20*len(B1.bank)) , 10],2)
             pygame.draw.rect(screen, white, [850, 70, (20*ctr), 10], )

         # if questions are over
         else:
             screen.fill(black) # fils screen black
             screen.blit(scorescreen, (0, 0)) # displays screen screen image
             sum1 = 0 # reset variable sum1

             # adds total score
             for i in range(0, len(score_list)):
                 sum1 = sum1 + score_list[i]

            # draws rectangle for quiz results
             s = pygame.Surface((400, 400), pygame.SRCALPHA)  # per-pixel alpha
             s.fill((100, 100, 100, 240))  # notice the alpha value in the color
             screen.blit(s, (480, 20))
             pygame.draw.rect(screen, red, [480, 20, 400, 400], 5)

            # text of quiz results
             display_text_color("Out of " + str(len(B1.bank)) + " Questions", 500, 100)
             display_text_color("You got " + str(sum1) + " questions right", 500, 150)
             lenbank2 = len(B1.bank)
             # display_text_color("Or " + str((sum1/lenbank2)*100) + "%", 500, 150)
             display_text_color("Your enemy got " + str(a1) + " questions right ", 500, 200)

            # if player score is greater than computer score
             if a1 <= sum1:
                 display_text_color("you win!", 500, 300)
                 display_text_color("Press SPACE to exit", 500, 350)

                 # resets player to their original location
                 if keys[pygame.K_SPACE]:
                     draw = 0
                     player_one.rect.x = 100
                     player_one.rect.y = 300

                 quiz1_over = 1 # end of quiz 1

                 # Makes enemys image go away
                 enemy_one.rect.x = 1000
                 enemy_one.rect.y = 1000

            # if computer score is greater than player score
             else:
                 # rectangle for play again box
                 pygame.draw.rect(screen, red, [500, 300, 200, 50])

                 display_text_color("play again", 550, 310) # text for play again box

                 # button for play again box
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:
                         # resetting variables
                         quiz1_over = 0
                         ctr = 0
                         draw = 2

         buttonNext.draw(screen) # updates button on screen
#---------------------------------------------------------------------

     # actions to be done if draw is 3 (second battle)
     if draw == 3:
         if ctr <= (len(B2.bank)) - 1:

             # generates random number for enemy score
             a2 = random.randint(0, len(B3.bank))

            # makes next button visible
             buttonNext.visible = True
             visMode = False

             screen.fill(black) # fills the screen black

             # background picture for quiz
             screen.blit(bobbyJenkins, (0, 0))

             # prints quiz questions
             display_text_color(B2.bank[ctr].question, 200, 100)
             display_y = 200 # display y for questions

             # for loop that goes through all of the answers in a list
             for i in range(0, len(B2.bank[ctr].answerslist)):

                 # decides whether an answer is right or wrong using data from CSV
                 if B2.bank[ctr].correctans == i:
                     correct_string = "correct"
                 else:
                     correct_string = "incorrect"

                # draws option buttons
                 button(B2.bank[ctr].answerslist[i], 200, display_y, 500, 50, red, light_red, action=correct_string)
                 display_y = display_y + 100

                 # updates progress bar
                 display_text_color("Progress:", 800, 40)
                 pygame.draw.rect(screen, white, [800, 70, (20 * len(B2.bank)), 10], 2)
             pygame.draw.rect(screen, white, [800, 70, (20 * ctr), 10], )

         # if questions are over
         else:
             screen.fill(black) # fills screen black
             screen.blit(scorescreen, (0, 0)) # displays screen image
             sum1 = 0 # resets variable sum1

            # adds total score
             for i in range(0, len(score_list)):
                 sum1 = sum1 + score_list[i]

            # draws rectangle for quiz results
             s = pygame.Surface((400, 400), pygame.SRCALPHA)  # per-pixel alpha
             s.fill((100, 100, 100, 240))  # notice the alpha value in the color
             screen.blit(s, (480, 20))
             pygame.draw.rect(screen, red, [480, 20, 400, 400], 5)

             # text of quiz results
             display_text_color("Out of " + str(len(B2.bank)) + " Questions", 500, 100)
             display_text_color("You got " + str(sum1) + " questions right", 500, 150)
             lenbank2 = len(B2.bank)
             #display_text_color("Or " + str((sum1/lenbank2)*100) + "%", 500, 150)
             display_text_color("Your enemy got " + str(a2) + " questions right ", 500,200)

             # if player score is greater than computer score
             if a2 <= sum1:
                 display_text_color("you win!", 500, 300)
                 display_text_color("Press SPACE to exit", 500, 350)

                 # resets player to original location
                 if keys[pygame.K_SPACE]:
                     draw = 0
                     player_one.rect.x = 100
                     player_one.rect.y = 300

                 quiz2_over = 1 # end of quiz 2

                 # makes enemy imagtes go away
                 enemy_two.rect.x = 1000
                 enemy_two.rect.y = 1000

            # if computer score is greater than player score
             else:
                 # rectangle for play again box
                 pygame.draw.rect(screen, red, [500, 300, 200, 50])

                # text for polay again box
                 display_text_color("play again", 550, 310)

                 # button for play again box
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:

                         # resets variables
                         quiz2_over = 0
                         ctr = 0
                         draw = 3


         buttonNext.draw(screen)
#----------------------------------------------------------
     if draw == 4:
         if ctr <= (len(B3.bank)) - 1:
             # generates random number for enemy score
             a3 = random.randint(0, len(B3.bank))

             # makes next button visible
             buttonNext.visible = True
             visMode = False

             screen.fill(black)  # fills the screen black

             # background picture for quiz
             screen.blit(bobbyJenkins, (0, 0))

             # prints quiz questions
             display_text_color(B3.bank[ctr].question, 200, 100)
             display_y = 200 # display_y for questions

             # for loop that goes through all of the answers in a list
             for i in range(0, len(B3.bank[ctr].answerslist)):

                 # decides whether an answer is right or wrong using data from CSV
                 if B3.bank[ctr].correctans == i:
                     correct_string = "correct"
                 else:
                     correct_string = "incorrect"

                 # draws option buttons
                 button(B3.bank[ctr].answerslist[i], 200, display_y, 500, 50, red, light_red, action=correct_string)
                 display_y = display_y + 100

                 # updates progress bar
                 display_text_color("Progress:", 800, 40)
                 pygame.draw.rect(screen, white, [800, 70, (20 * len(B3.bank)), 10], 2)
             pygame.draw.rect(screen, white, [800, 70, (20 * ctr), 10], )

         # if questions are over
         else:
             screen.fill(black) # fils screen black
             screen.blit(scorescreen,(0,0)) # displays screen image
             sum1 = 0 # resets variable sum1

             # adds total score
             for i in range(0, len(score_list)):
                 sum1 = sum1 + score_list[i]
             display_text_color("The Score is " + str(sum1), 200, 100)

             # draws rectangle for quiz results
             s = pygame.Surface((400, 400), pygame.SRCALPHA)  # per-pixel alpha
             s.fill((100, 100, 100, 240))  # notice the alpha value in the color
             screen.blit(s, (480, 20))
             pygame.draw.rect(screen, red, [480, 20, 400, 400], 5)

             # text of quiz results
             display_text_color("Out of " + str(len(B3.bank)) + " Questions", 500, 100)
             display_text_color("You got " + str(sum1) + " questions right", 500, 150)
             lenbank2 = len(B3.bank)
             # display_text_color("Or " + str((sum1/lenbank2)*100) + "%", 500, 150)
             display_text_color("Your enemy got " + str(a3) + " questions right ", 500, 200)

             # if player score greater than computer score
             if a3 <= sum1:
                 display_text_color("you win!", 500, 300)
                 display_text_color("Press SPACE to exit", 500, 350)

                 # resets player to original location
                 if keys[pygame.K_SPACE]:
                     draw = 0
                     player_one.rect.x = 100
                     player_one.rect.y = 300

                 quiz3_over = 1 # end of quiz 3

                 # makes enemy images go away
                 enemy_three.rect.x = 1000
                 enemy_three.rect.y = 1000

             # if computer score is greater than player score
             else:
                 # rectangle for play again box
                 pygame.draw.rect(screen, red, [500, 300, 200, 50])

                # text for player again box
                 display_text_color("play again", 550, 310)

                 # button for player again box
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300 and \
                             pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:

                         # resets variables
                         quiz2_over = 0
                         ctr = 0
                         draw = 3


         buttonNext.draw(screen)
#--------------------------------------
     if draw == 5:
         if ctr <= (len(B4.bank)) - 1:
             # generates random number for enemy score
             a4 = random.randint(0, len(B3.bank))

             # makes next button visible
             buttonNext.visible = True
             visMode = False

             screen.fill(black)  # fills the screen black

             # background picture for quiz
             screen.blit(bobbyJenkins, (0, 0))

             # prints quiz questions
             display_text_color(B4.bank[ctr].question, 200, 100)
             display_y = 200 # display_y for questions

             # for loop that goes through all of the answers in a list
             for i in range(0, len(B4.bank[ctr].answerslist)):

                 # decides whether an answer is right or wrong using data from CSV
                 if B4.bank[ctr].correctans == i:
                     correct_string = "correct"
                 else:
                     correct_string = "incorrect"

                 # draws option buttons
                 button(B4.bank[ctr].answerslist[i], 200, display_y, 500, 50, red, light_red, action=correct_string)
                 display_y = display_y + 100

                 # updates progress bar
                 display_text_color("Progress:", 800, 40)
                 pygame.draw.rect(screen, white, [800, 70, (20 * len(B4.bank)), 10], 2)
             pygame.draw.rect(screen, white, [800, 70, (20 * ctr), 10], )

         # if questions are over
         else:
             screen.fill(black) # fills screen black
             screen.blit(scorescreen, (0, 0)) # displays screen image
             sum1 = 0 # resets variable sum1

             # adds total score
             for i in range(0, len(score_list)):
                 sum1 = sum1 + score_list[i]
             display_text_color("The Score is " + str(sum1), 200, 100)
             # a = random.randint(0, len(score_list))

            # draws rectangle for quiz results
             s = pygame.Surface((400, 400), pygame.SRCALPHA)  # per-pixel alpha
             s.fill((100, 100, 100, 240))  # notice the alpha value in the color
             screen.blit(s, (480, 20))
             pygame.draw.rect(screen, red, [480, 20, 400, 400], 5)

             # draws text of quiz results
             display_text_color("Out of " + str(len(B4.bank)) + " Questions", 500, 100)
             display_text_color("You got " + str(sum1) + " questions right", 500, 150)
             lenbank2 = len(B3.bank)
             # display_text_color("Or " + str((sum1/lenbank2)*100) + "%", 500, 150)
             display_text_color("Your enemy got " + str(a4) + " questions right ", 500, 200)

             # if player score is greater than computer score
             if a4 <= sum1:
                 display_text_color("you win!", 500, 300)
                 display_text_color("Press SPACE to exit", 500, 350)

                 # takes user to you win screen
                 if keys[pygame.K_SPACE]:
                     draw = -3

                 quiz4_over = 1 # end of quiz 4

                 # makes boss go away
                 boss.rect.x = 1000
                 boss.rect.y = 1000

            # if computer score is greater than player score
             else:
                 # rectange for player again box
                 pygame.draw.rect(screen, red, [500, 300, 200, 50])

                 # text for player agian box
                 display_text_color("play again", 550, 310)

                 # button for polay again box
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     if pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 300 and \
                             pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 350:

                         # resets variables
                         quiz4_over = 0
                         ctr = 0
                         draw = 3

         buttonNext.draw(screen) # updates utton on screen


      # ----------------------------

     # Makes screens incres when hitting the next button
     if 'click' in buttonNext.handleEvent(event):
         ctr = ctr + 1
         #print("draw" + str(draw))

     pygame.display.update() # updates screen




#------ Paul Kokhanov's code -------
# background screen
 if draw == 0:

    # calling function makes the spider walk downwards
       spider_one.down_walk()
       spider_two.down_walk()
       spider_three.down_walk()
       spider_four.down_walk()
       spider_five.down_walk()

    #  calling function Makes the spider walk downwards
       spiderside_one.side_walk()
       spiderside_two.side_walk()

       # calling function that makes player move left
       if keys[pygame.K_LEFT]:
         player_one.left_move()

       # calling function that makes player move right
       if keys[pygame.K_RIGHT]:
         player_one.right_move()

       # calling function that makes player move up
       if keys[pygame.K_UP]:
         player_one.up_move()

       # calling function that makes player move down
       if keys[pygame.K_DOWN]:
         player_one.down_move()

       screen.blit(background_floor,(0,0)) # draws backround image

       draw_Group.update() # updates draw group

       draw_Group.draw(screen) # draws draw group on the screen

       # draws the downward moving spiders on the screen
       spider_one.draw(screen)
       spider_two.draw(screen)
       spider_three.draw(screen)
       spider_four.draw(screen)
       spider_five.draw(screen)

       # Draws the sideways moving spiders on the screen
       spiderside_one.draw(screen)
       spiderside_two.draw(screen)

       screen.blit(background_image, (0, 0)) # displays background

        # counter for spider collisions
       display_text("You hit " + str(killed) + "  Spiders", 575, 50, white)

       pygame.display.flip() # Updates screen

       # checks if player has hit 10 spiders
       if killed >= 10:
           draw = -4


        # collsions between player and downward spiders
       spider_one_collision = player_one.rect.colliderect(spider_one)
       spider_two_collision = player_one.rect.colliderect(spider_two)
       spider_three_collision = player_one.rect.colliderect(spider_three)
       spider_four_collision = player_one.rect.colliderect(spider_four)
       spider_five_collision = player_one.rect.colliderect(spider_five)

       # collsions between player and sideways spiders
       spiderside_one_collision = player_one.rect.colliderect(spiderside_one)
       spiderside_two_collision = player_one.rect.colliderect(spiderside_two)

       # collsions between player and enemies
       result_one = player_one.rect.colliderect(enemy_one.rect)
       result_two = player_one.rect.colliderect(enemy_two.rect)
       result_three = player_one.rect.colliderect(enemy_three.rect)
       result_four = player_one.rect.colliderect(boss.rect)

    # returns player  to the start if they hit a spider
       if spider_one_collision or spider_two_collision or spider_three_collision or spiderside_one_collision or spiderside_two_collision or spider_four_collision or spider_five_collision:
           killed += 1
           player_one.rect.x = 100
           player_one.rect.y = 300
           Spidersound.play()

    # actions if player  collides with enemy 1
       if result_one:
         draw = 1
         result_two = False
         result_three = False
         result_four = False
         game_tracker = game_tracker + 1
         #print("game_tracker result_one "+str(game_tracker))

       # actions if player  collides with enemy 2
       if result_two:
         draw = 1
         result_one = False
         result_three = False
         result_four = False
         game_tracker = game_tracker + 1
         #print("game_tracker result_two "+str(game_tracker))

       # actions if player  collides with enemy 3
       if result_three:
         draw = 1
         result_one = False
         result_two = False
         result_four = False

         # actions if player  collides with big boss
       if result_four:
           draw = 1
           result_one = False
           result_two = False
           result_three = False





# -------- Simha Kalimipalli's code -------
# draws the battle screens
 if draw == 1:

         screen.fill(black) # fills the screen black

         # battle screen for quiz 1
         if quiz1_over == 0:
             pygame.draw.polygon(screen, grey, [(0, 100), (300, 100), (500, 713),(0, 713)])
             pygame.draw.polygon(screen, grey, [(712, 0), (1212, 0), (1212, 613),(900,613)])
             screen.blit(jeff, (10, 213))
             screen.blit(badguy1, (947, 0))

        # battle screen for quiz 2
         if quiz1_over == 1:
             pygame.draw.polygon(screen, grey, [(0, 100), (300, 100), (500, 713), (0, 713)])
             pygame.draw.polygon(screen, grey, [(712, 0), (1212, 0), (1212, 613), (900, 613)])
             screen.blit(badguy2, (947, 0))
             screen.blit(jeff, (10, 213))

         # battle screen for quiz 3
         if quiz2_over == 1:
             pygame.draw.polygon(screen, grey, [(0, 100), (300, 100), (500, 713), (0, 713)])
             pygame.draw.polygon(screen, grey, [(712, 0), (1212, 0), (1212, 613), (900, 613)])
             screen.blit(badguy3, (947, 0))
             screen.blit(jeff, (10, 213))

         # battle screen for quiz 4
         if quiz3_over == 1:
             pygame.draw.polygon(screen, grey, [(0, 100), (300, 100), (500, 713), (0, 713)])
             pygame.draw.polygon(screen, grey, [(712, 0), (1212, 0), (1212, 613), (900, 613)])
             screen.blit(bigboss, (900, 0))
             screen.blit(jeff, (10, 213))

         battle_text_surface = largefont.render(battle_text, True,white)  # make a variable "computer_surface" equal to string "computer" with a mediumfont
         screen.blit(battle_text_surface, (420, 150))  # display "computer_surface" to the screen

        # draws the boxes for the button
         pygame.draw.rect(screen, lightgrey, [350, 100, 390, 150], 5)
         pygame.draw.rect(screen, lightgrey, [447, 400, 390, 150], 5)

         initial_fight_text_surface = largefont.render(initial_fight_text, True,white)  # make a variable "computer_surface" equal to string "computer" with a mediumfont
         screen.blit(initial_fight_text_surface, (517, 450))  # display "computer_surface" to the screen
         pygame.display.flip()

        # button that starts the game from battle screen
         if event.type == pygame.MOUSEBUTTONDOWN:
             if pygame.mouse.get_pos()[0] >= 350 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1] <= 250:

                 #print("Which Quiz..")

                # Starts quiz 1
                 if quiz1_over == 0:
                     #print("Quiz 1")
                     draw = 2

                 # Starts quiz 2
                 if quiz1_over == 1:
                     #print("Quiz 2")
                     ctr = 0
                     score_list = []
                     for i in range(0, len(B2.bank)):
                         score_list.append(0)
                     draw = 3

                 # Starts quiz 3
                 if quiz2_over == 1:
                     #print("Quiz 3")
                     ctr = 0
                     score_list = []
                     for i in range(0, len(B3.bank)):
                         score_list.append(0)
                     draw = 4

                 # Starts quiz 4
                 if quiz3_over == 1:
                     #print("Quiz 4")
                     ctr = 0
                     score_list = []
                     for i in range(0, len(B4.bank)):
                         score_list.append(0)
                     #print("hello there!")
                     draw = 5

         # Escapes the enemy from battle screen
         if event.type == pygame.MOUSEBUTTONDOWN:
             if pygame.mouse.get_pos()[0] >= 447 and pygame.mouse.get_pos()[1] >= 400 and pygame.mouse.get_pos()[0] <= 837 and pygame.mouse.get_pos()[1] <= 550:
                 draw = 0
                 player_one.rect.x =100
                 player_one.rect.y = 300



#------ Paul Kokhanov's code --------
# Starting screen
 if draw == -1:
    screen.fill(black) # fills screen black

    # background image and logo for starting game
    screen.blit(initial_background,(0,-180))
    screen.blit(logo, (100, 200))

    # text for starting screen
    display_text("Play Now!", 680, 510, white)
    display_text("Instructions", 680, 610, white)



    #------ Simha Kalimipalli's code --------
    # button images
    pygame.draw.rect(screen, lightgrey, [650,500, 200, 50],5 )
    pygame.draw.rect(screen, lightgrey, [650, 600, 200, 50],5 )

    # Buttons to start the game
    if  event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 650 and pygame.mouse.get_pos()[1] >= 500 and pygame.mouse.get_pos()[0] <= 850 and pygame.mouse.get_pos()[1] <= 550:
                    draw = 0

    # Buttons to go to the instructions
    if  event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 650 and pygame.mouse.get_pos()[1] >= 600 and pygame.mouse.get_pos()[0] <= 850 and pygame.mouse.get_pos()[1] <= 650:
                    draw = -2

 # Instruction screen
 if draw == -2:
     screen.fill(black)
     display_text("Instructions for the game:", 100, 100, white)
     # Array containing instrcutions for the game
     instructions = [ \
                     "You can move freely in the area that is given", \
                     "Don't hit any spiders - if you hit 10 of them you lose",\
                     "To start a battle, you must collide with 3 enemies one by one", \
                     "When in a battle, you must answer the questions that are shown", \
                     "To beat an enemy, you must have more correct answers than the enemy", \
                     "Start with black-haired dude then go to yellow haired dude ", \
                     "After that, go to brown haired dude", \
                     "Once all three enemies are beaten, the room with the boss will open", \
                     "You must collide with the boss enemy to initiate battle", \
                     "Once the boss is beaten, YOU WIN"]

     # displays questions on screen
     y = 200
     for i in instructions:
         instruction_text = smallfont.render(i, False, (255, 255, 255))
         screen.blit(instruction_text, (100, y))
         y = y + 30

     screen.blit(logo, (900, 190))

     # Back button text
     display_text("Back", 200, 600, white)

     # Rectangle outline for instructions and back button
     pygame.draw.rect(screen, red, [90, 190, 780, 320], 5)
     pygame.draw.rect(screen, lightgrey, [190, 590, 200, 50], 5)

    # button to get back to the home screen
     if event.type == pygame.MOUSEBUTTONDOWN:
         if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[1] >= 600 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] <= 650:
             draw = -1

#------ Paul Kokhanov's code -------
# Screen once you win the game
 if draw == -3:
    screen.fill(black) # Fill screen black
    screen.blit(win1, (200,0)) # Win screen picture


 # Screen if you lose the game
 if draw == -4:
    screen.fill(black) # Fill screen black
    screen.blit(lose1, (200,0)) # lose screen picture

# checks collsion between player and the enemies
 player_one.checkcollision()

 #1070

