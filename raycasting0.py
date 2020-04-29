import numpy as np


class Sensor:
    def __init__(self, xSize: int, ySize: int, ppi: float, pos, rot):
        self.xSize = int(xSize)
        self.ysize = int(ySize)
        self.ppi = ppi
        self.pos = pos
        self.rot = rot
        self.data = np.zeros((xSize, ySize))
        for _ in np.nditer(self.data):
            _ = (0, 0, 0)


class Lens:
    def __init__(self, pos, rot):
        self.pos = pos
        self.rot = rot
        self.surfaces = []

    def addSurface(self, surface):
        self.surfaces.append(surface)


class Surface:
    def __init__(self, radius: float, thickness: float, IOR: float, depth: float):
        self.radius = radius
        self.thickness = thickness
        self.IOR = IOR
        self.depth = depth


class Scene:
    def __init__(self, sensor: Sensor, lenses: list, objects: list):
        self.sensor = sensor
        self.lenses = lenses
        self.objects = objects



s0 = Sensor(640, 480, 600, (0, 0, 0), (0, 0, 0))

l1 = Lens((10, 0, 0), (0, 0, 0))
l1s1 = Surface(10, 5, 1.50, 0)
l1.addSurface(l1s1)
l1s2 = Surface(10, None, 1, None)
l1.addSurface(l1s2)

scene = Scene(s0, [l1], [])
