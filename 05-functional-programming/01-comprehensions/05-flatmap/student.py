from util import Card


def genres(movies):
    return {genre for movie in movies for genre in movie.genres}


def actors(movies):
    return {actors for movie in movies for actors in movie.actors}


def repeat_consecutive(xs, n):
    return [s for s in xs for _ in range(n)]


def repeat_alternating(xs, n):
    return [s for _ in range(n) for s in xs]


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}
