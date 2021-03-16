#
# SpaceInvaders
# Created by Alex Smarandache on 15/03/2021
# Copyright © Alex Smarandache. All rights reserved.
#

import pygame
import random

class Enemy:
    def __init__(self, image):
        self.image = image
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)
        self.act_x = 4
        self.act_y = 40

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

    def get_act_x(self):
        return self.act_x
    
    def set_act_y(self, new_value):
        self.act_y = new_value

    def get_act_y(self):
        return self.act_y
    
    def add_x(self, value):
        self.x += value

    def add_y(self, value):
        self.y += value

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))