def insertion_sort(arr):
    for i in range(len(arr)):
        val =i - 1
        temp = arr[i]

        while val >= 0 and temp < arr[val]:
            arr[val + 1] = arr[val]
            val = val - 1

        arr[val + 1] = temp
    return arr


print(insertion_sort([8,4,23,42,16,15]))

