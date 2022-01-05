import pygame, sys

main_clock = pygame.time.Clock()
from pygame.locals import *
global screen,click
pygame.init()
display = pygame.display.set_mode((500, 500), 0, 32)
font1 = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 120)
pl_count = 0
click = False
answered = 0
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            click = True

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class rectangle(object):
    def __init__(self, x,y,value, Q, A, B, C, D, points, ans):
        global screen,display
        self.x = x
        self.y = y
        self.Rect = pygame.Rect(self.x, self.y, 200, 100)
        self.color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        self.value =value
        self.Q = Q
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.points = points
        self.ans = ans
        self.graybox = True

    '''
    def click(self):
    self.graybox = False
    print('click')
    self.question()'''

    def questionbox(self):
        global click,font1,screen,answered

        mx, my = pygame.mouse.get_pos()
        print(click,screen)

        self.Rect = pygame.Rect(self.x, self.y, 200, 100)

        if click and screen == 'game':
            print('click')
            if self.Rect.collidepoint(mx,my) and self.graybox == True:
                answered +=1
                print(answered)
                self.graybox = False
                print('click square')
                self.question()

        if self.graybox:
            pygame.draw.rect(display, (255, 0, 0), self.Rect)
        else:
            pygame.draw.rect(display, (128, 128, 128), self.Rect)

        draw_text(self.value, self.font, (255, 255, 255), display, self.x + 100, self.y + 50)


    def question(self):
        global click, score1, score2, player1, pl_count, screen

        screen = 'question'
        while screen == 'question':
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if screen == 'question':
                mx, my = pygame.mouse.get_pos()
                display.fill((200, 228, 241))
                correct_ans = self.ans
                draw_text(self.Q, font1, (255, 255, 255), display, 500, 50)

                Q1 = pygame.Rect(0, 200, 500, 300)
                pygame.draw.rect(display, (0,128,255), Q1)
                draw_text(self.A, font1, (255, 255, 255), display, 250, 350)

                Q2 = pygame.Rect(0, 550, 500, 300)
                pygame.draw.rect(display, (0,128,255), Q2)
                draw_text(self.B, font1, (255, 255, 255), display, 250, 700)

                Q3 = pygame.Rect(550, 200, 500, 300)
                pygame.draw.rect(display, (0,128,255), Q3)
                draw_text(self.C, font1, (255, 255, 255), display, 800, 350)

                Q4 = pygame.Rect(550, 550, 500, 300)
                pygame.draw.rect(display, (0,128,255), Q4)
                draw_text(self.D, font1, (255, 255, 255), display, 800, 700)

                if screen == 'question':
                    if Q1.collidepoint((mx, my)) and correct_ans == 'A':
                        if click:
                            print('A')
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    score1 += self.points
                                    print('player1=+100')
                                    answer_check(True)

                                else:
                                    player1 = True
                                    score2 += self.points
                                    print('player2=+100')
                                    answer_check(True)
                            else:
                                score1 += self.points
                                answer_check(True)

                    elif Q2.collidepoint((mx, my)) and correct_ans == 'B':
                        if click:
                            print('B')
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    score1 += self.points
                                    print('player1=+100')
                                    answer_check(True)

                                else:
                                    player1 = True
                                    score2 += self.points
                                    print('player2=+100')
                                    answer_check(True)
                            else:
                                score1 += self.points
                                answer_check(True)

                    elif Q3.collidepoint((mx, my)) and correct_ans == 'C':
                        if click:
                            print('C')
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    score1 += self.points
                                    print('player1=+100')
                                    answer_check(True)


                                else:
                                    player1 = True
                                    score2 += self.points
                                    print('player2=+100')
                                    answer_check(True)
                            else:
                                score1 += self.points
                                answer_check(True)

                    elif Q4.collidepoint((mx, my)) and correct_ans == 'D':
                        if click:
                            print('D')
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    score1 += self.points
                                    print('player1=+100')
                                    answer_check(True)


                                else:
                                    player1 = True
                                    score2 += self.points
                                    print('player2=+100')
                                    answer_check(True)
                            else:
                                score1 += self.points
                                answer_check(True)

                    if Q1.collidepoint((mx, my)) and correct_ans != 'A':
                        if click:
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    print('wrong ans')
                                    answer_check(False)


                                else:
                                    player1 = True
                                    print('wrong ans')
                                    answer_check(False)
                            else:
                                answer_check(False)

                    elif Q2.collidepoint((mx, my)) and correct_ans != 'B':
                        if click:
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    print('wrong ans')
                                    answer_check(False)


                                else:
                                    player1 = True
                                    print('wrong ans')
                                    answer_check(False)
                            else:
                                answer_check(False)
                    elif Q3.collidepoint((mx, my)) and correct_ans != 'C':
                        if click:
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    print('wrong ans')
                                    answer_check(False)


                                else:
                                    player1 = True
                                    print('wrong ans')
                                    answer_check(False)
                            else:
                                answer_check(False)
                    elif Q4.collidepoint((mx, my)) and correct_ans != 'D':
                        if click:
                            if pl_count == 2:
                                if player1 == True:
                                    player1 = False
                                    print('wrong ans')
                                    answer_check(False)


                                else:
                                    player1 = True
                                    print('wrong ans')
                                    answer_check(False)
                            else:
                                answer_check(False)
            pygame.display.update()
            clock.tick(30)

