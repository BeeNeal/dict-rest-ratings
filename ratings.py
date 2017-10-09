"""Restaurant rating lister."""

import random


def get_restaurant_ratings(filename):
    """opens text file and prints the restaurants and ratings sorted
    Returns nothing"""

    ratings = {}
    with open(filename) as text_file:
        for line in text_file:
            name, score = line.rstrip().split(':')
            ratings[name] = score
    return ratings


def print_sorted_ratings(ratings):
    """prints the restaurants and ratings sorted and returns nothing"""

    for restaurant, rating in sorted(ratings.items()):
        print "{name} is rated at {score}.".format(
            name=restaurant, score=rating)


def prompt_user_for_rating(orig_ratings):
    """adding user name and score to existing ratings"""

    new_ratings = orig_ratings
    user_rest = raw_input("Please enter a restaurant name: \n")
    user_rest = user_rest.title()
    while True:
        user_score = raw_input("Please enter that restaurant's score (1-5): \n")
        try:
            user_score = int(user_score)
        except ValueError:
            print "Try again - you did not enter a number from 1 - 5."
            continue
        if user_score not in range(1, 6):
            print "Try again - you did not enter a number from 1 - 5."
            continue
        break

    new_ratings[user_rest] = user_score
    return new_ratings


def setup_interaction():
    """set up the initial interaction, doesn't take in any parameters
    Runs functions based on user input"""
    current_ratings = get_restaurant_ratings("scores.txt")
    while True:
        print "You can get restaurant ratings, add a restaurant, update random restaurant, or quit."
        user_choice = raw_input("Enter P to print, A to add, R to update random restaurant or Q to quit:\n")
        if user_choice.lower().startswith('p'):
            print_sorted_ratings(current_ratings)
        elif user_choice.lower().startswith('a'):
            current_ratings = prompt_user_for_rating(current_ratings)
        elif user_choice.lower().startswith('r'):
            current_ratings = random_update(current_ratings)
        else:
            break


def random_update(ratings):
    """Asks the user to update the rating of a random restaurant"""

    names = ratings.keys()
    random_rest = random.choice(names)

    print "{name} is currently rated {rated}.".format(
        name=random_rest, rated=ratings[random_rest])
    new_rating = raw_input("Please enter new rating: \n")
    ratings[random_rest] = new_rating

    print "{name} is now rated {rated}.".format(
        name=random_rest, rated=ratings[random_rest])

    return ratings


def choice_update(ratings):
    """in progress"""
    pass

setup_interaction()
