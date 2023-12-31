"""Sources Used for Code: 
https://www.techwithtim.net/tutorials/game-development-with-python/side-scroller-pygame/scoring-end-screen/
https://www.youngwonks.com/blog/How-to-Make-a-Side-Scroller-Game-using-Python-and-PyGame"""

import pygame
import random

pygame.font.init()

pygame.mixer.init()
pygame.mixer.music.load('t-for-temple.wav')
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((1049,519))
pygame.display.set_caption('Run, Hooter, Run')
obstacles = ['images/rosen sprite.png','images/t.png','images/cherry.png', 
             'images/basketball.png', 'images/football.png', "images/belltower spritee new.png"]
score = 0

def menu():
    image = pygame.image.load('images/menuplay.jpg')
    image = pygame.transform.scale(image, (1049,519))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(390,460) and event.pos[1] in range(140,205):
                    intro()

def intro():
    image = pygame.image.load('images/intro2.jpg')
    image = pygame.transform.scale(image, (1049,519))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(645,885) and event.pos[1] in range(380,482):
                    pygame.mixer.music.pause()
                    game()

def game():
    pygame.mixer.music.load('background-music.wav')
    pygame.mixer.music.play(-1)
    image = pygame.image.load('images/background 2.jpg')
    image = pygame.transform.scale(image, (1049,519))
    bgx = 0 

    player = pygame.image.load('images/owl sprite.png')
    player = pygame.transform.rotozoom(player,0,0.2)
    player_y = 400
    gravity = .8
    jump = False

#obstacle 1
    obs = pygame.image.load(random.choice(obstacles))
    obs = pygame.transform.rotozoom(obs, 0,0.8)
    obs_x = 1100
    obs_y = random.randint(0,400)
    obs_speed = random.uniform(.5,2)

#obstacle 2
    obs2 = pygame.image.load(random.choice(obstacles))
    obs2 = pygame.transform.rotozoom(obs2, 0,0.8)
    obs2_x = 1600
    obs2_y = random.randint(0,400)
    obs2_speed = random.uniform(.5,2)

    while True:
        global score
        score += 1
        pygame.init()
        screen.blit(image,(bgx-1049,0))
        screen.blit(image,(bgx,0))
        screen.blit(image,(bgx+1049,0))

        bgx = bgx - .1
        if bgx <= -1049:
            bgx = 0

        p_rect = screen.blit(player,(50, player_y))
        if player_y < 400:
            player_y += gravity
        if jump == True:
            player_y = player_y - 2
            if player_y < 0:
                player_y = 0
    
        o_rect = screen.blit(obs,(obs_x,obs_y))
        obs_x -= obs_speed

        o2_rect = screen.blit(obs2,(obs2_x,obs2_y))
        obs2_x -= obs2_speed

        if obs_x < -100:
            obs = pygame.image.load(random.choice(obstacles))
            obs = pygame.transform.rotozoom(obs, 0,0.8)
            obs_x = 1100
            obs_y = random.randint(0,400)
            obs_speed = random.uniform(.5,2)

        if obs2_x < -100:
            obs2 = pygame.image.load(random.choice(obstacles))
            obs2 = pygame.transform.rotozoom(obs2, 0,0.8)
            obs2_x = 1600
            obs2_y = random.randint(0,400)
            obs2_speed = random.uniform(.5,2)
              
        if p_rect.colliderect(o_rect) or p_rect.colliderect(o2_rect):
            pygame.mixer.music.pause()
            gameover()
        
        scoreboard()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jump = True
            if event.type == pygame.KEYUP:
                jump = False
        
#displaying scoreboard
def scoreboard():
    largeFont = pygame.font.SysFont('lucidasansregular', 30) # Font object
    text = largeFont.render('Score: ' + str(score), 1, (0,0,0),(255,255,255)) # create our text
    textW = text.get_width()
    screen.blit(text, (1030-textW, 10)) # draw the text to the screen
    pygame.display.update()

def gameover():
    global score
    image = pygame.image.load('images/gameover.jpg')
    image = pygame.transform.scale(image, (1049,519))
    pygame.mixer.music.load('lose-game.wav')
    pygame.mixer.music.play()
    while True:
        screen.blit(image,(0,0))
        endingScore()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(588,760) and event.pos[1] in range(411,480):
                    score = 0
                    game()

#displays ending score
def endingScore():
    largeFont = pygame.font.SysFont('lucidasansregular', 72) # creates a font object
    lastScore = largeFont.render(str(updateFile()),1,(0,0,0)) # We will create the function updateFile later
    currentScore = largeFont.render(str(score),1,(0,0,0))
    screen.blit(lastScore, (710,210))
    screen.blit(currentScore, (690,125))
    pygame.display.update()
    
#updates the highest score
def updateFile():
    f = open('scores.txt','r') # opens the file in read mode
    file = f.readlines() # reads all the lines in as a list
    last = int(file[0]) # gets the first line of the file

    if last < int(score): # sees if the current score is greater than the previous best
        f.close() # closes/saves the file
        file = open('scores.txt', 'w') # reopens it in write mode
        file.write(str(score)) # writes the best score
        file.close() # closes/saves the file
        return score     
    return last

menu()
