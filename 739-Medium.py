## 739. Daily Temperatures

## Given an array of integers temperatures represents the daily temperatures, 
## return an array answer such that answer[i] is the number of days you have to 
## wait after the ith day to get a warmer temperature. 
## If there is no future day for which this is possible, keep answer[i] == 0 instead.

def dailyTemperatures(temperatures):
    l=len(temperatures)
    if l==1:
        return [0]
    answer=[0]*l
    temp=[]
    for i in range(l-1,-1,-1):
        if len(temp)==0:
            temp.insert(0,i)
            answer[i]=0
        else:
            while len(temp)!=0 and temperatures[i]>=temperatures[temp[0]]:
                temp.pop(0)
            if len(temp)==0:
                answer[i]=0
            else:
                answer[i]=temp[0]-i
            temp.insert(0,i)
    return answer

## monotonic decrease stack
def dailyTemperatures2(temperatures):
    l=len(temperatures)
    answer=[0]*l
    temp=[]
    for i in range(l):
        while temp and temperatures[i]>temperatures[temp[-1]]:
            idx=temp.pop()
            answer[idx]=i-idx
        temp.append(i)
    return answer

if __name__=='__main__':
    temperatures=[]
    print(dailyTemperatures(temperatures))