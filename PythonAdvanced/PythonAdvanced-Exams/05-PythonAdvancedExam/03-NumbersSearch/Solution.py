def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)
    missing_number = None
    duplicates = []
    for num in range(min_number, max_number + 1):
        if num not in args:
            missing_number = num
        if args.count(num) > 1:
            duplicates.append(num)
    return [missing_number, duplicates]