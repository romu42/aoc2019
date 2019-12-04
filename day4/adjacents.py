
from collections import deque

# def check_adjacent(password: str) -> bool:
#     for i in range(len(password)-1):
#         if password[i] == password[i + 1] and password[i + 1]:
#             return True
#     return False

# adjacent = []
# for i in range(len(password) - 1):
#     if password[i] == password[i + 1]:
#         adjacent.append([password[i]])
# return adjacent


def check_adjacent_limited(password: str) -> bool:
    d = deque(password)
    for item in set(password):
        if d.count(item) == 2:
            return True
    return False








if __name__ == '__main__':
    print(check_adjacent_limited('112233'))
    print(check_adjacent_limited('123444'))
    print(check_adjacent_limited('111122'))
