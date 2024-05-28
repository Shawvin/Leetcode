## 1208. Get Equal Substrings Within Budget

def equalSubstring(s, t, maxCost):
    dp=[0]*(len(s)+1)
    for i in range(len(s)):
        dp[i+1]=dp[i]+abs(ord(s[i])-ord(t[i]))
    start=0
    end=1
    max_l=0
    while end<=len(s):
        if dp[end]-dp[start]<=maxCost:
            end+=1
        else:
            max_l=max(max_l,end-start-1)
            start+=1
    max_l=max(max_l,end-start-1)
    return max_l

def equalSubstring2(s, t, maxCost):
    start=0
    end=0
    max_l=0
    cur_cost=abs(ord(s[0])-ord(t[0]))
    while end<=len(s)-1:
        if cur_cost<=maxCost:
            end+=1
            if end<len(s):
                cur_cost+=abs(ord(s[end])-ord(t[end]))
        else:
            max_l=max(max_l,end-start)
            cur_cost-=abs(ord(s[start])-ord(t[start]))
            start+=1
    max_l=max(max_l,end-start)
    return max_l

if __name__=='__main__':
    s = "krpgjbjjznpzdfy"
    t = "nxargkbydxmsgby"
    maxCost = 14
    print(equalSubstring2(s, t, maxCost))