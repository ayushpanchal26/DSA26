def reverse(i, arr, len_arr):
    if i >= len_arr / 2:
        return
    # Swap elements
    arr[i], arr[len_arr - i - 1] = arr[len_arr - i - 1], arr[i]
    reverse(i + 1, arr, len_arr)

n = int(input("Enter the length of array: "))
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

reverse(0, arr, n)

for i in range(n):
    print(arr[i])
