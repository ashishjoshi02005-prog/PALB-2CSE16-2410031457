def rowWithMax1s(arr):
    n = len(arr)
    m = len(arr[0])
    max_ones = 0
    result = -1
    for i in range(n):
        left, right = 0, m - 1
        first_one = m
        while left <= right:
            mid = (left + right) // 2
            if arr[i][mid] == 1:
                first_one = mid
                right = mid - 1
            else:
                left = mid + 1
        ones_count = m - first_one
        if ones_count > max_ones:
            max_ones = ones_count
            result = i
    return result
arr = [
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
print(rowWithMax1s(arr))