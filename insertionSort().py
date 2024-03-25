"""insertion"""
from json import loads
def insertion_sort(lis, last):
    """insertion"""
    compare = 0
    current = 1
    while current <= last:
        walker = current - 1
        while walker >= 0:
            compare += 1
            if lis[walker + 1] < lis[walker]:
                lis[walker + 1], lis[walker] = lis[walker], lis[walker + 1]
                walker -= 1
            else:
                break
        current += 1
        print(lis)
    print("Comparison times:", compare)
insertion_sort(loads(str(input())), int(input()))
