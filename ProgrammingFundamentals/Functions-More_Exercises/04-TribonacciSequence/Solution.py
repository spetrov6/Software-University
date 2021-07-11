def tribonacci(num):
    result = []
    last_three = [1,0,0]
    while len(result) < num:
        result.append(sum(last_three))
        last_three.append(sum(last_three))
        last_three.pop(0)
    print(*result,sep=" ")
tribonacci(int(input()))