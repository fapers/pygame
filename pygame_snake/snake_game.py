# Snake Game!
# by root

# our game imports
import pygame, sys, random, time

# check for initializing errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print(f'(!) Had {check_errors[1]} initializing errors, existing...')
    sys.exit(-1)
else:
    print(f'(+) PyGame successfully initialized!')

# Play surface
play_surface = pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game!")

# Colors
red = pygame.Color(255,0,0) # gameover
green = pygame.Color(0,255,0) # snake
black = pygame.Color(0,0,0) # score
white = pygame.Color(255,255,255) # background
brown = pygame.Color(165,42,42) # food

# FPS controller
fps_controller = pygame.time.Clock()

# Important variables
snake_pos = [100, 50]
snake_body = [[100,50],[90,50],[80,50]]

food_pos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
food_spawn = True

direction = 'RIGHT'
changeto = direction

score = 0

# Game over function
def game_over():
    my_font = pygame.font.SysFont('monaco', 72)
    go_surf = my_font.render('Game over!', True, red)
    go_rect = go_surf.get_rect()
    go_rect.midtop = (360,15)
    play_surface.blit(go_surf,go_rect)    
    show_score(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() # pygame exit
    sys.exit() # console exit

def show_score(choice=1):
    s_font = pygame.font.SysFont('monaco', 24)
    s_surf = s_font.render(f'Score: {score}', True, black)
    s_rect = s_surf.get_rect()
    if choice == 1:
        s_rect.midtop = (80,10)
    else:
        s_rect.midtop = (360,120)
    play_surface.blit(s_surf, s_rect)

# Main Logic of the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    
    # Update snake position  [x,y]
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
        
    # Snake body mechanism
    snake_body.insert(0,list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    # Food Spawn
    if food_spawn == False:
        food_pos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
    food_spawn = True
    
    play_surface.fill(white)
    for pos in snake_body:        
        pygame.draw.rect(play_surface, green, 
        pygame.Rect(pos[0],pos[1],10,10))
    
    pygame.draw.rect(play_surface, brown, 
    pygame.Rect(food_pos[0],food_pos[1],10,10))
    
    if snake_pos[0] > 710 or snake_pos[0] < 0:
        game_over()
    if snake_pos[1] > 450 or snake_pos[1] < 0:
        game_over()
        
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()    
    
    show_score()
    pygame.display.flip()
    
    fps_atual = 10
    match score:
        case 10:
            fps_atual += 10
        case 20:
            fps_atual += 20
        case _:
            fps_atual = fps_atual    
    fps_controller.tick(fps_atual)
