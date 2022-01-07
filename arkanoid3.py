import pygame
import time
pygame.init()
 
back = (200, 255, 255)
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()
 
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
 
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('Arial', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
 
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    
time_text = Label(150,230,200,100,(234,122,203))
time_text.set_text('Start',40, (233,122,123))
time_text.draw(20, 20)
start = True

def level2():
    platform_x = 200
    platform_y = 330
    move_right = False
    move_left = False
    game_over = False
 
    dx = 4
    dy = 4
    
    start_x = 5
    start_y = 5
    count = 9
    
    monsters = []
    for j in range(3):
        y = start_y + (55 * j)
        x = start_x + (27.5 * j)
        for i in range (count):
            d = Picture('enemy.png',x, y, 50, 50)
            monsters.append(d)
            x = x + 55
        count = count - 1
        
    ball = Picture('ball.png', 160, 200, 50, 50)
    platform = Picture('platform.png', platform_x, platform_y, 100, 30)
    
    game_over = False
        
    while not game_over:
        ball.fill()
        platform.fill()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False
            
        if move_right:
            platform.rect.x += 3
        if move_left:
            platform.rect.x -= 3
        ball.rect.x += dx
        ball.rect.y += dy
        if  ball.rect.y < 0:
            dy *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            dx *= -1
        if ball.rect.y > 350:
            time_text = Label(150,150,50,50,back)
            time_text.set_text('YOU LOSE',60, (255,0,0))
            time_text.draw(10, 10)
            game_over = True
        '''if len(monsters) == 0:
            time_text = Label(150,150,50,50,back)
            time_text.set_text('YOU WIN',60, (0,200,0))
            time_text.draw(10, 10)
            game_over = True'''
        if len(monsters) == 0:
            level2()
        if ball.rect.colliderect(platform.rect):
            dy *= -1
        for m in monsters:
            m.draw()
            #если монстра коснулся мяч, удаляем монстра из списка и меняем направления движения мяча
            if m.rect.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                dy *= -1
        platform.draw()
        ball.draw()
        pygame.display.update()
        clock.tick(40)

def level1():
    platform_x = 200
    platform_y = 330
    move_right = False
    move_left = False
    game_over = False
 
    dx = 3
    dy = 3
    
    start_x = 3
    start_y = 3
    count = 9
    
    monsters = []
    for j in range(1):
        y = start_y + (55 * j)
        x = start_x + (27.5 * j)
        for i in range (count):
            d = Picture('enemy.png',x, y, 50, 50)
            monsters.append(d)
            x = x + 55
        count = count - 1
        
    ball = Picture('ball.png', 160, 200, 50, 50)
    platform = Picture('platform.png', platform_x, platform_y, 100, 30)
    
    game_over = False
        
    while not game_over:
        ball.fill()
        platform.fill()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_LEFT:
                    move_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_LEFT:
                    move_left = False
            
        if move_right:
            platform.rect.x +=3
        if move_left:
            platform.rect.x -=3
        ball.rect.x += dx
        ball.rect.y += dy
        if  ball.rect.y < 0:
            dy *= -1
        if ball.rect.x > 450 or ball.rect.x < 0:
            dx *= -1
        if ball.rect.y > 350:
            time_text = Label(150,150,50,50,back)
            time_text.set_text('YOU LOSE',60, (255,0,0))
            time_text.draw(10, 10)
            game_over = True
        '''if len(monsters) == 0:
            time_text = Label(150,150,50,50,back)
            time_text.set_text('YOU WIN',60, (0,200,0))
            time_text.draw(10, 10)
            game_over = True'''
        if len(monsters) == 0:
            level2()
        if ball.rect.colliderect(platform.rect):
            dy *= -1
        for m in monsters:
            m.draw()
            #если монстра коснулся мяч, удаляем монстра из списка и меняем направления движения мяча
            if m.rect.colliderect(ball.rect):
                monsters.remove(m)
                m.fill()
                dy *= -1
        platform.draw()
        ball.draw()
        pygame.display.update()
        clock.tick(40)

while start:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if time_text.collidepoint(x,y):
                mw.fill(back)
                level1()
        if event.type == pygame.QUIT:
            start = False        
        
    pygame.display.update()
    clock.tick(40)


        
    
    