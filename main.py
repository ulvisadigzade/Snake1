# Example file showing a circle moving on screen
import pygame
import random
# pygame setup
pygame.init()
pygame.font.init()      
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((1250, 700))
clock = pygame.time.Clock()
running = True
dt = 0
x,y=0,0
prev_pressed=0
sqrsize=50
score=0



def randomapple():
    x,y = random.randrange(50,1250,50),random.randrange(5,700,50)
    return x,y

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
a,b = randomapple()
player_pos = pygame.Vector2(a,b)
snake = [[player_pos.x,player_pos.y]]

def drawsnake():
    pygame.draw.rect(screen,"purple",(snake[0][0],snake[0][1],50,50))
    for i in range(1,len(snake)):
        pygame.draw.rect(screen,"green",(snake[i][0],snake[i][1],50,50))

def movesnake(s,x,y):
    if not(x==y==0):
        for i in range(len(snake) - 1, 0, -1):
            snake[i][0] = snake[i - 1][0]
            snake[i][1] = snake[i - 1][1]
    
        snake[0][0]+=x
        snake[0][1]+=y

#rec = pygame.rect.Rect(screen,"green",(player_pos[0],player_pos[1],50,50))
def appendsquare(x,y):
    ln = len(snake)-1
    if x:
        snake.append([snake[ln][0]-50,snake[ln][1]])
    else:
        snake.append([snake[ln][0],snake[ln][1]-50])

def reset():
    a,b = randomapple()
    snake.clear()
    snake.append([a,b])

def lost(x,y):
    x,y = snake[0][0],snake[0][1]
    for i in range(2,len(snake)):
        if snake[0]==snake[i]:
            return 1
    if x+25>=1280 or x-25<=0 or y+10>=720 or y-10<=0:
        return 1
    return 0
    

ranpos1,ranpos2 = randomapple()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    score_surf = my_font.render(f"Score: {score}",False,(255,255,255))
    screen.blit(score_surf,(0,0))


    drawsnake()
    pygame.draw.rect(screen,"red",(ranpos1,ranpos2,50,50))


    #change movement distantion
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and prev_pressed!=2:
        prev_pressed=1
        x,y=0,-sqrsize
    elif keys[pygame.K_s] and prev_pressed!=1:
        prev_pressed=2
        x,y=0,sqrsize
    elif keys[pygame.K_a] and prev_pressed!=4:
        x,y=-sqrsize,0
        prev_pressed=3
    elif keys[pygame.K_d] and prev_pressed!=3:
        x,y=sqrsize,0
        prev_pressed=4

    if lost(x,y):
        reset()

    movesnake('a',x,y)

    if snake[0]==[ranpos1,ranpos2]:
        appendsquare(x,y)
        score+=10
        ranpos1,ranpos2 = randomapple()

    # flip() the display to put your work on screens
    pygame.display.flip()

    clock.tick(10)

pygame.quit()