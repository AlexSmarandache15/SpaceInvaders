#
# SpaceInvaders
# Created by Alex Smarandache on 15/03/2021
# Copyright © Alex Smarandache. All rights reserved.
#

import pygame
import math
import player
import random
import enemy
import bullet

class SpaceInvaders:

    def _display_score(self):
        my_score = self.font.render("Score: " + str(self.score), True, (0, 255, 0))
        self.screen.blit(my_score, (self.x, self.y))

    def _display_game_over(self):
        self.screen.blit(self.font.render("GAME OVER", True, (255, 255, 255)), (300, 250))

    def _is_collision(self, enemy_x, enemy_y, bullet_x, bullet_y):
        distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
        return distance < 27

    def play(self):
        pygame.init()
        background = pygame.image.load('background.png')
        pygame.mixer.music.load("background.wav")
        pygame.mixer.music.play(-1)
        self.my_player = player.Player(pygame.image.load('player.png'), 370, 480)
        self.enemies = []
        self.num_of_enemies = 7

        for i in range(self.num_of_enemies):
            if i % 3 == 0:
                self.enemies.append(enemy.Enemy(pygame.image.load('enemy1.png')))
            elif i % 3 == 1:
                self.enemies.append(enemy.Enemy(pygame.image.load('enemy2.png')))
            else:
                self.enemies.append(enemy.Enemy(pygame.image.load('enemy3.png')))
        
        self.my_bullet = bullet.Bullet(pygame.image.load('bullet.png'), 0, 480)
        self.score = 0
        self.x = 10
        self.y = 10
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.over_font = pygame.font.Font('freesansbold.ttf', 64)
        self.screen = pygame.display.set_mode((800, 600))
        
        is_running = True
        while is_running:
            self.screen.fill((0, 0, 0))
            self.screen.blit(background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.my_player.set_act_x(-5)
                    if event.key == pygame.K_RIGHT:
                        self.my_player.set_act_x(5)
                    if event.key == pygame.K_SPACE:
                        if self.my_bullet.get_is_ready() == True:
                            self.my_bullet.set_sound(pygame.mixer.Sound("laser.wav"))
                            self.my_bullet.play_sound()
                            self.my_bullet.set_x(self.my_player.get_x())
                            self.my_bullet.fire(self.screen, self.my_bullet.get_x(), self.my_bullet.get_y())
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.my_player.set_act_x(0)

            self.my_player.add_x(self.my_player.get_act_x())

            if self.my_player.get_x() <= 0:
                self.my_player.set_x(0)
            elif self.my_player.get_x() >= 736:
                self.my_player.set_x(736)

            for i in range(self.num_of_enemies):
                if self.enemies[i].get_y() > 440:
                    for j in range(self.num_of_enemies):
                        self.enemies[j].set_y(2000)
                    self._display_game_over()
                    break

                self.enemies[i].add_x(self.enemies[i].get_act_x())

                if self.enemies[i].get_x() <= 0:
                    self.enemies[i].set_act_x(4)
                    self.enemies[i].add_y(self.enemies[i].get_act_y())

                elif self.enemies[i].get_x() >= 736:
                    self.enemies[i].set_act_x(-4)
                    self.enemies[i].add_y(self.enemies[i].get_act_y())

                collision = self._is_collision(self.enemies[i].get_x(), self.enemies[i].get_y(), self.my_bullet.get_x(), self.my_bullet.get_y())

                if collision:
                    explosionSound = pygame.mixer.Sound("explosion.wav")
                    explosionSound.play()
                    self.my_bullet.set_y(480)
                    self.my_bullet.set_is_ready(True)
                    self.score += 1
                    self.enemies[i].set_x(random.randint(0, 736))
                    self.enemies[i].set_y(random.randint(50, 150))

                self.enemies[i].show(self.screen)

            if self.my_bullet.get_y() <= 0:
                self.my_bullet.set_y(480)
                self.my_bullet.set_is_ready(True)

            if self.my_bullet.get_is_ready() == False:
                self.my_bullet.fire(self.screen, self.my_bullet.get_x(), self.my_bullet.get_y())
                self.my_bullet.set_y(self.my_bullet.get_y() - self.my_bullet.get_act_y())

            self.my_player.show(self.screen)
            self._display_score()
            pygame.display.update()