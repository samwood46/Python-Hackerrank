def solution(A):
    n = len(A)
    result = 0
    for i in range(n - 1): #if the elements beside eachother are the same the result goes up
        if (A[i] == A[i + 1]):
            result = result + 1 #result is how many adjacenecys there are
    r = 0
    for i in range(n):#0-5
        count = 0
        if (i > 0): #if i is greater than 0
            if (A[i - 1] != A[i]): #if the adjacencys arent the same count will go up
                count = count + 1
            else:
                count = count -1 #if they are the count will go down
        if (i < n - 1):
            if (A[i + 1] != A[i]):
                count = count - 1
            else:
                count = count +1
        r = max(r, count)
    return result + r +1

print (solution([1,0,1,0,1,1]))