## 2116. Check if a Parentheses String Can Be Valid

def canBeValid(s, locked):
    n=len(locked)
    l_min, l_max=0,0
    for i in range(n):
        if locked[i]=='0':
            l_min-=1
            l_max+=1
        elif s[i]=='(':
            l_min+=1
            l_max+=1
        else:
            l_min-=1
            l_max-=1
        if l_max<0:
            return False
        if l_min<0:
            l_min=1
    return l_min==0

if __name__=='__main__':
    s = "))()))"
    locked = "0000"
    print(canBeValid(s, locked))