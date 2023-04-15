import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)  # Black
PLAYER_COLOR = (0, 255, 0)  # Green
ENEMY_COLOR = (255, 0, 0)  # Red
DOOR_COLOR = (0, 0, 255)  # Blue
WHITE = (255,255,255)

window = pygame.display.set_mode((800, SCREEN_HEIGHT)) 

# Maze
maze = [
    "##########",
    "#  #  #  #",
    "#  #  #  #",
    "#        #",
    "#  #  #  #",
    "#  #  #  #",
    "#        #",
    "#  #  #  #",
    "#  #  #  #",
    "##########",
]

# Trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal on Earth?": "Blue whale",
    "What is the chemical symbol for gold?": "Au",
    "What is the tallest mountain in the world?": "Mount Everest",
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Maze Game")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

    def update(self, walls):
        # Check for collision with walls
        hits = pygame.sprite.spritecollide(self, walls, False)
        for hit in hits:
            if self.rect.colliderect(hit.rect):
                if self.rect.right > hit.rect.left and self.rect.left < hit.rect.left:
                    self.rect.right = hit.rect.left
                elif self.rect.left < hit.rect.right and self.rect.right > hit.rect.right:
                    self.rect.left = hit.rect.right
                elif self.rect.bottom > hit.rect.top and self.rect.top < hit.rect.top:
                    self.rect.bottom = hit.rect.top
                elif self.rect.top < hit.rect.bottom and self.rect.bottom > hit.rect.bottom:
                    self.rect.top = hit.rect.bottom

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - 40
        self.rect.y = SCREEN_HEIGHT - 40

    def update(self):
        # Move enemy randomly
        direction = random.choice(["left", "right", "up", "down"])
        if direction == "left":
            self.rect.x -= 2
        elif direction == "right":
            self.rect.x += 2
        elif direction == "up":
            self.rect.y -= 2
        elif direction == "down":
            self.rect.y += 2

# Door class
class Door(pygame.sprite.Sprite):
    def __init__(self, trivia_question, answer):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(DOOR_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(40, SCREEN_WIDTH - 60)
        self.trivia_question = trivia_question
        self.answer = answer
#Create sprites
player = Player()
enemy = Enemy()
door = Door("What is the capital of France", "Paris")
pygame.sprite.Group.add(player,enemy,door)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check collision between player and enemy
    if pygame.sprite.collide_rect(player, enemy):
        print("Game Over! You were caught by the enemy!")
        running = False

    # Check collision between player and door
    if pygame.sprite.collide_rect(player, door):
        # Display trivia question and get player's answer
        answer = input(door.trivia_question + " ")
        if answer.lower() == door.answer.lower():
            print("Correct! Door unlocked.")
            door.kill()
        else:
            print("Incorrect answer. Try again.")

    pygame.sprite.Group.update()

    # Draw sprites on game window
    window.fill(WHITE)
    pygame.sprite.Group.draw(window)
    pygame.display.flip()

pygame.quit()