def even_odd(*args):
    args = list(args)
    type_of_nums = args.pop()
    if type_of_nums == "odd":
        return [int(x) for x in args if x % 2 != 0]
    else:
        return [int(x) for x in args if x % 2 == 0]