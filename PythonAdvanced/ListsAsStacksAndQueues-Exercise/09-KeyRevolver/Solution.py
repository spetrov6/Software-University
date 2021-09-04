from collections import deque
bullet_price = int(input())
barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
price = int(input())
bullets_shooted = 0
counter = 0
#during the shooting is used last bullet and first lock is shooted
while True:
    if bullets[-1] <= locks[0]:
        print("Bang!")
        bullets.pop()
        locks.popleft()
    else:
        print("Ping!")
        bullets.pop()
    bullets_shooted += 1
    counter += 1
    if counter == barrel_size and len(bullets) > 0:
        counter = 0
        print("Reloading!")
    if len(bullets) <= 0 < len(locks):
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    if len(locks) <= 0:
        print(f"{len(bullets)} bullets left. Earned ${price - (bullet_price * bullets_shooted)}")
        break