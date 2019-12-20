


if __name__ == "__main__":
    with open("test_input") as file:
        # data = file.read()
        new_list = []
        data = file.read().split("\n")
        print(data)
        new_list = [item.split(")") for item in data]
        print(new_list.sort())
        distance = 0
