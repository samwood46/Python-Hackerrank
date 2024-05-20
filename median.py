def findMedian(arr):
    # Write your code here
    arr.sort()
    
    length = len(arr)
    median = 0

    if len(arr) == 2:
        return int((sum(arr))/2)
    #even
    if length % 2 ==0:
        half = length/2
        half = int(half)
        half1 = half+1
        median = int(((arr[half])+(arr[half1]))/2)
    #odd
    if length %2 != 0:
        index = (float(length/2)-0.5)
        index = int(index)
        median = arr[index]
  
    return median


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    print (findMedian(arr))