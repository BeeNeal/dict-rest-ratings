"""Restaurant rating lister."""


def get_restaurant_ratings(filename):
    """opens text file and prints the Restaurants (key)
    and ratings (value) sorted and return nothing"""
    ratings = {}
    with open(filename) as text_file:
        for line in text_file:
            rest_data = line.rstrip().split(':')
            ratings[rest_data[0]] = rest_data[1]
    for restaurant, rating in sorted(ratings.items()):
        print "{name} is rated at {score}.".format(
            name=restaurant, score=rating)


get_restaurant_ratings("scores.txt")
