# Example file showing a basic pygame "game loop"
import pygame
import screen1
import player 

# pygame setup
pygame.init()
SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
title_font = pygame.font.SysFont("Consolas", 60) # font type fob bigger text goes here 
sub_title_font = pygame.font.SysFont("Consolas", 30) # font type for smaller text here goes here 


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

while running:
    #---  ALL EVENTS 
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #--button events--
    mouse_position = pygame.mouse.get_pos() #mouse position
            
    if event.type == pygame.MOUSEBUTTONDOWN and screen_state == "starting_screen":
        if full_button.collidepoint(event.pos):
            screen_state = "screen_1"


    #--screen fill--
    # fill the screen with a color to wipe away anything from last frame

    if screen_state == "starting_screen" :
        screen.fill("dark grey")

        screen.blit(game_title,center_text)

        if pygame.time.get_ticks() % 900 < 400: # makes the 
            screen.blit(press_to_start, press_rect)

    if screen_state == "screen_1" :
        screen1.draw_screen1(screen)
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    if goScreen1: 
        screen1.run(screen,clock)

pygame.quit()