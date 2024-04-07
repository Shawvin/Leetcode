## 1249. Minimum Remove to Make Valid Parentheses

def minRemoveToMakeValid(s):
    lst=[]
    for i in range(len(s)):
        if s[i]==')':
            if not lst or s[lst[-1]]!='(':
                lst.append(i)
            else:
                lst.pop()
        if s[i]=='(':
            lst.append(i)
    res=''
    for i in range(len(s)):
        if not lst:
            res+=s[i:]
            break
        elif i==lst[0]:
            lst.pop(0)
        else:
            res+=s[i]
    return res

if __name__=='__main__':
    s="lee(t(c)o)de)"
    print(minRemoveToMakeValid(s))