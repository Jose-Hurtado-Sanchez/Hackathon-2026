# Example file showing a basic pygame "game loop"
from networkx import cut_size
import pygame
import screen1
from player import Player 
import dorm
import random


# pygame setup
pygame.init()
SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
title_font = pygame.font.SysFont("Consolas", 60) # font type fob bigger text goes here 
sub_title_font = pygame.font.SysFont("Consolas", 30) # font type for smaller text here goes here 
small_text_font = pygame.font.SysFont("Consolas", 10) # font type for even smaller text here goes here 
day=1
maxDay =50
User = Player()
day_done = False 
entered_display_stats = False
pause_time = 0 
looped = 0
death_pause = 0

# colors
CRIMSON = (220, 20, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen_state = "starting_screen"

#button
full_button = pygame.Rect(0, 0, 1280, 720) #invisible button making the enttire intro screen clickable



#intro screen
game_title = title_font.render("THE WAZZU TRAIL",False,CRIMSON)
press_to_start = sub_title_font.render("Click Anywhere To Start",False, WHITE)
screen_rectangle = screen.get_rect() # turns screen into rectangle 
center_text = game_title.get_rect(center=screen_rectangle.center)
# position the "press to start" text just below the title
press_rect = press_to_start.get_rect(midtop=(screen_rectangle.centerx, center_text.bottom + 60)) 

goScreen1 = False

labels = ["Computer Science", "Buisness", "Nursing", "Kinesiology", "Liberal Arts"]
buttons = {}
x = 225
start_y = 300
w, h = 220, 60
gap = 20

for i, label in enumerate(labels):
    y = start_y + i * (h + gap) #each button gets a unique coordinate
    buttons[label] = pygame.Rect(x, y, w ,h)

choices = dorm.commands
choices_button = {}
x2 = 200
start_y2= 400 
w2, h2 = 880, 60
gap2 = 20
for i, choices in enumerate(choices):
    y = start_y2 + i * (h2 + gap2) #each button gets a unique coordinate
    choices_button[choices] = pygame.Rect(x, y, w ,h)


while running:
    #---  ALL EVENTS 
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #--button events--
    mouse_position = pygame.mouse.get_pos() #mouse position

    #checks to see if the user clicks down anywhere on the screen and then moves onto the intro screen    
    if event.type == pygame.MOUSEBUTTONDOWN and screen_state == "starting_screen":
        if full_button.collidepoint(event.pos):
            screen_state = "screen_1"

    #user clicks down and if it is inside the button it checks the label and then to the new dorm screen
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and screen_state == "screen_1":
        for label, rect in buttons.items():
            if rect.collidepoint(event.pos):
                User.major = label
                User.boostByMajor() #gives boost on major chosen 
                screen_state = "dorm"

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and screen_state == "dorm" and day_done==False: #pick option out of 3
        for choice, rect in choices_button.items():
            if rect.collidepoint(event.pos):
                day += 1
                day_done = True 
                print("Picked:", choice)
                User.update_user_stats(choice)
                print("Available keys: ", dorm.command_data.keys())
                screen_state = "display stats screen"
                pause_time = pygame.time.get_ticks()
                
                entered_display_stats = False
                break
        
    if screen_state == "display stats screen" and entered_display_stats == False: # display stats screen 
        screen.fill("dark grey")
        stats_font = pygame.font.Font(None, 100)
   
        print("ENTERED SCREEN STATS:")
        stats = {
            "Health": User.health,
            "Money": User.money,
            "Stress": User.stress,
            "Grade": User.grade,
            "Social_life_score": User.social_life_score
        }
        x = 200
        start_y= 320
        gap = 20
        for i, (label, values) in enumerate(stats.items()):
            y = start_y + i * (gap) #each button gets a unique coordinate
            text = small_text_font.render(f"{label}: {values}", True, (255,255,255))
            screen.blit(text,(x,y))

        if pygame.time.get_ticks() - pause_time > 5000:
            entered_display_stats = True
            screen_state = "dorm"
            day_done = False
            dorm.commands = random.sample(dorm.all_commands, 3)
            choices = dorm.commands
            choices_button = {}
            x2 = 200
            start_y2= 400 
            w2, h2 = 880, 60
            gap2 = 20
            for i, choice in enumerate(choices):
                y = start_y2 + i * (h2 + gap2) #each button gets a unique coordinate
                choices_button[choice] = pygame.Rect(x2, y, w2,h2)
            
    #--screen fill--
    # fill the screen with a color to wipe away anything from last frame

    if screen_state == "starting_screen" :
        screen.fill("dark grey")

        screen.blit(game_title,center_text)

        if pygame.time.get_ticks() % 900 < 400: # makes the 
            screen.blit(press_to_start, press_rect)

    if screen_state == "screen_1" :
        screen1.draw_screen1(screen) 
        for label, rect in buttons.items(): #loops through each button
            pygame.draw.rect(screen, "dark red", rect)

            text_surf = small_text_font.render(label,True, "white") #renders the button text
            text_rect = text_surf.get_rect(center = rect.center) #creates a rectangle
            screen.blit (text_surf, text_rect)

    if screen_state == "dorm" :
        screen.fill("dark grey")
        dorm.draw_dorm_screen(screen,User,day)
        for choices, rect in choices_button.items(): #loops through each button
            pygame.draw.rect(screen, "dark red", rect)
            text_surf = small_text_font.render(choices,True, "white") #renders the button text
            text_rect = text_surf.get_rect(center = rect.center) #creates a rectangle
            screen.blit (text_surf, text_rect)


    if( User.health <= 0 or User.grade <=0 or User.money <=0 or User.stress >=100) and looped >= 1:
        screen.fill("dark grey")

        User.death_screen(screen)
        if death_pause is 0:
            death_pause = pygame.time.get_ticks()

        if death_pause is not 0:
            if pygame.time.get_ticks() - death_pause > 5000: 
             running = False

        

    pygame.display.flip()
    clock.tick(60)
    looped += 1

pygame.quit()
