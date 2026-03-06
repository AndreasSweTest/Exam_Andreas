from .grid import Grid
from .player import Player
from . import pickups

player = Player(18, 6)   # ungefär mitten
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.add_random_walls()
pickups.randomize(g)


def print_status(game_grid):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)


command = ""
while command not in ["q", "x"]:
    print_status(g)

    command = input("Use WASD to move, I for inventory, Q/X to quit: ").strip().lower()

    if len(command) == 0:
        continue

    command = command[0]   # tar bara första tecknet

    moves = {
        'w': (0, -1),
        'a': (-1, 0),
        's': (0, 1),
        'd': (1, 0)
    }

    if command in moves:
        dx, dy = moves[command]

        new_x = player.pos_x + dx
        new_y = player.pos_y + dy

        if player.can_move(dx, dy, g):
            maybe_item = g.get(new_x, new_y)
            player.move(dx, dy)

            score -= 1   # the floor is lava

            if isinstance(maybe_item, pickups.Item):
                score += maybe_item.value
                print(f"You found a {maybe_item.name}! +{maybe_item.value} points.")
                inventory.append(maybe_item)
                g.clear(new_x, new_y)   # tömmer rutan där frukten låg

        else:
            print("Not allowed to walk through walls!")

    elif command == 'i':
        if not inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in inventory:
                print(f"  - {item.name} ({item.value} points)")

    elif command in ["q", "x"]:
        break

    else:
        print("Unknown command. Use w/a/s/d, i, q or x.")

print("\nThank you for playing!")