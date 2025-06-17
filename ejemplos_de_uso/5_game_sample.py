import pygame

# Game constants
WIDTH = 800
HEIGHT = 600
BALL_SPEED = 3
PADDLE_SPEED = 6
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
FONT_SIZE = 36

def reset_game():
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    paddle1 = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    return ball, paddle1, paddle2, BALL_SPEED, BALL_SPEED, 0, 0

def move_paddles(keys, paddle1_rect, paddle2_rect):
    if keys[pygame.K_w] and paddle1_rect.top > 0:
        paddle1_rect.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1_rect.bottom < HEIGHT:
        paddle1_rect.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_rect.top > 0:
        paddle2_rect.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2_rect.bottom < HEIGHT:
        paddle2_rect.y += PADDLE_SPEED
		
def move_ball(ball_rect, ball_dx, ball_dy, paddle1_rect, paddle2_rect):
    ball_rect.x += ball_dx
    ball_rect.y += ball_dy

    # Bounce off top and bottom
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Bounce off paddles
    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        ball_dx = -ball_dx

    return ball_dx, ball_dy

def draw_elements(screen, ball_rect, paddle1_rect, paddle2_rect, score1, score2, font):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle1_rect)
    pygame.draw.rect(screen, (255, 255, 255), paddle2_rect)
    pygame.draw.ellipse(screen, (255, 255, 255), ball_rect)
    pygame.draw.aaline(screen, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = font.render(f"{score1}     {score2}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    font = pygame.font.SysFont(None, FONT_SIZE)
    clock = pygame.time.Clock()

    ball, paddle1, paddle2, ball_dx, ball_dy, score1, score2 = reset_game()

    print("Player 1: W (up), S (down)")
    print("Player 2: ↑ (up arrow), ↓ (down arrow)")
    print("Press SPACE to restart the match and reset points.")
    print("Press ESC to quit the game.")

    running = True
    while running:
		# Input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            running = False

        if keys[pygame.K_SPACE]:
            ball, paddle1, paddle2, ball_dx, ball_dy, score1, score2 = reset_game()

		# Logic
        move_paddles(keys, paddle1, paddle2)
        ball_dx, ball_dy = move_ball(ball, ball_dx, ball_dy, paddle1, paddle2)

        if ball.left <= 0:
            score2 += 1
            ball, paddle1, paddle2, ball_dx, ball_dy, _, _ = reset_game()
        elif ball.right >= WIDTH:
            score1 += 1
            ball, paddle1, paddle2, ball_dx, ball_dy, _, _ = reset_game()

		# Output
        draw_elements(screen, ball, paddle1, paddle2, score1, score2, font)
		
		# 60 FPS
        clock.tick(60)

    pygame.quit()

main_loop()
