import os

import pytest

from chess_analysis import download_pgn

from data.pgn_text import LASKER_GAME

TEST_LIVE = os.getenv("TEST_LIVE", False)


def test_get_download_url():
    # Normal behavior
    game_id = "112358"
    filename = "johnson_lasker_1926.pgn"
    expected = "https://www.chessgames.com/pgn/johnson_lasker_1926.pgn?gid=112358"
    url = download_pgn.get_download_url(game_id, filename)
    assert isinstance(url, str)
    assert url == expected

    # Filename not specified
    game_id = "112358"
    expected = "https://www.chessgames.com/pgn/game.pgn?gid=112358"
    url = download_pgn.get_download_url(game_id)
    assert isinstance(url, str)
    assert url == expected


@pytest.mark.skipif(TEST_LIVE is not True, reason="Skipping expensive tests")
def test_download():
    url = "https://www.chessgames.com/pgn/game.pgn?gid=1380448"
    expected = LASKER_GAME
    pgn = download_pgn.download(url)
    assert isinstance(pgn, str)
    assert [l.strip() for l in pgn.split("\n")] == expected
