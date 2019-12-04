from collections import deque


def get_password_count(input: str) -> int:
    count = 0
    start, stop = input.split('-')
    print(start, stop)
    for password in range(int(start), int(stop)):
        if check_increase(str(password)) and check_adjacent(str(password)):
            count += 1
    return count


def get_password_count_limited(input: str) -> int:
    count = 0
    start, stop = input.split('-')
    print(start, stop)
    for password in range(int(start), int(stop)):
        if check_increase(str(password)) and check_adjacent_limited(str(password)):
            count += 1
    return count


def check_length(password: str) -> bool:
    if len(str(password)) == 6:
        return True
    else:
        return False



def check_adjacent(password: str) -> bool:
    for i in range(len(password)-1):
        if password[i] == password[i + 1] and password[i + 1]:
            return True
    return False


def check_adjacent_limited(password: str) -> bool:
        d = deque(password)
        for item in set(password):
            if d.count(item) == 2:
                return True
        return False


def check_increase(password: str) -> bool:
    if ''.join(sorted(password)) == password:
        return True
    else:
        return False



if __name__ == '__main__':
    print(get_password_count('172851-675869'))
    print(get_password_count_limited('172851-675869'))
