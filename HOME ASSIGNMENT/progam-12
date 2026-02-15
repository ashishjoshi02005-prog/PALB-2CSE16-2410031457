def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()
    ans = arr[n-1] - arr[0]
    small = arr[0] + k
    big = arr[n-1] - k
    if small > big:
        small, big = big, small
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        if subtract >= small or add <= big:
            continue
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    return min(ans, big - small)
print(get_min_diff([1, 5, 8, 10], 2))      # Output: 5
print(get_min_diff([3, 9, 12, 16, 20], 3)) # Output: 11