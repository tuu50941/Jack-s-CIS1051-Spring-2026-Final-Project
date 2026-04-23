import pygame
import sys
import random



# Board and font settings
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

# Create initial lists for both players
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

# Start with a random placeholder letter
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

# Display info on player letters, scores, selected_letter
def draw_status():
    status_text = f"{players[current_player]}'s turn | Scores: {scores[0]} - {scores[1]} | Letter: {selected_letter} | Shuffle: < | End Turn: > \n Player 1's: {player1Letters} | Player 2's: {player2Letters}"
    status_surface = font.render(status_text, True, BLUE)
    screen.blit(status_surface, (10, SCREEN_SIZE + 10))

# place letter on board
def place_tile(pos):
    global current_player
    x, y = pos
    col, row = x // TILE_SIZE, y // TILE_SIZE
    if row < BOARD_SIZE and board[row][col] == "":
        board[row][col] = selected_letter + " (" + str(letterPoints[selected_letter]) + ")"
        scores[current_player] += letterPoints[selected_letter]
        letterQuantities[selected_letter] -= 1
        # replace placed letters with a "" in player letter lists
        if current_player == 0:
            sLIndex = player1Letters.index(selected_letter)
            player1Letters[sLIndex] = ""
        elif current_player == 1:
            sLIndex2 = player2Letters.index(selected_letter)
            player2Letters[sLIndex2] = ""

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # if > pressed, end turn and refill empty spots in letter lists
            if event.unicode == ">":
                if current_player == 0:
                    for i in range(len(player1Letters)):
                        # if iterator reaches a certain amount,
                        # there may not be letters left to collect
                        endTurnIterator1 = 0
                        while player1Letters[i] == "":
                            player1Letters[i] = random.choice(list(letterPoints.keys()))
                            if endTurnIterator1 >= 52:
                                player1Letters[i] = "NA"
                            endTurnIterator1 += 1
                        if player1Letters[i] == "NA":
                            player1Letters[i] = ""
                elif current_player == 1:
                    for i in range(len(player2Letters)):
                        endTurnIterator2 = 0
                        while player2Letters[i] == "":
                            player2Letters[i] = random.choice(list(letterPoints.keys()))
                            if endTurnIterator2 >= 52:
                                player2Letters[i] = "NA"
                            endTurnIterator2 += 1
                        if player2Letters[i] == "NA":
                            player2Letters[i] = ""
                current_player = (current_player + 1) % 2
            # if < pressed, reshuffle letters given to current player and
            # end their turn
            elif event.unicode == "<":
                if current_player == 0:
                    for i in range(len(player1Letters)):
                        shuffleLetter1 = random.choice(list(letterPoints.keys()))
                        shuffleIterator1 = 0
                        # keep shuffling until player has 7 letters again
                        while letterQuantities[shuffleLetter1] == 0:
                            shuffleLetter1 = random.choice(list(letterPoints.keys()))
                            if shuffleIterator1 >= 52:
                                player2Letters[i] = "NA"
                            shuffleIterator1 += 1
                        if player1Letters[i] == "NA":
                            player1Letters[i] = ""
                        else:
                            player1Letters[i] = shuffleLetter1
                elif current_player == 1:
                    for i in range(len(player2Letters)):
                        shuffleLetter2 = random.choice(list(letterPoints.keys()))
                        shuffleIterator2 = 0
                        while letterQuantities[shuffleLetter2] == 0:
                            shuffleLetter2 = random.choice(list(letterPoints.keys()))
                            if shuffleIterator2 >= 52:
                                player2Letters[i] = "NA"
                            shuffleIterator2 += 1
                        if player2Letters[i] == "NA":
                            player2Letters[i] = ""
                        else:
                            player2Letters[i] = shuffleLetter2
                current_player = (current_player + 1) % 2
            # if a typed letter is in a player's letter list, it becomes
            # selected_letter                
            elif event.unicode.isalpha() and len(event.unicode) == 1:
                letterTyped = event.unicode.upper()
                if current_player == 0 and letterTyped in player1Letters:
                    selected_letter = letterTyped
                if current_player == 1 and letterTyped in player2Letters:
                    selected_letter = letterTyped
        # if certain tile clicked while a certain letter is selected that
        # still has a quantity greater than 0, place the letter 
        elif event.type == pygame.MOUSEBUTTONDOWN and letterQuantities[selected_letter] > 0:
            place_tile(pygame.mouse.get_pos())

    draw_board()
    draw_status()
    pygame.display.flip()
