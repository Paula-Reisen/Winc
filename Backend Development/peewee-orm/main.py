from turtle import left
import models
import peewee
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    models.Dish.select().order_by(models.Dish.price_in_cents.desc())
    return models.Dish.name


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    listVegetarianDishes = []
    for dish in models.Dish.select():
        if all(models.Ingredient.is_vegetarian == 1):
            listVegetarianDishes.append(dish)
    return [listVegetarianDishes]


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    models.Rating.select().order_by(models.Rating.rating.asc())
    return models.Rating.restaurant



def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    restaurant_name = models.Restaurant.select(models.Restaurant.name).limit(1)
    models.Rating.select().where(models.Rating.restaurant == restaurant_name)
    models.Rating.rating == 24
    
def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    models.Restaurant.select().where(models.Restaurant.opening_time == '19:00')

    for dish in models.Dish.select(models.Dish.served_at).join(models.Restaurant.name, join_type=left):
        if models.Ingredient.is_vegan == 1:
           models.Dish.select(models.Dish.served_at).where(models.Dish.name == dish)
           restaurant = models.Restaurant.name
        return restaurant

def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    ...
    models.Dish.name == 'FishAndChips'
    ingredients = ['Cheese', 'Fish', 'Patatoes']
    
    for ingredient in ingredients:
        if not all(models.Ingredient.name == ingredient):
            models.Ingredient.name == ingredient

        return models.Dish.name


