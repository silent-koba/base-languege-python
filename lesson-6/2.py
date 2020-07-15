class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self):
        print(f'Масса асфальта: {int(self._length * self._width * 25 * 0.005)} т')


r = Road(20, 5000)
r.asphalt_weight()