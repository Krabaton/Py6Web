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
    def __init__(self, floor: Floor, ceiling: Ceiling, wall: Wall):
        self.floor = floor
        self.ceiling = ceiling
        self.wall = wall


house = Building(Floor(), Ceiling(), Wall())

house.floor.build()
house.ceiling.build()
house.wall.build()
