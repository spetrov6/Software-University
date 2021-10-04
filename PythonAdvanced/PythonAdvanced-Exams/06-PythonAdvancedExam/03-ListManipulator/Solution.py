def list_manipulator(list_of_numbers, *args):
    action, side = args[0], args[1]

    if action == "remove":
        if side == "end":
            if len(args) > 2:
                for _ in range(args[2]):
                    list_of_numbers.pop()
            else:
                list_of_numbers.pop()

        else:
            if len(args) > 2:
                for _ in range(args[2]):
                    list_of_numbers.pop(0)
            else:
                list_of_numbers.pop(0)

    elif action == "add":
        if side == "end":
            for index in range(2, len(args)):
                list_of_numbers.append(args[index])

        else:
            counter = 0
            for index in range(2, len(args)):
                list_of_numbers.insert(counter, args[index])
                counter += 1
    return list_of_numbers