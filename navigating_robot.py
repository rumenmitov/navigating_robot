import serial
import math
import matplotlib.pyplot as plt
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

position = {
    "x": 0.0,
    "y": 0.0
}

path_x = [position["x"]]
path_y = [position["y"]]


def normalize(position):
    return math.sqrt(position["x"]**2 + position["y"]**2)


def rotate(position, angle):
    return {
        "x": round(math.cos(angle) * position["x"]
                   - math.sin(angle) * position["y"], 3),
        "y": round(math.sin(angle) * position["x"]
                   + math.cos(angle) * position["y"], 3)
    }


def test_normalize():
    assert normalize({"x": 1.0, "y": 0.0}) == 1.0
    assert normalize({"x": 0.0, "y": 1.0}) == 1.0


def test_rotate():
    assert rotate({"x": 1.0, "y": 0.0}, math.pi / 2) == {"x": 0.0, "y": 1.0}
    assert rotate({"x": 0.0, "y": 2.0}, math.pi / 2) == {"x": -2.0, "y": 0.0}


if __name__ == "__main__":
    test_normalize()
    test_rotate()

    while True:
        data = ser.readline().decode('utf-8').strip()

        if (data == 1):
            position = rotate(position, math.pi / 6)

        magnitude = normalize(position)
        position["x"] += position["x"] / magnitude
        position["y"] += position["y"] / magnitude

        path_x.append(position["x"])
        path_y.append(position["y"])

        plt.plot(path_x, path_y)

        time.sleep(1)
