import random
import pygame


pygame.init()
score = 0
width = 1000
height = 600
block_size = 25
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame basics")

background = ("black")
snake = [(100,100)]

dir = (block_size,0)

clocl = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Papyrus",20)


fx = random.randint(0, width//block_size-1)
fy = random.randint(0,height//block_size-1)
food = (fx * block_size, fy *block_size)



def draw_grid():
    for i in range(0,width,block_size):
        pygame.draw.line(screen,"White",(i,0),(i,height),1)
    for j in range(0,height,block_size):
        pygame.draw.line(screen,"white",(0,j), (width,j),1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dir = (block_size,0)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dir = (-block_size,0)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dir = (0,block_size)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                dir = (0,-block_size)




    screen.fill(background)
    # draw_grid()

    new_pos = (snake[0][0] + dir[0],snake[0][1] + dir[1])
    # snake[0] =  new_pos

    if (new_pos in snake or new_pos[0] < 0 or new_pos[0] >= width or new_pos[1] < 0 or new_pos[1] >= height):
        running = False

    snake.insert(0,new_pos)

    if new_pos == food:
        fx = random.randint(0, width // block_size - 1)
        fy = random.randint(0, height // block_size - 1)
        food = (fx * block_size, fy * block_size)
        score = score +1

    else:
        snake.pop()

    for block in snake:
        pygame.draw.rect(screen,"green",(block[0],block[1],block_size,block_size))


    # pygame.draw.rect(screen,"green",(snake[0][0], snake[0][1], block_size,block_size))

    pygame.draw.rect(screen,"red",(food[0], food[1], block_size,block_size))

    text_score = font.render(f"Score: {score}", True, 'white')
    screen.blit(text_score,(900,20))

    pygame.display.flip()
    clocl.tick(10)
