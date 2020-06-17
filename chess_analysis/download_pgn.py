"""Download a PGN from ChessGames.com and save it as a string. Use an imperative programming style so we can demonstrate using pytest to test imperative code."""

import requests


def get_download_url(game_id, filename="game.pgn"):
    """If this function seems contrived, that's because it is contrived to
    provide pytest examples."""

    return f"https://www.chessgames.com/pgn/{filename}?gid={game_id}"


def download(url):
    response = requests.get(url)
    return response.content.decode("utf-8")
