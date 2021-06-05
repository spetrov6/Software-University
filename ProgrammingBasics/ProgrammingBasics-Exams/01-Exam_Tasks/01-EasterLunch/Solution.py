bread = int(input())
eggs = int(input())
cookie = int(input())
eggs_total = eggs * 12
paint_price = eggs_total * 0.15
eggs_price = eggs * 4.35
cookies_price = cookie * 5.40
bread_price = bread * 3.20
total_price = paint_price + cookies_price + bread_price + eggs_price
print(f"{total_price:.2f}")
