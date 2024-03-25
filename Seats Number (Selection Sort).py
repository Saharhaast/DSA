"""Seats Number"""
from json import loads
def selection_sort_seat(lis, last):
    """selection"""
    compare = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            compare += 1
            if lis[walker][0] < lis[smallest][0] or (lis[walker][0] == lis[smallest][0]\
                and int(lis[walker][1:]) < int(lis[smallest][1:])):
                smallest = walker
            walker += 1
        lis[current], lis[smallest] = lis[smallest], lis[current]
        current += 1
        print(lis)
    print("Comparison times:", compare)
selection_sort_seat(loads(str(input())), int(input()))
