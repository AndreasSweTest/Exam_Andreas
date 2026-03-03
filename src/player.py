from operator import truediv


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, dx, dy, grid):
        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        # Inom kartan?
        if not (0 <= new_x < grid.width and 0 <= new_y < grid.height):
            return False

        # Inte vägg?
        if grid.get(new_x, new_y) == grid.wall:
            return False

        # Annars OK (tom eller frukt tillåts)
        return True