player1= True
score1 = 0
score2 = 0
clock = pygame.time.Clock()
Q1_100 = rectangle(0, 100,'100', 'Which organ does covid-19 affect?', 'Lungs', 'Heart', "Liver", 'kidney', 100, 'A')
Q1_200 = rectangle(0, 200,'200', 'Which age group does covid affect the most?', '0-11', '11-22', "30-49", '50-80+', 200, 'D')
Q1_300 = rectangle(0, 300,'300', 'What does the 19 stand for in COVID-19?', 'the number of variants', 'the year it was discovered', "The amount of symptoms", 'The chance (%) of being infected', 300, 'B')
Q1_400 = rectangle(0, 400,'400', 'When Was covid-19 first discovered?', 'November 21 2019', 'December 21 2019', "December 31 2019", 'January 14 2020', 400, 'C')
Q1_500 = rectangle(0, 500,'500', 'Which health condition put you at greater risk to covid-19?', 'Alzheimer’s', 'Cancer', "Flu", 'Severe heart conditions', 500, 'D')

Q2_100 = rectangle(250, 100,'100', 'What is the most common symptom?', 'Fever', 'Sore throat', "Aches and pain", 'Irrated eyes', 100, 'A')
Q2_200 = rectangle(250, 200,'200', 'How many days does it take for covid to show symptoms on average?', '10-14 days', '7-8 days', "3-4 days", '5-6 days', 200, 'D')
Q2_300 = rectangle(250, 300,'300', 'Which statement is false about PCR testing?', 'PCR stand for Polymerase chain reaction', 'It is 100% accurate', "PCR typically takes 1-3 days to get results back", 'PCR is more effective than an antigen test', 300, 'B')
Q2_400 = rectangle(250, 400,'400', 'How is PCR testing done?', 'Sample taken from your saliva', 'Nose swab', "Blood sample", 'plasma', 400, 'B')
Q2_500 = rectangle(250, 500,'500', 'Which is not an unusual symptom of covid-19?', 'Loss of smell or taste', 'Light sensitivity', "Skin rashes", 'Tiredness', 500, 'D')

Q3_100 = rectangle(550, 100,'100', 'Which is not a side effect after taking the vaccine?', 'Fatigue', 'Chills', "Mild fever", 'coughing', 100, 'D')
Q3_200 = rectangle(550, 200,'200', 'How many shots do you need to take to be considered completely vaccinated?', '1 doses', '2 doses', "3 doses", '4 doses', 200, 'B')
Q3_300 = rectangle(550, 300,'300', 'Which is not true about the vaccine?', 'You can still spread it despite taking the vaccine', 'vaccine makes you completely immune to the virus', "The vaccine reduces mild and severe cases", 'It keeps other people safe', 300, 'B')
Q3_400 = rectangle(550, 400,'400', 'What is not a common allergic reaction to covid-19 vaccine?', 'Hives (bumps on the skin)', 'Difficulty breathing', "Swelling on your face, tongue or throat", 'Muscle ache', 400, 'D')
Q3_500 = rectangle(550, 500,'500', 'When do allergic reactions occur after taking the vaccine?', '1-2 mins', '15-30 mins', "1-2 hours", '6-12 hours', 500, 'B')

