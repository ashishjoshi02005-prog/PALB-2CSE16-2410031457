def all_palindrome(arr):
    for num in arr:
        s = str(num)
        if s != s[::-1]:
            return False
    return True
print(all_palindrome([111, 222, 333, 444, 555])) 
print(all_palindrome([121, 131, 20]))   