"""selection"""
from json import loads
def selection_sort(lis, last):
    """selection"""
    compare = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            compare += 1
            if lis[walker] < lis[smallest]:
                smallest = walker
            walker += 1
        lis[current], lis[smallest] = lis[smallest], lis[current]
        current += 1
        print(lis)
    print("Comparison times:", compare)
selection_sort(loads(str(input())), int(input()))