Q4_100 = rectangle(800, 100,'100', 'How many feet apart should you be to avoid possible transmission of the virus?', '2 feet', '3 feet', "6 feet", '5 feet', 100, 'C')
Q4_200 = rectangle(800, 200,'200', 'Which is not an effective method to prevent spreading covid-19?', 'Using a face mask', 'Washing your hands without soap', "Using hand sanitizer", 'Social distancing', 200, 'B')
Q4_300 = rectangle(800, 300,'300', 'Where does most transmission occur the least?', 'Indoors', 'Crowded area', "Confined place with proper ventilation", 'Confined place', 300, 'C')
Q4_400 = rectangle(800, 400,'400', 'What procedures should you take when gathering with people in a room?', 'Keep it properly ventilated', 'Distance at minimum 1 meter', "Wear masks", 'All of the above', 400, 'D')
Q4_500 = rectangle(800, 500,'500', 'How many layers does a proper face mask have', '1 layer', '2 layers', "3 layers", '4 layers', 500, 'C')

def game(x):
    while True:
        global score1,score2,click,player1,pl_count,screen,display
        screen = 'game'
        display.fill((200, 228, 241))

        if x == 1:
            draw_text('player 1= ' + str(score1), font1, (255, 255, 255), display, 500, 750)
            pl_count = 1

        if x == 2:
            draw_text('player 1= ' + str(score1), font1, (255, 255, 255), display, 500, 750)
            draw_text('player 2= ' + str(score2), font1, (255, 255, 255), display, 500, 700)
            pl_count = 2

        draw_text('Facts', font1, (255, 255, 255), display, 100, 50)
        draw_text('Symptoms', font1, (255, 255, 255), display, 350, 50)
        draw_text('Vaccine', font1, (255, 255, 255), display, 650, 50)
        draw_text('Safety', font1, (255, 255, 255), display, 900, 50)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        Q1_100.questionbox()
        Q1_200.questionbox()
        Q1_300.questionbox()
        Q1_400.questionbox()
        Q1_500.questionbox()

        Q2_100.questionbox()
        Q2_200.questionbox()
        Q2_300.questionbox()
        Q2_400.questionbox()
        Q2_500.questionbox()


        Q3_100.questionbox()
        Q3_200.questionbox()
        Q3_300.questionbox()
        Q3_400.questionbox()
        Q3_500.questionbox()

        Q4_100.questionbox()
        Q4_200.questionbox()
        Q4_300.questionbox()
        Q4_400.questionbox()
        Q4_500.questionbox()

        if answered == 20:
            end_screen()

        pygame.display.update()
        main_clock.tick(30)

def answer_check(x):
    while True:
        global click, pl_count, screen
        screen = 'answer_check'
        mx, my = pygame.mouse.get_pos()
        box = pygame.Rect(200, 200, 600, 500)
        next = pygame.Rect(350, 550, 300, 100)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if x == True:
            pygame.draw.rect(display, (51, 255, 51), box)
            draw_text('Correct', font2, (255, 255, 255), display, 500, 350)

        if x == False:
            pygame.draw.rect(display, (201, 0, 0), box)
            draw_text('Wrong', font2, (255, 255, 255), display, 500, 350)

        pygame.draw.rect(display, (255, 255, 0), next)
        draw_text('Continue', font1, (255, 255, 255), display, 500, 600)

        if screen == 'answer_check':
            if next.collidepoint((mx, my)):
                if click:
                    game(pl_count)

        pygame.display.update()

def end_screen():
    while True:
        global click, pl_count, screen, answered

        screen = 'end screen'
        display.fill((200, 228, 241))
        draw_text('Ranking', font2, (255, 255, 255), display, 500, 200)
        if pl_count == 2:
            if score1 > score2:
                draw_text('player 1= ' + str(score1), font2, (255, 255, 255), display, 500, 350)
                draw_text('player 2= ' + str(score2), font2, (255, 255, 255), display, 500, 550)
            else:
                draw_text('player 1= ' + str(score1), font2, (255, 255, 255), display, 500, 350)
                draw_text('player 2= ' + str(score2), font2, (255, 255, 255), display, 500, 500)
        else:
            draw_text('player 1= ' + str(score1), font2, (255, 255, 255), display, 500, 550)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        clock.tick(30)
        pygame.display.update()