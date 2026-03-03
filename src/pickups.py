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


# Alla frukter värda 20 poäng
pickups = [
    Item("Banana",      20, "B"),
    Item("Apple",       20, "A"),
    Item("Strawberry",  20, "S"),
    Item("Cherry",      20, "C"),
    Item("Watermelon",  20, "W"),
    Item("Orange",      20, "O"),
]


def randomize(grid: Grid):
    """Placerar ut alla items på slumpmässiga tomma positioner"""
    for item in pickups:
        while True:
            x = random.randint(1, grid.width - 2)
            y = random.randint(1, grid.height - 2)
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break


