import pygame
from pygame.locals import *

pygame.init()

ttt_screen_size = (600, 600)
ttt_color_fill      = (0, 255, 0)
ttt_cell_line_fill = (255, 0, 0)
ttt_win_line_fill = (255, 255, 0)
ttt_cell_line_width = 4
ttt_win_line_width = 7
ttt_x_color_fill = (0, 0, 255)
ttt_o_color_fill = (10, 100, 255)

ttt_screen = pygame.display.set_mode(ttt_screen_size, 0, 32)
ttt_screen.fill(ttt_color_fill)

pygame.display.set_caption('Tic Tac Toe 1.0')
player = 'X'
ttt_board_state =\
            [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]

def is_pos_available(col, row):
    global ttt_board_state
    return ttt_board_state[row][col] == None

def initialize_ttt_board(ttt_screen):
    global ttt_board, ttt_color_fill, ttt_cell_line_fill, ttt_cell_line_width
    ttt_board = pygame.Surface(ttt_screen.get_size())
    ttt_board = ttt_board.convert()
    ttt_board.fill((ttt_color_fill))

    ## draw rows
    pygame.draw.line(ttt_board, ttt_cell_line_fill, (0, 199), (599, 199),
                     ttt_cell_line_width)
    pygame.draw.line(ttt_board, ttt_cell_line_fill, (0, 399), (599, 399),
                     ttt_cell_line_width)

    ## draw columns
    pygame.draw.line(ttt_board, ttt_cell_line_fill, (199, 0), (199, 599),
                     ttt_cell_line_width)
    pygame.draw.line(ttt_board, ttt_cell_line_fill, (399, 0), (399, 599),
                     ttt_cell_line_width)

    return ttt_board

def draw_winner_row(row_num):
    global ttt_board, ttt_win_line_fill, ttt_win_line_width
    start, end = (0, 0), (0, 0)
    if row_num == 0:
        start, end = (0, 99), (599, 99)
    elif row_num == 1:
        start, end = (0, 299), (599, 299)
    elif row_num == 2:
        start, end = (0, 499), (599, 499)
    pygame.draw.line(ttt_board, ttt_win_line_fill, start, end,
                     ttt_win_line_width)

def draw_winner_col(col_num):
    global ttt_board, ttt_win_line_fill, ttt_win_line_width
    start, end = (0, 0), (0, 0)
    if col_num == 0:
        start, end = (99, 0), (99, 599)
    elif col_num == 1:
        start, end = (299, 0), (299, 599)
    elif col_num == 2:
        start, end = (499, 0), (499, 599)
    pygame.draw.line(ttt_board, ttt_win_line_fill, start, end,
                     ttt_win_line_width)

def draw_winner_diag(diag_num):
    global ttt_board, ttt_win_line_fill, ttt_win_line_width
    start, end = (0, 0), (0, 0)
    if diag_num == 0:
        start, end = (0, 0), (599, 599)
    elif diag_num == 1:
        start, end = (599, 0), (0, 599)
    pygame.draw.line(ttt_board, ttt_win_line_fill, start, end,
                     ttt_win_line_width)

def draw_draw():
    for x in xrange(0, 3):
        draw_winner_row(x)
        draw_winner_col(x)
    draw_winner_diag(0)
    draw_winner_diag(1)

def display_ttt_board(ttt_board, ttt_screen):
    ttt_screen.blit(ttt_board, (0, 0))
    pygame.display.flip()

def mouse_click_to_ttt_board_pos(mouse_click_x, mouse_click_y):
    col, row = -1, -1
    if mouse_click_x < 200:
        col = 0
    elif mouse_click_x < 400:
        col = 1
    elif mouse_click_x < 600:
        col = 2

    if mouse_click_y < 200:
        row = 0
    elif mouse_click_y < 400:
        row = 1
    elif mouse_click_y < 600:
        row = 2

    return col, row

def draw_o_player(ttt_board, cell_center_x, cell_center_y):
    global ttt_o_color_fill
    pygame.draw.circle(ttt_board, ttt_o_color_fill, (cell_center_x, cell_center_y), 80, 2)

def draw_x_player(ttt_board, cell_center_x, cell_center_y):
    pygame.draw.line(ttt_board, ttt_x_color_fill,
                         (cell_center_x - 55, cell_center_y - 55),
                         (cell_center_x + 55, cell_center_y + 55),
                         2)
    pygame.draw.line(ttt_board, ttt_x_color_fill,
                         (cell_center_x + 55, cell_center_y - 55),
                         (cell_center_x - 55, cell_center_y + 55),
                         2)

def draw_ttt_player(ttt_board, player, col, row):
    global ttt_board_state
    cell_center_x = col * 200 + 99
    cell_center_y = row * 200 + 99
    if player == 'O':
        draw_o_player(ttt_board, cell_center_x, cell_center_y)
    elif player == 'X':
        draw_x_player(ttt_board, cell_center_x, cell_center_y)
    ttt_board_state[row][col] = player
    print ttt_board_state

def switch_ttt_player():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

def capture_mouse_click(ttt_board):
    global player
    mouse_click_x, mouse_click_y = pygame.mouse.get_pos()
    col, row = mouse_click_to_ttt_board_pos(mouse_click_x, mouse_click_y)
    if is_pos_available(col, row):
        draw_ttt_player(ttt_board, player, col, row)
        switch_ttt_player()
    
def is_game_over():
    if is_winner('X'): return True
    if is_winner('O'): return True
    if all_cells_occupied(): return True
    return False

def is_winner(player):
    global ttt_board_state
    if ttt_board_state[0][0] == ttt_board_state[0][1] == ttt_board_state[0][2] == player:
        draw_winner_row(0)
        return True
    if ttt_board_state[1][0] == ttt_board_state[1][1] == ttt_board_state[1][2] == player:
        draw_winner_row(1)
        return True
    if ttt_board_state[2][0] == ttt_board_state[2][1] == ttt_board_state[2][2] == player:
        draw_winner_row(2)
        return True
    if ttt_board_state[0][0] == ttt_board_state[1][0] == ttt_board_state[2][0] == player:
        draw_winner_col(0)
        return True
    if ttt_board_state[0][1] == ttt_board_state[1][1] == ttt_board_state[2][1] == player:
        draw_winner_col(1)
        return True
    if ttt_board_state[0][2] == ttt_board_state[1][2] == ttt_board_state[2][2] == player:
        draw_winner_col(2)
        return True
    if ttt_board_state[0][0] == ttt_board_state[1][1] == ttt_board_state[2][2] == player:
        draw_winner_diag(0)
        return True
    if ttt_board_state[0][2] == ttt_board_state[1][1] == ttt_board_state[2][0] == player:
        draw_winner_diag(1)
        return True
    return False

def all_cells_occupied():
    global ttt_board_state
    for row in ttt_board_state:
        for cell_val in row:
            if cell_val == None:
                return False
    return True

def is_draw():
    return not is_winner('X') and  not is_winner('O') and all_cells_occupied()

ttt_board = initialize_ttt_board(ttt_screen)
is_game_on = True
while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                exit(0)
            elif event.type == MOUSEBUTTONDOWN and is_game_on == True:
                capture_mouse_click(ttt_board)
                
            if is_game_on == True:
                display_ttt_board(ttt_board, ttt_screen)
        
            if is_game_over() and is_game_on == True:
                is_game_on = False 
                if is_draw(): draw_draw()
                display_ttt_board(ttt_board, ttt_screen)    
    except pygame.error, e:
        del ttt_screen
        pygame.display.quit()
        print e
    
            









