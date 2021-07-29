import pygame
import random
import pickle
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (167, 0, 238)
size = 10

wight = 750
height = 750
screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption('SNAKE IS GOOD')
back = (60, 179, 113)
pygame.display.update()

x = random.randrange(size, wight - size, size)
y = random.randrange(size, wight - size, size)


clock = pygame.time.Clock()

run = True

font_score = pygame.font.SysFont("times-new-roman", 14)
font_end = pygame.font.SysFont("times-new-roman", 24)

#  Snake


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bebeb.jpg")
        self.image = pygame.transform.scale(self.image, [30, 30])
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.size = 10
        self.score = 0
        self.hello = 0
        self.speed = 3
        self.dx = 0
        self.dy = 0


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def move(self):
        food.rect.x = random.randrange(50, wight - 50)
        food.rect.y = random.randrange(50, height - 50)


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.jpg")
        self.image = pygame.transform.scale(self.image, [40, 40])
        #self.image.fill(PURPLE)
        self.rect = self.image.get_rect()

# where to draw game object


snake = Snake()
snake.rect.x = wight // 2
snake.rect.y = height // 2

snake1 = Snake()
snake1.rect.x = wight // 2
snake1.rect.y = height // 2

food = Food()
food.rect.x = random.randrange(50, wight - 50)
food.rect.y = random.randrange(50, height - 50)

# sprite group
sprites_group = pygame.sprite.Group()
sprites_group.add(snake)
sprites_group.add(snake1)
sprites_group.add(food)

wall_group = pygame.sprite.Group()

SCOREHIGH = 0

def redraw(): # сверху скоре
    if playing:
        screen.fill(back)
        font_score = pygame.font.SysFont("times-new-roman", 24)
        score = font_score.render('score : ' + str(snake.score), True, BLUE)
        scoreRect = score.get_rect()
        scoreRect.center = (50, 40)
        screen.blit(score, scoreRect)
        # появление объектов
        sprites_group.update()
        sprites_group.draw(screen)
        wall_group.update()
        wall_group.draw(screen)
        pygame.display.update()
    else: # конец игры надписи
        screen.fill(BLACK)
        font_end = pygame.font.SysFont("times-new-roman", 55)
        title = font_end.render("Let's play, my little Sun <3", False, RED)
        titleRect = title.get_rect()
        titleRect.center = (wight//2, 100)
        screen.blit(title, titleRect)

        # high score
        high = font_end.render("High Score: " + str(SCOREHIGH), True, PURPLE)
        highRect = high.get_rect()
        highRect.center = (wight//2, 340)
        screen.blit(high, highRect)
        # lvl = font_end.render("You did" + str())

        # start
        font = pygame.font.SysFont("times-new-roman", 45)
        start = font.render("Press Space to Start again, pls", True, PURPLE)
        startRect = start.get_rect()
        startRect = (120, 520)
        screen.blit(start, startRect)


playing = False
with open('high_score.pkl', 'br') as f:
    SCOREHIGH = pickle.load(f)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(30)

    if playing:
       #  Snake movement


        snake.rect.x += snake.dx
        snake.rect.y += snake.dy
        snake1.rect.x += snake1.dx
        snake1.rect.y += snake1.dy
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            snake.dx = -snake.speed
            snake.dy = 0
        if key[pygame.K_RIGHT]:
            snake.dx = snake.speed
            snake.dy = 0
        if key[pygame.K_UP]:
            snake.dy = -snake.speed
            snake.dx = 0
        if key[pygame.K_DOWN]:
            snake.dy = snake.speed
            snake.dx = 0


        if key[pygame.K_d]:
            snake1.dx = snake.speed
            snake1.dy = 0
        if key[pygame.K_a]:
            snake1.dx = -snake.speed
            snake1.dy = 0
        if key[pygame.K_w]:
            snake1.dy = -snake.speed
            snake1.dx = 0
        if key[pygame.K_s]:
            snake1.dy = snake.speed
            snake1.dx = 0


        #  Collision
        if snake.rect.collidepoint(food.rect.x, food.rect.y):
            food.move()
            wall = Wall()
            wall.rect.x = snake.rect.x + 50
            wall.rect.y = snake.rect.y + 50
            wall_group.add(wall)
            snake.score+=1
            snake.size+=10


        if snake1.rect.collidepoint(food.rect.x, food.rect.y):
            food.move()
            wall1 = Wall()
            wall1.rect.x = snake1.rect.x + 50
            wall1.rect.y = snake1.rect.y + 50
            snake.score+=1
            wall_group.add(wall1)

        for wall in wall_group:
             if wall.rect.collidepoint(snake.rect.x, snake.rect.y):
                if snake.score > snake.hello:
                    snake.hello = snake.score
                playing = False
        for wall1 in wall_group:
            if wall1.rect.collidepoint(snake1.rect.x, snake1.rect.y):
                if snake.score > snake.hello:
                    snake.hello = snake.score
                playing = False


        if snake.rect.x < 0 or snake.rect.x > wight - size or snake.rect.y < 0 or snake.rect.y > height - size:
            playing = False
        if snake1.rect.x < 0 or snake1.rect.x > wight - size or snake1.rect.y < 0 or snake1.rect.y > height - size:
            playing = False
        # lvl
        if snake.score == 2:
            snake.score = 5
            snake.speed = 4

        if snake.score == 8:
            snake.score += 10
            snake.speed = 7
        if snake.score == 34:
            snake.score += 11
            snake.speed = 10
    else:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            playing = True
            snake.rect.x = wight // 2
            snake.rect.y = height // 2
            snake1.rect.x = wight // 2
            snake1.rect.y = height // 2
            snake.score = 0
            wall_group.empty()

    SCOREHIGH = max(snake.score, snake1.score, SCOREHIGH)
    redraw()
    pygame.display.update()
    pygame.display.flip()
with open('high_score.pkl', 'bw') as f:
    pickle.dump(SCOREHIGH, f)
pygame.quit()