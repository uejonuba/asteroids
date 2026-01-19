from constants import *
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.rotation = 0

    def draw(self,screen) :
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self,dt) :
        self.position += self.velocity * dt 
    
    def split(self) :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        log_event("asteroid_split")
        rand_angle = random.uniform(20,50)
        new_angle1 = self.velocity.rotate(rand_angle)
        new_angle2 = self.velocity.rotate(-rand_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_aster1 = Asteroid(self.position.x,self.position.y,new_rad)
        new_aster2 = Asteroid(self.position.x,self.position.y,new_rad)
        new_aster1.velocity = new_angle1
        new_aster2.velocity = new_angle2
    

