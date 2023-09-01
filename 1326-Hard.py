## 1326. Minimum Number of Taps to Open to Water a Garden

## There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).
## There are n + 1 taps located at points [0, 1, ..., n] in the garden.
## Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.
## Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

## greedy
def minTaps(n, ranges):
    reach=[0]*(n+1)
    for i,e in enumerate(ranges):
        if e==0:
            continue
        start=max(0, i-e)
        reach[start]=max(reach[start], i+e)
    count, far_reach, end=0, 0, 0
    for i, e in enumerate(reach):
        if i>end:
            if far_reach<=end:
                return -1
            end=far_reach
            count+=1
        far_reach=max(far_reach, e)
    return count+(end<n)

## dp
def minTaps2(n, ranges):
    dp=[float("inf")]*(n+1)
    dp[0]=0
    for i,e in enumerate(ranges):
        if e==0:
            continue
        left=max(0,i-e)
        right=min(n,i+e)
        for j in range(left, right+1):
            dp[j]=min(dp[j], dp[left]+1)
    if dp[-1]==float("inf"):
        return -1
    else:
        return dp[-1] 

if __name__=='__main__':
    ranges = [3,4,1,1,0,0]
    n=5
    print(minTaps2(n, ranges))