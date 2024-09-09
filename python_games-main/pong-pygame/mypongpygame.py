# Jucimar Jr
# 2024
# Ana Klissia Furtado Martins
# 2415310025

import pygame

pygame.init()

# Initialize the mixer module
pygame.mixer.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)

SCORE_MAX = 3
ROBOT_SPEED = 4

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2024-09-06")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 90)
victory_text = victory_font.render('- VICTORY -', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (300, 350)

# game over text
game_over_font = pygame.font.Font('assets/PressStart2P.ttf', 90)
game_over_text = victory_font.render('GAME OVER', True, COLOR_RED, COLOR_BLACK)
game_over_text_rect = score_text.get_rect()
game_over_text_rect.center = (400, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')
game_over_sound_effect = pygame.mixer.Sound('assets/game-over-arcade-6435.mp3')
game_over_sound_effect.set_volume(1.0)
game_over_played = False

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball_x < 100 and player_1_y < ball_y + 25 and player_1_y + 150 > ball_y:

            paddle_height = 150
            center_of_paddle = paddle_height / 2
            center_of_paddle_y = player_1_y + center_of_paddle
            distance_from_center = (ball_y + 25) - center_of_paddle_y

            if abs(distance_from_center) <= center_of_paddle * 0.2:  # CENTER
                ball_dx *= -2
                ball_dy = 0
            elif abs(distance_from_center) < center_of_paddle * 0.6:  # Near center
                ball_dx *= -0.9
                ball_dy = 4
            else:  # Near the tip
                if distance_from_center > 0:
                    ball_dx *= -1.05
                    if ball_dy == 0:
                        ball_dy = 4
                    else:
                        ball_dy *= -1.3
                else:
                    ball_dx *= -1.05
                    if ball_dy == 0:
                        ball_dy = 4
                    else:
                        ball_dy *= 1.3

            bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if ball_x > 1180 and player_2_y < ball_y + 25 and player_2_y + 150 > ball_y:

            paddle_height = 150
            center_of_paddle = paddle_height/2
            center_of_paddle_y = player_2_y + center_of_paddle
            distance_from_center = (ball_y + 25) - center_of_paddle_y

            if abs(distance_from_center) <= center_of_paddle * 0.1:  # Center
                ball_dx *= -1.3
                ball_dy = 0
            elif abs(distance_from_center) < center_of_paddle * 0.6:  # Near center
                ball_dx *= -0.9
                ball_dy = 4
            else:  # Near the tip
                if distance_from_center > 0:
                    ball_dx *= -1.05
                    if ball_dy == 0:
                        ball_dy = 4
                    else:
                        ball_dy *= -1.3
                else:
                    ball_dx *= -1.05
                    if ball_dy == 0:
                        ball_dy = 4
                    else:
                        ball_dy *= 1.3
            bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dx = 5
            ball_dy = 5
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dx = 5
            ball_dy = 5
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 5
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 5
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 570:
            player_1_y = 570

        # player 2 "Artificial Intelligence" with movement delay
        if ball_x > 640:
            if player_2_y < ball_y:
                player_2_y += ROBOT_SPEED
            elif player_2_y > ball_y:
                player_2_y -= ROBOT_SPEED
            # restrict bot collides with upper wall
            if player_2_y < 0:
                player_2_y = 0
            elif player_2_y > 570:
                player_2_y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        screen.blit(score_text, score_text_rect)
        if score_1 > score_2:  # drawing victory
            screen.fill(COLOR_BLACK)
            screen.blit(victory_text, victory_text_rect)
        else:  # drawing defeat
            screen.fill(COLOR_BLACK)
            screen.blit(game_over_text, game_over_text_rect)
            if not game_over_played:
                game_over_sound_effect.play()
                game_over_played = True

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
