from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import pandas as pd

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    movie_df = pd.read_csv(MOVIE_DATA)
    movie_df = movie_df[movie_df["title_year"] >= MIN_YEAR]

    directors = defaultdict(list)
    for index, row in movie_df.iterrows():
        directors[row["director_name"]].append(
            Movie(row["movie_title"], row["title_year"], row["imdb_score"])
        )

    directors = defaultdict(
        list, {k: v for k, v in directors.items() if len(v) >= MIN_MOVIES}
    )

    return directors


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""

    return round(sum([movie.score for movie in movies]) / len(movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""

    director_scores = []
    for director, movies in directors.items():
        director_scores.append((director, calc_mean_score(movies)))
    director_scores.sort(key=lambda x: x[1], reverse=True)
    return director_scores
