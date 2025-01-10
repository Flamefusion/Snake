import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Set window dimensions
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Font
font_style = pygame.font.SysFont(None, 30)

# Function to display text
def display_text(text, color, x, y):
    text_surface = font_style.render(text, True, color)
    window.blit(text_surface, (x, y))

# Game start screen
def game_start_screen():
    window.fill(black)
    display_text("Press any key to start", white, 150, 170)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game over screen
def game_over_screen(score):
    window.fill(black)
    display_text("Game Over", red, 250, 100)
    display_text("Your Score: " + str(score), white, 220, 150)
    display_text("Press any key to restart", white, 150, 200)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_loop()

# Snake initial position and size
snake_x = window_width / 2
snake_y = window_height / 2
snake_size = 10
snake_list = []
snake_length = 1

# Food initial position
food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

# Game variables
game_over = False
clock = pygame.time.Clock()
snake_speed = 15
x_change = 0
y_change = 0
score = 0

# Function to display the snake
def display_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, green, [x, y, snake_size, snake_size])

# Main game loop
def game_loop():
    global snake_x, snake_y, snake_list, snake_length, food_x, food_y, game_over, x_change, y_change, score

    snake_x = window_width / 2
    snake_y = window_height / 2
    snake_list = []
    snake_length = 1
    food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
    game_over = False
    x_change = 0
    y_change = 0
    score = 0
    start_time = time.time()  # Record start time

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != snake_size:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -snake_size:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != snake_size:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change != -snake_size:
                    y_change = snake_size
                    x_change = 0

        # Check for boundaries
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        # Update snake position
        snake_x += x_change
        snake_y += y_change

        # Add snake head to list
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        # Maintain snake length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for self-collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        # Clear the window
        window.fill(black)

        # Draw food
        pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])

        # Draw snake
        display_snake(snake_list)

        # Display live score and time
        play_time = round(time.time() - start_time)
        display_text("Score: " + str(score), white, 10, 10)
        display_text("Time: " + str(play_time) + "s", white, 510, 10)

        # Update display
        pygame.display.update()

        # Check for food collision
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            snake_length += 1
            score += 1

        # Control game speed
        clock.tick(snake_speed)

    game_over_screen(score)

# Start the game
game_start_screen()
game_loop()

pygame.quit()
quit()
