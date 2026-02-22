# Example file showing a basic pygame "game loop"
import pygame
import screen1
from player import Player 
import dorm


# pygame setup
pygame.init()
SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
title_font = pygame.font.SysFont("Consolas", 60) # font type fob bigger text goes here 
sub_title_font = pygame.font.SysFont("Consolas", 30) # font type for smaller text here goes here 
small_text_font = pygame.font.SysFont("Consolas", 10) # font type for even smaller text here goes here 

User = Player()

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
        dorm.draw_dorm_screen(screen,User)
    
    pygame.display.flip()
    clock.tick(60)

    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

  

pygame.quit()
