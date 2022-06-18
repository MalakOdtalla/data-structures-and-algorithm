def BinarySearch(list, key):
	low = 0
	high = len(list) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2
		if list[mid] < key:
			low = mid + 1
		elif list[mid] > key:
			high = mid - 1
		else:
			return mid
	return -1

print(BinarySearch([1, 3, 5, 8],9))