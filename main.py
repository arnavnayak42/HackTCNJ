import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up player character
player_pos = [30, 30]
player_size = 20

# Set up end point
end_pos = [width - 30, height - 30]
end_size = 20

# Set up walls
walls = []
for i in range(10):
    wall_x = random.randint(0, width - 20)
    wall_y = random.randint(0, height - 20)
    wall_width = random.randint(50, 150)
    wall_height = random.randint(50, 150)
    walls.append(pygame.Rect(wall_x, wall_y, wall_width, wall_height))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get player input
    keys = pygame.key.get_pressed()
    
    if pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player_pos[1] -= .3
        if keys[pygame.K_s]:
            player_pos[1] += .3
        if keys[pygame.K_a]:
            player_pos[0] -= .3
        if keys[pygame.K_d]:
            player_pos[0] += .3

    # Check collision with walls
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for wall in walls:
        if player_rect.colliderect(wall):
            player_pos = [30, 30]  # Reset player position if collision occurs

    # Check if player reached the end point
    end_rect = pygame.Rect(end_pos[0], end_pos[1], end_size, end_size)
    if player_rect.colliderect(end_rect):
        print("You won!")
        running = False

    # Draw background
    screen.fill(BLACK)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, GREEN, wall)

    # Draw player character
    pygame.draw.rect(screen, WHITE, player_rect)

    # Draw end point
    pygame.draw.rect(screen, RED, end_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()