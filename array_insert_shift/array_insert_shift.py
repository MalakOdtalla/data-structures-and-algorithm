import math


def arrayinsertShift(arr, num):

  newArr = []
  middle = math.ceil(len(arr)/2)

  for i in range(len(arr)+1):
    if(i < middle) :
        newArr[i] = arr[i]

    elif(i == middle):
        newArr[i] = num

    elif (i > middle):
        newArr[i] = arr[i -1]

    return newArr

print(arrayinsertShift([3,4,5],7))