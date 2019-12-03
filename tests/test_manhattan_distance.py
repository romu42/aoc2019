import pytest
from day3.manhattan_distance import closest_intersect


@pytest.mark.parametrize(
    "moves, distance",
    [
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\n\
    U62,R66,U55,R34,D71,R55,D58,R83",
            159,
        ),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n\
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    ],
)
def test_closest_intersect(moves, distance):
    assert closest_intersect(moves) == distance
