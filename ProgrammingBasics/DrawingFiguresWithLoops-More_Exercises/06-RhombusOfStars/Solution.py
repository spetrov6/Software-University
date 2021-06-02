n = int(input())
for up in range(1,n + 1):
    print(" " * (n - up) + "* " * up)
for down in range(n -1 , 0, - 1):
    print(" " * (n - down) + "* " * down)