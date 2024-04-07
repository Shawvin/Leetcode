## 1544. Make The String Great

def makeGood(s):
    res=''
    b=len(s)
    a=0
    while b!=a:
        res=''
        b=len(s)
        i=0
        while i<b:                
            if i==len(s)-1:
                res+=s[i]
                i+=1
            elif abs(ord(s[i])-ord(s[i+1]))==32:
                i+=2
            else:
                res+=s[i]
                i+=1
        a=len(res)
        s=res
    return res

def makeGood(s):
    pre=-1
    s=list(s)
    for cur in range(len(s)):
        if pre<0 or abs(ord(s[cur])-ord(s[pre]))!=32:
            pre+=1
            s[pre]=s[cur]
        else:
            pre-=1        
    return "".join(s[:pre+1])


if __name__=='__main__':
    s="leEeetcode"
    print(makeGood(s))