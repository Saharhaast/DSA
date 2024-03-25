"""bubble"""
from json import loads
def bubble_sort(lis, last):
    """bubble"""
    compare = 0
    current = 0
    is_sorted = False
    while current <= last and is_sorted is False:
        walker = last
        is_sorted = True
        while walker > current:
            compare += 1
            if lis[walker] < lis[walker - 1]:
                is_sorted = False
                lis[walker], lis[walker - 1] = lis[walker - 1], lis[walker]
            walker -= 1
        current += 1
        print(lis)
    print("Comparison times:", compare)
bubble_sort(loads(str(input())), int(input()))
