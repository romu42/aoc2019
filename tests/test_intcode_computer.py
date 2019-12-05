import pytest
from day5.intcode_computer import computer


@pytest.mark.parametrize(
    "initial_state, final_state",
    [
        ([1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]),
        ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
        ([3, 0, 4, 0, 99], [1, 0, 4, 0, 99]),
    ],
)
def test_fix_computer(initial_state, final_state):
    assert computer(initial_state) == final_state