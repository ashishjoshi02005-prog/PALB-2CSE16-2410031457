def chocolate_distribution(arr, m):
    if m > len(arr):
        return -1
    arr.sort()
    min_diff = 999999999
    for i in range(len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_distribution(arr, m))