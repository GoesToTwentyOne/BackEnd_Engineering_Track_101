def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    result = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])

    return result

# Example usage
input_array = [12, 4, 5, 6, 7, 3, 1, 8]

# Sorting the array using merge sort
sorted_array = merge_sort(input_array)
print(sorted_array)
