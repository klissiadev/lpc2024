import pygame

pygame.init()

# Define colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_PADDLE = (30, 100, 200)

# screen size
WIDTH_SCREEN = 600
HEIGHT_SCREEN = 700

size = (WIDTH_SCREEN, HEIGHT_SCREEN)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout - PyGame Edition - 2024-09-17")

# level_attempt text
level_attempt_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
level_attempt_text = level_attempt_font.render('1      1', True, COLOR_WHITE)
level_attempt_text_rect = level_attempt_text.get_rect()
level_attempt_text_rect.center = (190, 50)

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
score_text = score_font.render('000    000', True, COLOR_WHITE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (270,100)

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_width = 50   # Width of the player
player_1_height = 15  # Height of the player
player_1_x = (WIDTH_SCREEN/2) - 25        # Initial x position
player_1_y = HEIGHT_SCREEN - 60   # y position near the bottom of the screen
player_1_move_right = False
player_1_move_left = False

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1_move_left = False
            if event.key == pygame.K_RIGHT:
                player_1_move_right = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_1_move_left = True
            if event.key == pygame.K_RIGHT:
                player_1_move_right = True

    # player 1 right movement
    if player_1_move_right:
        player_1_x -= 5
    else:
        player_1_x += 0

    # player 1 left movement
    if player_1_move_left:
        player_1_x += 5
    else:
        player_1_x += 0

    # player 1 collides with wall
    if player_1_x <= 0:
        player_1_x = 0
    elif player_1_x >= WIDTH_SCREEN - player_1_width:
        player_1_x = WIDTH_SCREEN - player_1_width

    # Drawing objects
    screen.fill(COLOR_BLACK)


    def wall_colors(width):
        pygame.draw.rect(screen, COLOR_RED, (width, 130, 10, 25))
        pygame.draw.rect(screen, COLOR_ORANGE, (width, 155, 10, 25))
        pygame.draw.rect(screen, COLOR_GREEN, (width, 180, 10, 25))
        pygame.draw.rect(screen, COLOR_YELLOW, (width, 205, 10, 25))
        pygame.draw.rect(screen, COLOR_PADDLE, (width, HEIGHT_SCREEN - 67, 10, 30))

    # Draw white borders: top, left, and right
    pygame.draw.rect(screen, COLOR_WHITE, (0, 0, WIDTH_SCREEN, 25))  # Top border
    pygame.draw.rect(screen, COLOR_WHITE, (0, 0, 10, HEIGHT_SCREEN))  # Left border
    wall_colors(0) # Left border color
    pygame.draw.rect(screen, COLOR_WHITE, (WIDTH_SCREEN - 10, 0, 10, HEIGHT_SCREEN))  # Right border
    wall_colors(WIDTH_SCREEN - 10) # Left border color

    pygame.draw.rect(screen, COLOR_PADDLE, (player_1_x, player_1_y, player_1_width, player_1_height))
    screen.blit(level_attempt_text, level_attempt_text_rect)
    screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()