# PLAYER CLASS TO BE IMPORTED INTO MAIN.PY

class Player:

    def __init__(self):
        self.move_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.moves = []
        self.symbol = ''
        self.winning_sequence = ''
        self.bot = False
        self.turn = False
        self.name = ''