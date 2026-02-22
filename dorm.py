import pygame 
import random 


pygame.font.init()
SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True


CRIMSON = (220, 20, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


all_commands = [
    "Go to the Coug",
    "Study",
    "Skip class",
    "Do Homework",
    "Hang out with friends",
    "Go to the gym",
    "Go to class",
    "Go out to the Frats",
    "Go to the Grocery Store",
    "Go out to eat",
]

# allow repeats; returns a list of length 3
commands = random.choices(all_commands, k=3)

print("Command 1: " + commands[0])
print("Command 2: " + commands[1])
print("Command 3: " + commands[2])

 #button group 
firstChoice = {"Command 1": pygame.Rect(200,180,220,60)}
secondChoice = {"Command 2": pygame.Rect (200,180,220,60)}
thirdChoice = {"Command 3": pygame.Rect (200,180,220,60)}


command_data = {
    "Go to the Coug":
    {
        "description": "You decide to go to the Coug",
        "impact": {"money": -100, "health": -20, "stress": -10, "social_life_score": +40, "grade": -25}
    },

    "Study": {
        "description": "You decide to study",
        "impact": {"money": 0, "health": 0, "stress": +20, "social_life_score": -20, "grade": +20}
    },

    "Skip class": {
        "description": "You decide to skip class",
        "subs": {"money": 0, "health": 0, "stress": -10, "social_life_score": 0, "grade": -10}
    },

    "Do Homework": { 
        "description": "You decide to do your homework",
        "subs": {"money": 0, "health": 0, "stress": +10, "social_life_score": -10, "grade": +20}
    },

    "Hang out with friends": {
        "description": "You decide to hang out with your friends",
        "subs": {"money": 0, "health": 0, "stress": -20, "social_life_score": +15, "grade": 0}
    },

    "Go to the gym": {
        "description": "You decide to go to the gym",
        "subs": {"money": 0, "health": +30, "stress": -10, "social_life_score": 0, "grade": 0}
    },

    "Go to class": {
        "description": "You decide to go to class",
        "subs": {"money": 0, "health": 0, "stress": -10, "social_life_score": -10, "grade": +10}
    },

    "Go to the Frats":{
        "description": "You decide to go to the Frats",
        "subs": {"money": 0, "health": -20, "stress": -10, "social_life_score": +10, "grade": -20}
    },
    
    "Go to the Grocery Store": {
        "description": "You decide to go to the Grocery Store",
        "subs": {"money": -100, "health": +10, "stress": -10, "social_life_score": 0, "grade": 0}
    }, 

    "Go out to eat": {
        "description": "You decide to go out to eat",
        "subs": {"money": -100, "health": 0, "stress": -10, "social_life_score": 0, "grade": 0}
    }
}
    
    
def check_stats(user):
    if user.health > 100:
        user.health = 100
    if user.health < 0: 
        user.health = 0 
    if user.stress > 100:
        user.stress = 100
    if user.stress < 0:
        user.stress = 0
    if user.social_life_score > 100:
        user.social_life_score = 100
    if user.social_life_score < 0:
        user.social_life_score = 0
    if user.grade > 100:
        user.grade = 100


def draw_dorm_screen(screen,user,day): 
    title_font = pygame.font.SysFont("Consolas", 30)
    body_font = pygame.font.SysFont("Consolas", 15)
    check_stats(user)
    stats = {
        "Money": user.money,
        "Name": "Butch",
        "Major": user.major,
        "Health" : user.health,
        "Stress Level" : user.stress,
        "Social Life" : user.social_life_score,
        "Academic Grade"  : user.grade,
    }
    title_surf = title_font.render(f"Day {day} ", True, BLACK)
    screen.blit(title_surf, (50,30))

    
