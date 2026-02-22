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


command_data = {
    "Go to the Coug":
    {
        "description": "You decide to go to the Coug",
        "subs": 
        [
            {"text": "Your friend doesn't have any money so you pay for there drink", "money": -30, "health": -1, "stress": -5, "social_life_score":+10, "grade": -1},
            {"text": "You have one drink", "money": -10, "health": -1, "stress": -10, "social_life_score": +5, "grade": -1},
            {"text": "You have lots of drinks", "money": -100, "health": -2, "stress": -15, "social_life_score": +15, "grade": -2}
        ]
    },

    "Study": {
        "description": "You decide to study",
        "subs": [
            {"text": "You study for 1 hour", "money": 0, "health": 0, "stress": +5, "social_life_score": -5, "grade": +1},
            {"text": "You study for 3 hours", "money": 0, "health": 0, "stress": +10, "social_life_score": -10, "grade": +2},
            {"text": "You study for 5 hours", "money": 0, "health": 0, "stress": +15, "social_life_score": -15, "grade": +3}
        ]
    },

    "Skip class": {
        "description": "You decide to skip class",
        "subs": [
            {"text": "You skip class and take a nap", "money": 0, "health": +5, "stress": -5, "social_life_score": 0, "grade": -1},
            {"text": "You skip class and study for a test", "money": 0, "health": 0, "stress": +5, "social_life_score": 0, "grade": +5},
            {"text": "You skip class and hang out with a friend", "money": 0, "health": 0, "stress": -5, "social_life_score": +5, "grade": -1}
        ]
    },

    "Do Homework": { 
        "description": "You decide to do your homework",
        "subs": [
            {"text": "You do your homework that is due tonight", "money": 0, "health": 0, "stress": +5, "social_life_score": -5, "grade": +1},
            {"text": "You do your homework that is due for the next three days", "money": 0, "health": 0, "stress": +10, "social_life_score": -10, "grade": +2},
            {"text": "You do your homework that is due for the rest of the week", "money": 0, "health": 0, "stress": +15, "social_life_score": -15, "grade": +5}
        ]
    },

    "Hang out with friends": {
        "description": "You decide to hang out with your friends",
        "subs": [
            {"text": "You hang out with your friends for an hour", "money": 0, "health": 0, "stress": -5, "social_life_score": +5, "grade": 0},
            {"text": "You hang out with your friends for three hours", "money": 0, "health": 0, "stress": -10, "social_life_score": +10, "grade": 0},
            {"text": "You hang out with your friends for the whole day", "money": 0, "health": 0, "stress": -15, "social_life_score": +15, "grade": 0}
        ]
    },

    "Go to the gym": {
        "description": "You decide to go to the gym",
        "subs": [
            {"text": "You go to the gym for an 30 min", "money": 0, "health": +5, "stress": -5, "social_life_score": 0, "grade": 0},
            {"text": "You go to the gym for an hour", "money": 0, "health": +10, "stress": -10, "social_life_score": 0, "grade": 0},
            {"text": "You go to the gym for two hours", "money": 0, "health": +15, "stress": -15, "social_life_score": 0, "grade": 0}
        ]
    },

    "Go to the Frats":{
        "description": "You decide to go to the Frats",
        "subs": [
            {"text": "You go to the Frats and have one drink", "money": 0, "health": -5, "stress": -5, "social_life_score": +5, "grade": -1},
            {"text": "You go to the Frats and have three drinks", "money": 0, "health": -10, "stress": -10, "social_life_score": +10, "grade": -2},
            {"text": "You go to the Frats and have five drinks", "money": 0, "health": -15, "stress": -15, "social_life_score": +15, "grade": -3}
        ]
    },
    
    "Go to the Grocery Store": {
        "description": "You decide to go to the Grocery Store",
        "subs": [
            {"text": "You go to the Grocery Store and buy some snacks", "money": -20, "health": +5, "stress": 0, "social_life_score": 0, "grade": 0},
            {"text": "You go to the Grocery Store and buy some groceries for the week", "money": -100, "health": +10, "stress": -10, "social_life_score": 0, "grade": 0},
            {"text": "You go to the Grocery Store and buy a lot of groceries for the month", "money": -400, "health": +15, "stress": -15, "social_life_score": 0, "grade": 0}
        ]
    }, 

    "Go out to eat": {
        "description": "You decide to go out to eat",
        "subs": [
            {"text": "You go out to eat and get fast food", "money": -15, "health": -5, "stress": 0, "social_life_score": 0, "grade": 0},
            {"text": "You go out to eat and get a nice meal", "money": -50, "health": 0, "stress": -5, "social_life_score": 0, "grade": 0},
            {"text": "You go out to eat and get a fancy meal", "money": -100, "health": +5, "stress": -10, "social_life_score": 0, "grade": 0}
        ]
    }
}


selected_command = "Go to the coug"

#event = random.choice(command_data[selected_command]["subs"])


def draw_dorm_screen(screen,user): 
    title_font = pygame.font.SysFont("Consolas", 30)
    body_font = pygame.font.SysFont("Consolas", 15)
    day = 1
    maxDay = 50
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