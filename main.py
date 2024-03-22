import serial
import math
import matplotlib.pyplot as plt
from playsound import playsound
import tests
import vector_utils as utils

ser = serial.Serial('/dev/ttyACM0', 9600)

position = {
    "x": 1.0,
    "y": 1.0
}

path = {
    "x": [position["x"]],
    "y": [position["y"]]
}


if __name__ == "__main__":
    tests.test_normalize()
    tests.test_rotate()

    while True:
        # INFO: Get data from sensor
        data = int(ser.readline().decode('utf-8').strip())

        # INFO: Calculate direction vector of robot
        direction_vector = position

        if len(path["x"]) > 2 and len(path["y"]) > 2:
            direction_vector = {
                    "x": position["x"] - path["x"][-2],
                    "y": position["y"] - path["y"][-2],
            }

        # INFO: Get normalized vector of current direction
        magnitude = utils.normalize(direction_vector)

        if magnitude == 0:
            magnitude = 1.0

        normalized_direction = {
                "x": direction_vector["x"] / magnitude,
                "y": direction_vector["y"] / magnitude
        }

        # INFO: If data is 1, robot is turning to the right, hence rotate
        #       normalized direction vector by -30 degrees and play sound
        if (data == 1):
            normalized_direction = utils.rotate(normalized_direction, -math.pi / 6)
            playsound("./assets/wow.mp3", False)

        # INFO: Update current position and robot path
        position["x"] += normalized_direction["x"]
        position["y"] += normalized_direction["y"]

        path["x"].append(position["x"])
        path["y"].append(position["y"])

        # INFO: Plot path
        plt.plot(path["x"], path["y"], color='red')
        plt.draw()
        plt.pause(0.01)
