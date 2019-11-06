# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i_A, i_B = 0, 0
    # Current index of merged_arr is the sum of the indicies
    # of arrA & arrB
    while (i := i_A + i_B) < elements:
        try:
            a = arrA[i_A]
        # If we've reached the end of arrA, fill w/ arrB
        except:
            merged_arr[i:] = arrB[i_B:]
            break
        
        try:
            b = arrB[i_B]
        # If we've reached the end of arrB, fill w/ arrA
        except:
            merged_arr[i:] = arrA[i_A:]
            break
        
        # If the values are equal, add them both and skip the
        # next index; otherwise, add the lesser value
        if a == b:
            merged_arr[i:i + 2] = [a, b]
        elif a < b:
            merged_arr[i] = a
        elif b < a:
            merged_arr[i] = b
        # Increment the index wherever an element was added from
        if a <= b:
            i_A += 1
        if b <= a:
            i_B += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr) // 2 # Find the middle index
        arr = merge(
            merge_sort(arr[:mid]), # Everything up to mid
            merge_sort(arr[mid:]) # Everything after mid
        )
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    arrA, arrB = arr[start:mid], arr[mid:end]
    i_A, i_B = 0, 0
    # Current index of arr is the sum of the indices
    # of arrA & arrB added to the starting index
    while (i := start + i_A + i_B) < end:
        try:
            a = arrA[i_A]
        # If we've reached the end of arrA, fill w/ arrB
        except:
            arr[i:end] = arrB[i_B:]
            break
        
        try:
            b = arrB[i_B]
        # If we've reached the end of arrB, fill w/ arrA
        except:
            arr[i:end] = arrA[i_A:]
            break
        
        # If the values are equal, add them both and skip the
        # next index; otherwise, add the lesser value
        if a == b:
            arr[i:i + 2] = [a, b]
        elif a < b:
            arr[i] = a
        elif b < a:
            arr[i] = b
        # Increment the index wherever an element was added from
        if a <= b:
            i_A += 1
        if b <= a:
            i_B += 1
    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO
    m = ((l + r) // 2) + 1
    if r - l > 0:
        merge_sort_in_place(arr, l, m - 1)
        merge_sort_in_place(arr, m, r)
        merge_in_place(arr, l, m, r+1)
    return arr

arr1 = [8, 4, 2]
print(merge_sort_in_place(arr1, 0, len(arr1)-1))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):
    return arr
