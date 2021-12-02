#cpsc3720

import pygame, sys, random, time, pygame_menu
from database.database import Database
check_errors = pygame.init()

#make sure initializes correctly
if check_errors[1] > 0:
    print("(!) had {0} initializing errors, exiting....".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(!) PyGame Initialized Successfully")

pygame.init()

#use this to know if start screen or not
activeRouund = False
#starts here -> once press start say round
currentScreen = 'Start'

X = 720
Y = 460
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('\ (•◡•) / CHARADES \ (•◡•) /')
pygame.display.flip()

screenW = screen.get_width()
screenH = screen.get_height()

clock = 60
font = pygame.font.SysFont('arial', 30)
smallFont = pygame.font.SysFont('arial', 20)
medFont = pygame.font.SysFont('arial', 25)

orange = (245, 102,0)
blue = (0, 32, 91)
purple = (46,26,71)

genre_menu = pygame_menu.Menu('Select Genre', X, Y, theme=pygame_menu.themes.THEME_BLUE)
main_menu = pygame_menu.Menu('Charades', X, Y, theme=pygame_menu.themes.THEME_BLUE)
play_menu = pygame_menu.Menu('Play', X, Y, theme=pygame_menu.themes.THEME_BLUE)
end_menu = pygame_menu.Menu('Time Up!', X, Y, theme=pygame_menu.themes.THEME_BLUE)

genre_menu.disable()
main_menu.disable()
play_menu.disable()
end_menu.disable()

db = Database()
selected_words = []

def activeRound():
    active = font.render('ACTIVE ROUND', True, purple) 
    activeRect = active.get_rect()
    activeRect.midtop = (360, 15)
    screen.blit(active, activeRect) 
    instructions = smallFont.render('Act out the word below', True, purple) 
    instructionsRect = instructions.get_rect()
    instructionsRect.midtop = (360, 50)
    screen.blit(instructions, instructionsRect) 

def nextCardButton():
    nextButtonText = font.render('Next Card', True, orange)
    #creating next button
    nextButton = nextButtonText.get_rect()
    #set center of next button
    nextButton.midbottom = screenW/2,screenH/2+85
    #create button
    pygame.draw.rect(screen, purple,[screenW/2-72,screenH/2+50, 145,40])
    #but text onto the button
    screen.blit(nextButtonText, nextButton)

def currentCard():
    currCard = font.render('[CARD]', True, blue) 
    currCardRect = currCard.get_rect()
    currCardRect.midtop = (X/2, Y/2-40)
    screen.blit(currCard, currCardRect) 

def selectScreen():
    screen.fill((0,0,0))
    #menu.add.menu_link()
    genre_menu.enable()
    genre_menu.add.button('History', currentCard('History'))
    genre_menu.add.button('Celebrities', currentCard('Celebrities'))
    genre_menu.add.button('Movies', currentCard('Movies'))
    #genre_menu.mainloop(screen)
    

def currentCard(genre_str):
    genre_menu.disable()
    genre_menu.full_reset()
    play_menu.enable()
    selected_words = db.get_cards([genre_str])
    word = selected_words[random.randint(0,len(selected_words)-1)]

    #menu = pygame_menu.Menu(genre_str, 720, 400, theme=pygame_menu.themes.THEME_BLUE)
    play_menu.add.label(word, word)
    #play_menu.mainloop(screen)

    #currCard = font.render(word, True, blue) 
    #currCardRect = currCard.get_rect()
    #currCardRect.midtop = (X/2, Y/2-40)
    #screen.blit(currCard, currCardRect) 


#cocntroller
fpsController = pygame.time.Clock()

# def mousePressend(event):
#     if(activeRouund == 'Round'):
#         #if next key pressed -> add draw a new card

# sets timer to activate once per 1000 ms
pygame.time.set_timer(pygame.USEREVENT, 1000)

#game logic
while True:
    screen.fill((255,255,255))

    #the timer
    timer = medFont.render('Time left: ' + str(clock), True, orange)
    screen.blit(timer, (290, 75))
    for event in pygame.event.get():
        #quitting
        if event.type == pygame.QUIT: 
            pygame.quit()

        # condition to catch timer activation
        elif event.type == pygame.USEREVENT:
            clock -= 1
            # condition to stop timer at 0
            if clock <= 0:
                clock = 0 ; pygame.time.set_timer(pygame.USEREVENT, 0)

        # restarts timer at 60 on key [r] pressed 
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            clock = 60 ; pygame.time.set_timer(pygame.USEREVENT, 1000)   

        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    if screenW/2-65 <= mouse[0] <= screenW/2-65+140 and screenH/2+50 <= mouse[1] <= screenH/2+50+40:
        #        pass
        #        
        
        #get the pos of the mouse so we can know which button
        mouse = pygame.mouse.get_pos()
        selectScreen()
        genre_menu.enable()
        genre_menu.mainloop(screen)
        #activeRound()
        #nextCardButton()
        #currentCard()

        #update game
        pygame.display.update()


#way selecting through the genres - buttons
#selecting genre -> timer 1min per player, 

