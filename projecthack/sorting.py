def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    lengthOfArray = len(items) - 1

    # number of rounds will be the total length - 1, for array with length 5, we will do 4 rounds: 0 and 1, 1 and 2, 2 and 3, 3 and 4.
    for i in range(lengthOfArray):

        # at each round, we compare the current j with the next value

        for j in range(lengthOfArray - i):

            # only swap their positions if left value < right value as we aim to move all the small values to the back

            if items[j] < items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items[::-1]

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:

        return items
# Find the middle point and devide it
    middle = len(items) // 2
    left_list = items[:middle]
    right_list = items[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
