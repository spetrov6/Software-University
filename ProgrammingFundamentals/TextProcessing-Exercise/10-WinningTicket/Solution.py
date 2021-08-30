def is_consistent(half,symbol):
    """
    Check if wining symbol is consistent a.k.a Cash$$$$$$ and is not a non-consistent @@s@s@s@s@
    :param half:Which half to check for consistency
    :param symbol:What is winning symbol
    :return:True or False
    """
    count = 0
    for char in half:
        if char == symbol:
            count += 1
            if count == 6:
                return True
        else:
            count = 0
    return False
tickets = [i.strip() for i in input().split(", ")]
symbols = ["@", "#", "$", "^"]
for ticket in tickets:
    first_half = ticket[:len(ticket) // 2]
    second_half = ticket[len(ticket) // 2:]
    symbols_first_half = next((x for x in first_half if x in symbols and first_half.count(x) >= 6), "none")
    symbols_second_half = next((x for x in second_half if x in symbols and second_half.count(x) >= 6), "none")
    if len(ticket) != 20:
        print("invalid ticket")
    elif len(set(ticket)) == 1 and first_half[0] in symbols:
        print(f'ticket "{ticket}" - 10{first_half[0]} Jackpot!')
    elif first_half.count(symbols_first_half) >= 6 and second_half.count(symbols_second_half) >= 6:
        if is_consistent(first_half,symbols_first_half) and is_consistent(second_half,symbols_second_half) and symbols_first_half == symbols_second_half:
            if first_half.count(symbols_first_half) < second_half.count(symbols_second_half):
                print(f'ticket "{ticket}" - {first_half.count(symbols_first_half)}{symbols_first_half}')
            else:
                print(f'ticket "{ticket}" - {second_half.count(symbols_second_half)}{symbols_second_half}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print(f'ticket "{ticket}" - no match')