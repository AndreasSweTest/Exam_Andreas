import random

from .grid import Grid   # om du behöver typ-hint eller isinstance

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


# Alla frukter värda 20 poäng nu
pickups = [
    Item("carrot",      20, "c"),
    Item("apple",       20, "a"),
    Item("strawberry",  20, "s"),
    Item("cherry",      20, "h"),
    Item("watermelon",  20, "w"),
    Item("radish",      20, "r"),
    Item("cucumber",    20, "u"),
    Item("meatball",    20, "m"),   # fortfarande med? :)
]


def randomize(grid: Grid):
    """Placerar ut alla items på slumpmässiga tomma positioner"""
    for item in pickups:
        while True:
            x = random.randint(1, grid.width - 2)   # undvik väggar
            y = random.randint(1, grid.height - 2)
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break