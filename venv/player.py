#
# SpaceInvaders
# Created by Alex Smarandache on 15/03/2021
# Copyright © Alex Smarandache. All rights reserved.
#

import pygame

class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.act_x = 0

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

    def add_x(self, value):
        self.x += value

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))