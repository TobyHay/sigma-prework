# Given a list of integers, return the highest and lowest numbers in the array (without using max() or min() )

def maxmin(integers):
    sorted_list = sorted(integers)
    return [sorted_list[0], sorted_list[-1]]


integers = [20, 50, 12, 6, 14, 8]
print(maxmin(integers))
