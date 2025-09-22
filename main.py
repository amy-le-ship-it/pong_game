import pygame
import random

# Settings
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")
    clock = pygame.time.Clock()

    # Players
    player_1_rect = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)
    player_2_rect = pygame.Rect(SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50, 7, 100)
    player_1_move = 0
    player_2_move = 0

    # Ball
    ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)
    ball_accel_x = random.choice([-1, 1]) * random.randint(2, 4) * 0.3
    ball_accel_y = random.choice([-1, 1]) * random.randint(2, 4) * 0.3

    started = False
    running = True

    while running:
        delta_time = clock.tick(60)
        screen.fill(COLOR_BLACK)

        # Start screen
        if not started:
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('Press SPACE to Start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if not started and event.key == pygame.K_SPACE:
                    started = True
                # Paddle controls
                if event.key == pygame.K_w:
                    player_1_move = -0.5
                if event.key == pygame.K_s:
                    player_1_move = 0.5
                if event.key == pygame.K_UP:
                    player_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    player_2_move = 0.5

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_w, pygame.K_s):
                    player_1_move = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player_2_move = 0

        player_1_rect.top += player_1_move * delta_time
        player_2_rect.top += player_2_move * delta_time
        
        # Game logic
        if started:
            # Move paddles
            player_1_rect.y += player_1_move * delta_time
            player_2_rect.y += player_2_move * delta_time

            # Move ball
            ball_rect.x += ball_accel_x * delta_time
            ball_rect.y += ball_accel_y * delta_time

            # Ball collisions
            if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
                ball_accel_y *= -1
            if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
                running = False  # End game when ball leaves screen

            if ball_rect.colliderect(player_1_rect) or ball_rect.colliderect(player_2_rect):
                ball_accel_x *= -1

            # Draw everything
            pygame.draw.rect(screen, COLOR_WHITE, player_1_rect)
            pygame.draw.rect(screen, COLOR_WHITE, player_2_rect)
            pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

            pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
