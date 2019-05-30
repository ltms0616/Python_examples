Numbers=[21,56,32,49,87,16,98,5,77]

def merge_sort(array):
    if len(array) > 1:
        mid=len(array)//2
        left_array=array[:mid]
        right_array=array[mid:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_idx = 0
        right_idx = 0
        merge_idx = 0

        while left_idx < len(left_array) and right_idx < len(right_array):
            if left_array[left_idx] < right_array[right_idx]:
                array[merge_idx] = left_array[left_idx]
                left_idx += 1
            else:
                array[merge_idx] = right_array[right_idx]
                right_idx += 1
            merge_idx += 1

        while left_idx < len(left_array):
            array[merge_idx] = left_array[left_idx]
            left_idx += 1
            merge_idx += 1

        while right_idx < len(right_array):
            array[merge_idx] = right_array[right_idx]
            right_idx += 1
            merge_idx += 1

merge_sort(Numbers)
print(Numbers)

