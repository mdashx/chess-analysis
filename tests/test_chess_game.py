import random
import os

import pytest

from chess_analysis.chess_game import ChessGame

E4 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
E5 = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"
NF3 = "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
NF6 = "rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"

INFO = "info depth 5 seldepth 5 multipv 1 score cp 49 nodes 782 nps 97750 tbhits 0 time 8 pv g1f3 b8c6 d2d4 d7d5 e2e3"

TEST_LIVE = os.getenv("TEST_LIVE", False)


def test_init():
    pgn = "1. e4 e5 2. Nf3 Nf6"
    chess_game = ChessGame(pgn)
    assert isinstance(chess_game, ChessGame)


def test_get_fen():
    pgn = "1. e4 e5 2. Nf3 Nf6"
    chess_game = ChessGame(pgn)
    expected = E4
    chess_game.get_fen()
    assert isinstance(chess_game.fen, list)
    assert len(chess_game.fen) == 4
    assert isinstance(chess_game.fen[0], str)
    assert chess_game.fen[0] == expected


def test_get_eval_from_string():
    chess_game = ChessGame("")
    expected = "cp 49"
    score = chess_game.get_eval_from_string(INFO)
    assert score == expected


@pytest.mark.skipif(TEST_LIVE is not True, reason="Skipping expensive tests")
def test_get_eval():
    chess_game = ChessGame("")
    chess_game.fen = [E4, E5, NF3, NF6]
    chess_game.get_eval(E4)
    assert len(chess_game.evaluations) == 1
    assert isinstance(chess_game.evaluations, list)
    assert isinstance(chess_game.evaluations[0], tuple)
    assert isinstance(chess_game.evaluations[0][1], str)


def test_eval_all(monkeypatch):
    def random_score(instance, fen):
        score = f"cp {random.randrange(-100, 100, 1) / 100.0}"
        instance.evaluations.append((fen, score))

    monkeypatch.setattr(ChessGame, "get_eval", random_score)
    chess_game = ChessGame("")
    chess_game.fen = [E4, E5, NF3, NF6]
    chess_game.eval_all()
    assert len(chess_game.evaluations) == 4
    assert isinstance(chess_game.evaluations, list)
    assert isinstance(chess_game.evaluations[3], tuple)
    assert isinstance(chess_game.evaluations[3][1], str)


@pytest.mark.xfail
def test_create_diagram():
    """Not implemented yet!"""
    chess_game = ChessGame("")
    diagram = chess_game.create_diagram(E4)
    # diagram should be an XML string (SVG)
    assert isinstance(diagram, str)
