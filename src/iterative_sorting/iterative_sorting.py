# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # Create dictionary of numbers w/ count for each
    count_dict = {}
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        try:
            count_dict[i] += 1
        except:
            count_dict[i] = 1
    # Calculate maximum value if none specified
    if maximum == -1:
        for j in count_dict.keys():
            if j > maximum:
                maximum = j
    # Create array with running count of numbers
    sum = 0
    count_list = []
    for i in range(0, maximum + 1):
        try:
            sum += count_dict[i]
        except:
            pass
        count_list.append(sum)
    # Create sorted result from list of running count
    start = 0
    for (num, count) in enumerate(count_list):
        if count > start:
            arr[start:count] = [num] * (count - start)
            start = count
    return arr
