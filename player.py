import pygame

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
            self.stess -=20
            








