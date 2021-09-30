def flights(*args):
    destinations = {}

    for destination in range(0, len(args), 2):
        if args[destination] == "Finish":
            break

        if args[destination] not in destinations:
            destinations[args[destination]] = 0

        destinations[args[destination]] += int(args[destination + 1])

    return destinations