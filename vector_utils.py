import math


def normalize(position):
    return math.sqrt(position["x"]**2 + position["y"]**2)


def rotate(position, angle):
    return {
        "x": round(math.cos(angle) * position["x"]
                   - math.sin(angle) * position["y"], 3),
        "y": round(math.sin(angle) * position["x"]
                   + math.cos(angle) * position["y"], 3)
    }
