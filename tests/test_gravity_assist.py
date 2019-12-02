import pytest
from day2.gravity_assist import fix_computer


@pytest.mark.parametrize("initial_state, final_state",[
    ([1,0,0,0,99], [2,0,0,0,99]),
    ([2,3,0,3,99], [2,3,0,6,99]),
    ([2,4,4,5,99,0], [2,4,4,5,99,9801]),
    ([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]),

])
def test_fix_computer(initial_state, final_state):
    assert fix_computer(initial_state) == final_state