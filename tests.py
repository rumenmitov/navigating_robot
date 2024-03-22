import math
import vector_utils as utils


def test_normalize():
    assert utils.normalize({"x": 1.0, "y": 0.0}) == 1.0
    assert utils.normalize({"x": 0.0, "y": 1.0}) == 1.0


def test_rotate():
    assert utils.rotate({"x": 1.0, "y": 0.0}, math.pi / 2) == {"x": 0.0, "y": 1.0}
    assert utils.rotate({"x": 0.0, "y": 2.0}, math.pi / 2) == {"x": -2.0, "y": 0.0}
