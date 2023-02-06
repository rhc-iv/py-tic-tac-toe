import random

from art import text2art

from bot import bot_turn
from player import Player

# VARIABLES/CONSTANTS/ETC:
num_players = 0
starter = ''
symbol = ''
display = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = False
player1 = Player()
player2 = Player()
player1.name = 'Player 1'
draw = text2art('tic\n'
                'tac\n'
                'toe',
                font='block',
                chr_ignore=True
                )


# CREATE THE GAME BOARD:
def draw_grid(moves):
    count = 0
    for i in range(1, 4):
        print(f'-------------------\n|  {moves[count]}  |'
              f'  {moves[count + 1]}  |  {moves[count + 2]}  '
              f'|\n-------------------')
        count += 3
    print('\n\n')


# PROMPT FOR PLAYER:
def get_move(player, player_next, status):
    entry = 0
    # IF PLAYER, SELECT ENTRY. IF AI, SELECT ENTRY:
    if player.bot:
        entry = bot_turn(status, create_sequence(status), player_next, player)
    else:
        while entry < 1 or entry > 9:
            try:
                entry = int(input(
                    f'{player.name}, where would you like to move? Enter '
                    f'1-9:\n'))
            # IF ENTRY IS INVALID, ASK AGAIN FOR INPUT:
            except ValueError:
                entry = 0
            # CHECK TO SEE IF GRID SQUARE IS OPEN:
            if entry not in player.move_options:
                entry = 0
    # UPDATE BOARD/POSSIBLE MOVES BASED ON CURRENT BOARD STATUS:
    player.moves.append(entry)
    player.move_options.remove(entry)
    player_next.move_options.remove(entry)
    player.turn = False
    player_next.turn = True
    display[entry - 1] = player.symbol
    draw_grid(display)
    return check_for_win(display, player)


# DECLARE WINNER IF WIN CONDITION EXISTS:
def declare_win(player):
    print(f'\nCongratulations! {player.name}, has won!')
    return


def create_sequence(status):
    sequence = [str(status[0]) + str(status[1]) + str(status[2]),
                str(status[3]) + str(status[4]) + str(status[5]),
                str(status[6]) + str(status[7]) + str(status[8]),
                str(status[0]) + str(status[3]) + str(status[6]),
                str(status[1]) + str(status[4]) + str(status[7]),
                str(status[2]) + str(status[5]) + str(status[8]),
                str(status[0]) + str(status[4]) + str(status[8]),
                str(status[2]) + str(status[4]) + str(status[6])
                ]
    return sequence


# WIN CONDITION CHECK AFTER EACH PLAYER'S MOVE:
def check_for_win(status, player):
    sequence = create_sequence(status)
    win = False
    for i in range(0, 8):
        if sequence[i] == player.winning_sequence:
            win = True
            declare_win(player)
            break
    return win


# CREATES THE INITIAL GAME BOARD IN THE CONSOLE:
draw_grid(display)

# INPUT FOR NO. OF PLAYERS:
while num_players != '1' and num_players != '2':
    num_players = input(
        'To play vs. computer, enter "1". To play head-to-head, enter "2".\n')

# INPUT CHOICE FOR TURNS:
if num_players == '2':
    player2.name = 'Player 2'
    while starter != '1' and starter != '2' and (
        starter != 'r' and starter != 'R'):
        starter = input(
            'Press "1" or "2" to determine who goes first, or "R" for '
            'Random.\n')
# IF GAME CHOICE IS PLAYER VS. AI:
else:
    player2.name = 'bot'
    player2.bot = True
    while starter != '1' and (starter != 'b' and starter != 'B') and (
        starter != 'r' and starter != 'R'):
        starter = input(
            'Should you or the AI go first? Enter 1 for you, '
            '"B" for the AI, or "R" for Random.\n')
    if starter.upper() == 'B':
        starter = '2'

# IF FIRST MOVE SELECTED IS RANDOM:
if starter.upper() == 'R':
    starter = random.randint(1, 2)
    if starter == 1:
        player1.turn = True
    else:
        player2.turn = True
elif starter == '1':
    player1.turn = True
else:
    player2.turn = True

# INPUT FOR PLAYER CHARACTER ("X" or "O")
while symbol != 'X' and symbol != 'O':
    if num_players == '2':
        symbol = input(
            f'Player {starter}, would you like to be "X" or "O"?\n').upper()
    # INPUT DIALOG FOR PLAYER VS. AI CHARACTER CHOICE:
    else:
        symbol = input(f'Would you like to be "X" or "O"?\n').upper()

# APPLIES CHARACTER CHOICE FROM INPUT & VARIABLE FOR WIN CONDITION:
if int(starter) == 1:
    player1.symbol = symbol
    player1.winning_sequence = symbol + symbol + symbol
    if symbol.upper() == 'X':
        player2.symbol = 'O'
        player2.winning_sequence = 'OOO'
    else:
        player2.symbol = 'X'
        player2.winning_sequence = 'XXX'
else:
    player2.symbol = symbol
    player2.winning_sequence = symbol + symbol + symbol
    if symbol.upper() == 'X':
        player1.symbol = 'O'
        player1.winning_sequence = 'OOO'
    else:
        player1.symbol = 'X'
        player1.winning_sequence = 'XXX'

draw_grid(display)

# LOOP THRU BOARD (PRESENT STATE) TO CHECK WIN CONDITION:
for i in range(1, 10):
    # CHECK PLAYER TURN STATE:
    if player1.turn:
        win = get_move(player1, player2, display)
    else:
        win = get_move(player2, player1, display)
    # CHECK WIN CONDITION AFTER EACH TURN:
    if win:
        break

# DISPLAY UPON DRAW CONDITION:
if not win:
    print(draw)
    print("Tough going! It's art draw!")
