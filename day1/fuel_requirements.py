# https://adventofcode.com/2019/day/1

def mass_to_fuel_ratio(mass: int)-> int:
    return int(mass / 3) - 2

def sum_fuel(fuel: int)-> int:
    if fuel < 6:
        return fuel
    else:
        return sum_fuel(int(fuel / 3) - 2) + fuel

def sum_fuel_requirements(data: str)-> int:
    total = 0
    for mass in data:
        total += mass_to_fuel_ratio(int(mass))
    return total

def sum_fuel_total_requirements(data: str)-> int:
    total = 0
    for mass in data:
        sub_total = 0
        sub_total += mass_to_fuel_ratio(int(mass))
        if sub_total <= 2:
            total += sub_total
            next
        else:
            total += sum_fuel(sub_total)
    return total




if __name__ == '__main__':
    with open("puzzle_input") as data:
        print(sum_fuel_total_requirements(data))
        print(sum_fuel_requirements(data))




