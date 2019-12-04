import pytest
from day4.get_password import check_adjacent, check_increase, check_length, check_range


@pytest.mark.parametrize("password, expected", [(12, False), (112234, True)])
def test_check_length(password, expected):
    assert check_length(str(password)) == expected


@pytest.mark.parametrize(
    "password, expected", [(12, False), (11, True), (1969, False), (100756, True)]
)
def test_check_adjacent(password, expected):
    assert check_adjacent(str(password)) == expected


@pytest.mark.parametrize(
    "password, expected", [(12, False), (11, True), (1969, False), (100789, True)]
)
def test_check_increase(password, expected):
    check_increase(str(password)) == expected
