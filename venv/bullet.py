#
# SpaceInvaders
# Created by Alex Smarandache on 15/03/2021
# Copyright © Alex Smarandache. All rights reserved.
#

import pygame
import random

class Bullet:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.act_x = 0
        self.act_y = 10
        self.is_ready = True

    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

    def set_act_x(self, new_value):
        self.act_x = new_value
    
    def set_sound(self, sound):
        self.sound = sound
     
    def play_sound(self):
        self.sound.play()
        
    def get_act_x(self):
        return self.act_x

    def set_act_y(self, new_value):
        self.act_y = new_value

    def get_act_y(self):
        return self.act_y

    def set_is_ready(self, new_value):
        self.is_ready = new_value

    def get_is_ready(self):
        return self.is_ready

    def add_x(self, value):
        self.x += value

    def add_y(self, value):
        self.y += value

    def fire(self, screen, x, y):
        self.is_ready = False
        screen.blit(self.image, (x + 16, y + 10))