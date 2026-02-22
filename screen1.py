import pygame 

pygame.font.init()
SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True


CRIMSON = (220, 20, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

MAJORS = ["Computer Science", "Buisness", "Nursing", "Kinesiology", "Liberal Arts"]

                    

def _render_wrapped(surface, text, font, color, x, y, max_width, line_spacing=6):
    words = text.split()
    line = ''
    for word in words:
        test = (line + ' ' + word).strip()
        if font.size(test)[0] <= max_width:
            line = test
        else:
            surf = font.render(line, True, color)
            surface.blit(surf, (x, y))
            y += surf.get_height() + line_spacing
            line = word
    if line:
        surf = font.render(line, True, color)
        surface.blit(surf, (x, y))
        y += surf.get_height() + line_spacing
    return y

def draw_screen1(screen):
    title_font = pygame.font.SysFont("Consolas", 30)
    body_font = pygame.font.SysFont("Consolas", 15)

    title_surf = title_font.render("Welcome to The Wazzu Trail Game!", True, BLACK)
    intro_text = (
        "It is Butch's Senior year at WSU and to graduate you must complete the Wazzu Trail and "
        "keep all your attributes up! "
        "You will be making choices that will affect your attributes and your path to graduation. "
        "Social Life: Represents your social interaction to increase this attribute you can go to bars, hang out with friends, and go out. "
        "Stress Level: Represents your stress to increase this attribute you can study to decrease your stress you can go out. "
        "Health: Represents your health and this can go down if you go to the bars and there are random nights where you are more likely to get sick."
        "Money: Represents your money you start with $8,000 and this goes down if you spend to much money on going out so budget well. "
        "Grade: When Social Life goes up your grade goes down and when your Stress Level goes up your grade goes down.  " 
    )

    select_surf = body_font.render("Select your major:", True, BLACK)

   #button group
    computerScienceButton = {"ComputerScience": pygame.Rect(200,180,220,60)}
    businessButton = {"Buisness": pygame.Rect (200,180,220,60)}
    nursingButton = {"Nursing": pygame.Rect (200,180,220,60)}
    kinesiologyButton = {"Kinesiology": pygame.Rect (200,180,220,60)}
    liberalArtsButton= {"Liberal Arts":pygame.Rect (200,180,220,60)}

    screen.fill("dark grey")

    screen.blit(title_surf, (50, 30))

    y_after = _render_wrapped(screen, intro_text, body_font, BLACK, 50, 80, 760)

    screen.blit(select_surf, (50, y_after + 10))

