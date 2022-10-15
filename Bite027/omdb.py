import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_data = []
    for file in files:
        with open(file) as f:
            movie_data.append(json.load(f))
    return movie_data


def get_single_comedy(movies: list) -> str:
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies: list) -> str:
    movies_dict = {}
    for movie in movies:
        awards = movie["Awards"]
        movies_dict[movie["Title"]] = int(
            awards[awards.find("&") + 2 : awards.rfind(" nominations.")]
        )
    return max(movies_dict, key=movies_dict.get)


def get_movie_longest_runtime(movies: list) -> str:
    movies_dict = {}
    for movie in movies:
        movies_dict[movie["Title"]] = int(
            "".join(c for c in movie["Runtime"] if c.isdigit())
        )
    return max(movies_dict, key=movies_dict.get)
