import pygame, sys,time
main_clock = pygame.time.Clock()
from pygame.locals import *
from Game import game
pygame.init()
pygame.display.set_caption('Jeopardy')
display = pygame.display.set_mode((1000, 800), 0, 32)
font1 = pygame.font.SysFont(None, 60)
font2 = pygame.font.SysFont(None, 120)

mx, my = pygame.mouse.get_pos()
pl_count = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    global click, screen, pl_count
    screen = 'main'
    if screen == 'main':
        while True:
            display.fill((200, 228, 241))
            draw_text('Covid-19 Jeopardy', font2, (255, 255, 255), display, 500, 50)
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(370, 300, 250, 100)
            pygame.draw.rect(display, (255, 0, 0), button_1)
            draw_text('Play', font1, (255, 255, 255), display, 500, 350)

            if button_1.collidepoint((mx, my)) and screen == 'main':
                if click:
                    print('menu')
                    player_count()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    num = pygame.mouse.get_pressed()
                    if num[0]:
                        click = True

            pygame.display.update()
            main_clock.tick(60)

def player_count():
    global click, screen
    screen = 'player select'
    if screen == 'player select':
        while True:
            display.fill((200, 228, 241))

            mx, my = pygame.mouse.get_pos()

            player_Count1 = pygame.Rect(375, 90, 250, 100)
            player_Count2 = pygame.Rect(375, 200, 250, 100)

            pygame.draw.rect(display, (255, 0, 0), player_Count1)
            pygame.draw.rect(display, (255, 0, 0), player_Count2)

            draw_text('player select screen', font2, (255, 255, 255), display, 500, 50)

            draw_text('1', font1, (255, 255, 255), display, 500, 140)
            draw_text('2', font1, (255, 255, 255), display, 500, 250)

            if screen == 'player select':
                if player_Count1.collidepoint((mx, my)):
                    if click:
                        print('clicked 1 player')
                        game(1)
                if player_Count2.collidepoint((mx, my)):
                    if click:
                        print('clicked 2 player')
                        game(2)

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            main_clock.tick(60)
main_menu()