class Floor:
    def __init__(self):
        self.name = 'floor'

    def build(self):
        print(f'Build {self.name}')


class Ceiling:
    def __init__(self):
        self.name = 'ceiling'

    def build(self):
        print(f'Build {self.name}')


class Wall:
    def __init__(self):
        self.name = 'wall'

    def build(self):
        print(f'Build {self.name}')


class Building:
    def __init__(self):
        self.floor = None
        self.ceiling = None
        self.wall = None

    def inject_floor(self, floor):
        self.floor = floor

    def inject_ceiling(self, ceiling):
        self.ceiling = ceiling

    def inject_wall(self, wall):
        self.wall = wall


def build():  # Fabric
    house = Building()
    house.inject_floor(Floor())
    house.inject_ceiling(Ceiling())
    house.inject_wall(Wall())
    return house


house = build()

house.floor.build()
house.ceiling.build()
house.wall.build()
