# https://adventofcode.com/2019/day/1

import pytest
from day1.fuel_requirements import (
    mass_to_fuel_ratio,
    sum_fuel_requirements,
    sum_fuel_total_requirements,
)


@pytest.mark.parametrize(
    "mass, expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_mass_to_fuel_ratio(mass, expected):
    assert mass_to_fuel_ratio(mass) == expected


def test_sum_fuel_requirement():
    data = ["12", "14", "1969", "100756"]
    assert sum_fuel_requirements(data) == 34241


def test_sum_fuel_total_requiremnt():
    data = ["12", "14", "1969", "100756"]
    assert sum_fuel_total_requirements(data) == 51316
