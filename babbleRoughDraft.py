import pygame
import sys
import random


########### TRY TO COMBINE BABBLE TEST 1 AND 2
########### BABBLETEST1 HAS RANDOM LETTERS AND SCORES
########### BABBLETEST2 HAS THE BOARD AND CLICKING TO PLACE LETTERS

########### REMOVE LETTERS PLACED AND ADD NEW RANDOM ONES ONCE A PLAYER'S TURN
########### HAS ENDED (> IS ENTERED)

########### ADD A FEATURE THAT LETS PLAYERS RESHUFFLE THEIR LETTERS


# --- Game Settings ---
TILE_SIZE = 40
BOARD_SIZE = 15
SCREEN_SIZE = TILE_SIZE * BOARD_SIZE
FONT_SIZE = 24

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 50))
pygame.display.set_caption("Two-Player Babble")
font = pygame.font.Font(None, FONT_SIZE)

# Board: 2D array for letters
board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Players and Letters Settings
players = ["Player 1", "Player 2"]
scores = [0, 0]
player1Letters = ["","","","","","",""]
player2Letters = ["","","","","","",""]
current_player = 0
letterPoints = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,
                "K":5,"L":1,"M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,
                "U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
letterQuantities = {"A":9,"B":2,"C":2,"D":4,"E":12,"F":2,"G":3,"H":2,"I":9,
                    "J":1,"K":1,"L":4,"M":2,"N":6,"O":8,"P":2,"Q":1,"R":6,
                    "S":4,"T":6,"U":4,"V":2,"W":2,"X":1,"Y":2,"Z":1}

#Create initial lists for both players
for i in range(len(player1Letters)):
    randomLetter = random.choice(list(letterPoints.keys()))
    while letterQuantities[randomLetter] <= 0:
        randomLetter = random.choice(list(letterPoints.keys()))
    player1Letters[i] = randomLetter
    letterQuantities[randomLetter] -= 1
    randomLetter2 = random.choice(list(letterPoints.keys()))
    while letterQuantities[randomLetter2] <= 0:
        randomLetter2 = random.choice(list(letterPoints.keys()))
    player2Letters[i] = randomLetter2
    letterQuantities[randomLetter2] -= 1

#Start with a random placeholder letter
selected_letter = random.choice(list(letterPoints.keys()))

def draw_board():
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)
            if board[row][col] != "":
                letter_surface = font.render(board[row][col], True, BLACK)
                screen.blit(letter_surface, (col * TILE_SIZE + 10, row * TILE_SIZE + 8))

def draw_status():
    status_text = f"{players[current_player]}'s turn | Scores: {scores[0]} - {scores[1]} | Letter: {selected_letter} \n Player 1's: {player1Letters} | Player 2's: {player2Letters}"
    status_surface = font.render(status_text, True, BLUE)
    screen.blit(status_surface, (10, SCREEN_SIZE + 10))

def place_tile(pos):
    global current_player
    x, y = pos
    col, row = x // TILE_SIZE, y // TILE_SIZE
    if row < BOARD_SIZE and board[row][col] == "":
        board[row][col] = selected_letter + " (" + str(letterPoints[selected_letter]) + ")"
        scores[current_player] += letterPoints[selected_letter]
        letterQuantities[selected_letter] -= 1
        #replace placed letters with a ""
        if current_player == 0:
            sLIndex = player1Letters.index(selected_letter)
            player1Letters[sLIndex] = ""
        elif current_player == 1:
            sLIndex2 = player2Letters.index(selected_letter)
            player2Letters[sLIndex2] = ""

# --- Main Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.unicode == ">":
                current_player = (current_player + 1) % 2
            elif event.unicode.isalpha() and len(event.unicode) == 1:
                letterTyped = event.unicode.upper()
                if current_player == 0 and letterTyped in player1Letters:
                    selected_letter = letterTyped
                if current_player == 1 and letterTyped in player2Letters:
                    selected_letter = letterTyped

        elif event.type == pygame.MOUSEBUTTONDOWN and letterQuantities[selected_letter] > 0:
            place_tile(pygame.mouse.get_pos())

    draw_board()
    draw_status()
    pygame.display.flip()
