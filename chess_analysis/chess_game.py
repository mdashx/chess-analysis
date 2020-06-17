import io
from subprocess import Popen, PIPE


import chess.pgn


class ChessGame:
    def __init__(self, pgn):
        self.pgn = io.StringIO(pgn)
        self.fen = []
        self.evaluations = []
        self.engine = None

    def get_fen(self):
        "Walk through the game and save a FEN string for each position"
        game = chess.pgn.read_game(self.pgn)
        board = game.board()
        for move in game.mainline_moves():
            self.fen.append(board.fen())
            board.push(move)

    @staticmethod
    def get_eval_from_string(info):
        info = info.split("score")
        info = info[1].strip().split()
        return " ".join([info[0], info[1]])

    def get_eval(self, fen):
        engine = Popen("stockfish", stdout=PIPE, stdin=PIPE, universal_newlines=True)
        engine.stdin.write("uci\n")
        engine.stdin.write(f"position fen {fen}\n")
        engine.stdin.write("go depth 5\n")
        engine.stdin.flush()
        while True:
            text = engine.stdout.readline().strip()
            if "info depth 5" in text:
                self.evaluations.append((fen, self.get_eval_from_string(text)))
                return

    def eval_all(self):
        for fen in self.fen:
            self.get_eval(fen)
