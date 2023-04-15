import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)  # Black
PLAYER_COLOR = (0, 255, 0)  # Green
ENEMY_COLOR = (255, 0, 0)  # Red
DOOR_COLOR = (0, 0, 255)  # Blue

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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        trivia_question = {
            "What is the capital of France": "Paris",
            "How tall is Lebron James": "6'7",
            "Which country has the highest population": "China"
        }
print(trivia_questions[1])
#Create sprites
player = Player()
enemy = Enemy()
door = Door("")