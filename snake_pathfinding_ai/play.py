from snake import *
from square import *
from os import environ


def draw_screen(surface):
    surface.fill(SURFACE_CLR)


def draw_grid(surface):
    x = 0
    y = 0

    for r in range(ROWS):
        x = x + SQUARE_SIZE
        y = y + SQUARE_SIZE
        #pygame.draw.line(surface(sth to draw on), color, start_pos, end_pos)
        #draw vertically
        pygame.draw.line(surface, GRID_CLR, (x, 0), (x, HEIGHT))
        #draw horizontally
        pygame.draw.line(surface, GRID_CLR, (0, y), (WIDTH, y))


def play_game():
    pygame.init()
    environ['SDL_VIDEO_CENTERED'] = '1' #center our screen
    pygame.display.set_caption("Snake BFS")
    game_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() #Create clock object to work with time
    snake = Snake(game_surface) #Create the snake object

    run = True
    while run:
        #draw the screen or the board
        draw_screen(game_surface) 
        #draw the separating lines betweene each square
        draw_grid(game_surface)

        snake.update()
        clock.tick(1)
        pygame.display.update() # make the display appear of the monitor

#is used to execute some code only if the file was run directly, and not imported
if __name__ == '__main__':
    play_game()
