"""Swap"""
def Swap_Var(text_in):
    """Variable"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))
def swap_tuple_values(data_tuple):
    xxx, yyy = data_tuple
    return (yyy, xxx)
laongdao_data = Swap_Var(input())
swapped_data = swap_tuple_values(laongdao_data)
print(swapped_data)
