## 1395. Count Number of Teams

def numTeams(rating):
    n=len(rating)
    res=0
    for i in range(1,n-1):
        count1=0
        count2=0
        for j in range(i):
            if rating[j]>rating[i]:
                count1+=1
        for j in range(i+1,n):
            if rating[j]<rating[i]:
                count2+=1
        res+=count1*count2
        res+=(i-count1)*(n-i-1-count2)
    return res

if __name__=='__main__':
    rating = [2,5,3,4,1]
    print(numTeams(rating))
