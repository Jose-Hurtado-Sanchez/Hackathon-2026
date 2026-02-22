import pygame
BLACK = (0, 0, 0)
CRIMSON = (220, 20, 60)

class Player:
    def __init__(self):
        self.money = 8000.00
        self.name = "unknown"
        self.major = "unknown"
        self.health = 75
        self.stress = 50 # dependent on major 
        self.social_life_score = 50 #depenedent on major 
        self.grade = 70 # every grade starts at 100 

    def boostByMajor(self):
        if self.major == "Computer Science":
            self.stress += 25 # start with higher stress level 
            self.grade  += 20 # start with higher grade level 

        if self.major == "Buisness": 
            self.stress -= 10
            self.social_life_score +=20
        
        if self.major == "Nursing":
            self.stress += 15
            self.health += 20
            self.social_life_score -= 10

        if self.major == "Kinesiology":
            self.health += 15
            self.social_life_score += 5
            self.grade +=5

        if self.major == "Liberal Arts":
            self.social_life_score += 20
            self.stress -=20
            


    def update_user_stats(self,choice):
        if choice == "Go to the Coug":
            self.money -= 100
            self.health -=20
            self.stress -=10
            self.grade -= 25
            self.social_life_score += 40

        if choice == "Study":
            self.stress +=20
            self.social_life_score -=20
            self.grade +=20

        if choice == "Skip class":
            self.stress -= 10
            self.grade -=10
            self.social_life_score -=20

        if choice == "Do Homework":
            self.stress += 10
            self.social_life_score -=10
            self.grade += 20

        if choice == "Hang out with friends":
            self.stress -=20
            self.social_life_score +=15

        if choice == "Go to the gym":
            self.health += 30
            self.stress -= 10

        if choice == "Go to the Frats":
            self.health -=20
            self.stress -=10
            self.social_life_score += 10
            self.grade -=20

        if choice == "Go to the Grocery Store":
            self.money -=100
            self.health +=10
            self.stress -=10 
        
        if choice == "Go out to eat":
            self.money -=100 
            self.stress -=10
        
        if choice == "Go to Class":
            self.stress -=10
            self.social_life_score -= 10
            self.grade += 10

    def death_screen(self, screen):
        title_font = pygame.font.SysFont("Consolas", 30)
        body_font = pygame.font.SysFont("Consolas", 15)

        death_msg = title_font.render("YOU LOSE", True, BLACK)
        death_rect = death_msg.get_rect(center=(640,250))
        screen.blit(death_msg,death_rect)
        
        if self.health <= 0:
            reason= "YOUR HEALTH REACHED 0"
        elif self.money <= 0:
            reason= "YOUR MONEY REACHED 0"
        elif self.social_life_score <=0:
            reason = "YOUR SOCIAL LIFE REACHED 0"
        elif self.stress >= 100:
            reason = "YOUR STRESS LEVEL REACHED 100"

        reason_of_loss = body_font.render(reason, True,BLACK)
        reason_rect = reason_of_loss.get_rect(center=(640,400))
        screen.blit(reason_of_loss,reason_rect)









