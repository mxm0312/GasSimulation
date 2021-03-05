import pygame
import random
import math
import matplotlib.pyplot as plt


shir = 800
vis = 800
counter = 5
pygame.init()

win = pygame.display.set_mode((shir, vis))

pygame.display.set_caption("Симуляция газа")
N = 20

timer = pygame.time.get_ticks()
moleculus = []


class molecula:
    radius = 25
    def __init__(self, x, y, speedx, speedy):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy

    def draw(self):
        pygame.draw.circle(win, (128,0,128), (int(self.x),int(self.y)), self.radius)

    def checkWalls(self):
        if self.y >= vis - 2*self.radius and self.speedy >= 0:
            self.speedy *= -1

        if self.y <= 2*self.radius and self.speedy <= 0:
            self.speedy *= -1

        if self.x >= shir - 2*self.radius and self.speedx >= 0:
            self.speedx *= -1

        if self.x <= 2*self.radius and self.speedx <= 0:
            self.speedx *= -1

    def checkProblems(self):

        for i in range(N):
            if math.sqrt( (self.x - moleculus[i].x)*(self.x - moleculus[i].x) + (self.y - moleculus[i].y)*(self.y - moleculus[i].y) ) <= 2*self.radius and math.sqrt( (self.x - moleculus[i].x)*(self.x - moleculus[i].x) + (self.y - moleculus[i].y)*(self.y - moleculus[i].y) ) != 0:
                # с - длина вектора
                c = math.sqrt( (moleculus[i].speedx - self.speedx)*(moleculus[i].speedx - self.speedx) + (moleculus[i].speedy - self.speedy)*(moleculus[i].speedy - self.speedy) )
                b = math.sqrt( (self.x - moleculus[i].x)*(self.x - moleculus[i].x) + (self.y - moleculus[i].y)*(self.y - moleculus[i].y) )
                a = math.sqrt( (self.x - moleculus[i].x - moleculus[i].speedx + self.speedx)*(self.x - moleculus[i].x - moleculus[i].speedx + self.speedx) + (self.y - moleculus[i].y - moleculus[i].speedy + self.speedy)*(self.y - moleculus[i].y - moleculus[i].speedy + self.speedy)  )
                if (2*b*c) != 0:
                    if (b*b + c*c - a*a) / (2*b*c) > 0:
                    #формула для косинуса из скалярного произведения берётся внизу
                        X_axis = [self.x - moleculus[i].x, self.y - moleculus[i].y]
                        Y_axis = [X_axis[1], -X_axis[0]]
                        v_x = (self.speedx * X_axis[0] + self.speedy * X_axis[1])/(X_axis[0]*X_axis[0] + X_axis[1]*X_axis[1])
                        v_y = (self.speedx*Y_axis[0]+self.speedy*Y_axis[1])/(Y_axis[0]*Y_axis[0] + Y_axis[1]*Y_axis[1])
                        u_x = (moleculus[i].speedx*X_axis[0] + moleculus[i].speedy*X_axis[1])/(X_axis[0]*X_axis[0] + X_axis[1]*X_axis[1])
                        u_y = (moleculus[i].speedx*Y_axis[0] + moleculus[i].speedy*Y_axis[1])/(Y_axis[0]*Y_axis[0] + Y_axis[1]*Y_axis[1])
                        vax = [X_axis[0]*v_x, X_axis[1]*v_x]
                        vay = [Y_axis[0]*v_y, Y_axis[1]*v_y]
                        ubx = [X_axis[0]*u_x, X_axis[1]*u_x]
                        uby = [Y_axis[0]*u_y, Y_axis[1]*u_y]

                        if (X_axis[0]*X_axis[0] + X_axis[1]*X_axis[1] != 0) and (Y_axis[0]*Y_axis[0] + Y_axis[1]*Y_axis[1] != 0):
                            self.speedx = vay[0] + ubx[0]
                            self.speedy = vay[1] + ubx[1]
                            moleculus[i].speedx = uby[0] + vax[0]
                            moleculus[i].speedy = uby[1] + vax[1]

    def move(self):
        self.x += self.speedx
        self.y += self.speedy

    def update(self):
        self.checkWalls()
        self.move()
        self.draw()

for i in range(N):
    m = molecula(random.randint(50, shir - 50), random.randint(50, shir - 50), random.randint(-42, 42), random.randint(-42, 42))
    moleculus.append(m)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(N):

        moleculus[i].checkProblems()
        moleculus[i].update()

    pygame.display.update()
    win.fill((0,0,0))

pygame.quit()
