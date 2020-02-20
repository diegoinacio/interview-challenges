
# ! Problem

# {1, 2, 3} -> 2 is the median.
# {1, 2, 3, 4} -> (2 + 3)/2 = 2.5 is the median.

# ? Function Description

# * Given an input stream of  integers, you must ..
# * perform the following task for each i_th integer:
# 1 - Add the i_th integer to a running list of integers.
# 2 - Find the median of the updated list (i.e., for the ..
#     first element through the i_th element).
# 3 - Print the list's updated median on a new line. The ..
#     printed value must be a double-precision number ..
#     scaled to 1 decimal place (i.e., 12.3 format).

# * {16, 8, 2, 4, 32} -> {16.0, 12.0, 8.0, 6.0, 8.0}


from typing import List


def runningMedian(input_list: List[int]) -> List[str]:
    result = []
    N = len(input_list)
    for i in range(N):
        medianValue = 0
        currentList = sorted(input_list[:i + 1])
        n = len(currentList)
        if n % 2:
            medianValue = currentList[n//2]
        else:
            medianValue = (currentList[n//2] + currentList[n//2 - 1])/2
        result += [f'{medianValue:.1f}']
    return result
