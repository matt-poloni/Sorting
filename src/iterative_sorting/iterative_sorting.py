# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for (i, v) in enumerate(arr):
            if i+1 == len(arr):
                break
            elif v > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr