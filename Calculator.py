"""66070313"""
def calculator(num):
    """calculator"""
    res = 0
    if num == 1:
        print(1)
    else:
        for amount in range(1, num+1):
            res += len(str(amount))
        print(res + num)
calculator(int(input()))
