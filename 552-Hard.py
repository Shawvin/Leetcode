## 552. Student Attendance Record II

def checkRecord(n):
    if n==1:
        return 3
    dp=[1,1,0,1,1,1,0]
    dp_next=[0]*7
    i=2
    #dp[2]=[3,3,2]
    while i<n+1:
        dp_next[0]=sum(dp[:4])
        dp_next[1]=dp[0]+dp[3]
        dp_next[2]=dp[1]
        dp_next[3]=dp[4]+dp[5]+dp[6]
        dp_next[4]=sum(dp[4:])
        dp_next[5]=dp[4]
        dp_next[6]=dp[5]
        dp, dp_next=dp_next,dp
        i+=1
    return sum(dp[:4])%(10**9+7)

def checkRecord2(n):
    # Recursion + Cache
    mod=10**9+7
    #only @cache will lead to MLE
    dp=[[[-1]*3 for _ in range(2)] for _ in range(n+1)]
    def f(i, absent, late):
        if absent>=2 or late>=3: return 0
        if i==0: return 1
        if dp[i][absent][late]!=-1:
            return dp[i][absent][late]
        ans=f(i-1, absent, 0)
        ans+=f(i-1, absent, late+1)
        ans+=f(i-1, absent+1, 0)
        dp[i][absent][late]=ans%mod
        return dp[i][absent][late]
    return f(n, 0, 0)

if __name__=='__main__':
    n = 93573
    print(checkRecord(n))