## 3439. Reschedule Meetings for Maximum Free Time I

def maxFreeTime(eventTime: int, k: int, startTime, endTime) -> int:
    n=len(startTime)
    free=[0]*(n+1)
    free[0]=startTime[0]
    for i in range(1,n):
        free[i]=startTime[i]-endTime[i-1]
    free[-1]=eventTime-endTime[-1]
    temp=sum(free[0:k+1])
    res=temp
    for i in range(1,n+1-k):
        temp+=free[i+k]
        temp-=free[i-1]
        res=max(res, temp)
    return res

def maxFreeTime2(eventTime: int, k: int, startTime, endTime) -> int:
    n=len(startTime)
    temp=startTime[0]
    for i in range(1,k+1):
        if i<n:
            temp+=(startTime[i]-endTime[i-1])
        else:
            temp+=(eventTime-endTime[i-1])
    res=temp
    for i in range(1,n-k+1):
        if i+k<n:
            temp+=(startTime[i+k]-endTime[i+k-1])
        else:
            temp+=(eventTime-endTime[i+k-1])
        if i-2>=0:
            temp-=(startTime[i-1]-endTime[i-2])
        else:
            temp-=startTime[i-1]
        res=max(res, temp)
    return res

if __name__=='__main__':
    eventTime = 10
    k = 1 
    startTime = [0,2,9] 
    endTime = [1,4,10]
    print(maxFreeTime(eventTime, k, startTime, endTime))