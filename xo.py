import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
grid = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = "X"  
game_over = False

def check_winner(player):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == player:
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] == player:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
        return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            x, y = event.pos
            col = x // 166
            row = y // 166
            if grid[row][col] == "":
                grid[row][col] = current_player
                if check_winner(current_player):
                    print(f"Le joueur {current_player} a gagné!")
                    game_over = True
                current_player = "O" if current_player == "X" else "X"

    screen.fill("black")
    for i in range(1, 3):
        pygame.draw.line(screen, "white", (i * 166, 0), (i * 166, 500), 3)
        pygame.draw.line(screen, "white", (0, i * 166), (500, i * 166), 3)
    font = pygame.font.SysFont(None, 100)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == "X":
                text = font.render("X", True, "white")
                screen.blit(text, (j * 166 + 50, i * 166 + 50))
            elif grid[i][j] == "O":
                text = font.render("O", True, "white")
                screen.blit(text, (j * 166 + 50, i * 166 + 50))

    pygame.display.flip()

pygame.quit()
