# AI code in case of player vs. ai selection.

import random

# CHECK PER AI TURN FOR WIN CONDITION:
def can_i_win(sequence, bot):
    move = 0
    for line in sequence:
        if line.count(bot.symbol) == 2:
            potential_move = line.strip(bot.symbol)
            try:
                int(potential_move)
            except ValueError:
                pass
            else:
                return int(potential_move)
    return move


# RANDOM MOVE SELECTION FOR AI:
def attack(status, bot):
    # IF MIDDLE SQUARE IS UNTAKEN, SELECT IT:
    if status[4] == 5:
        move = 5
        return move
    else:
        # IF CORNER SQUARE IS UNTAKEN, RANDOMLY SELECT ONE THAT IS UNUSED:
        for i in random.sample([1, 3, 7, 9], 4):
            if i in bot.move_options:
                return i
        # RANDOM CHOICE IF MIDDLE/CORNER SQUARES ARE USED:
        return random.choice(bot.move_options)



def bot_turn(status, sequence, player, bot):
    move = can_i_win(sequence, bot)
    # CHOOSE UNUSED SQUARE IF IT SATISFIES THE WIN CONDITION:
    if move > 0:
        return move
    for line in sequence:
        if line.count(player.symbol) == 2:
            potential_move = line.strip(player.symbol)
            try:
                int(potential_move)
            except ValueError:
                pass
            else:
                return int(potential_move)
    return attack(status, bot)