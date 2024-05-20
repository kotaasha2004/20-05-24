def find_smallest_missing(arr):
    # Initialize the smallest missing positive integer
    smallest_missing = 1
    
    # Iterate through the sorted array
    for num in arr:
        # If the current number is greater than the smallest missing,
        # we cannot form the smallest missing number
        if num > smallest_missing:
            break
        # Otherwise, add the current number to smallest_missing
        smallest_missing += num
    
    # Return the smallest missing positive integer
    print(smallest_missing)

input_list=input().split()
integer_list=list(map(int, input_list))
sorted_list=sorted(integer_list)
find_smallest_missing(sorted_list)
