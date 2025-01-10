import pygame
import random

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

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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

# Quit Pygame
pygame.quit()
quit()
