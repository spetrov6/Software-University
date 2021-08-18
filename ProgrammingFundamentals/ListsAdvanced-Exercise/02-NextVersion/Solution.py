current_version = [int(i) for i in input().split(".")]
for i in range(len(current_version) - 1,-1,-1):
    if current_version[i] + 1 <= 9:
        current_version[i] += 1
        break
    else:
        current_version[i] = 0
print(*current_version,sep=".")
