## 1653. Minimum Deletions to Make String Balanced

def minimumDeletions(s):
    f=0
    b=0
    for c in s:
        if c=='a':
            b+=1
    res=b
    for c in s:
        if c=='a':
            b-=1
        if c=='b':
            f+=1
        res=min(res,f+b)
    return res

if __name__=='__main__':
    s = "aababbab"
    print(minimumDeletions(s))