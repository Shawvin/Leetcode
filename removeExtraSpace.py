def removeExtraSpace(s):
    s=list(s)
    r=0
    l=0
    while r<len(s):
        if s[r]!=' ':
            if l!=0:
                s[l]=' '
                l+=1
            while r<len(s) and s[r]!=' ':
                s[l]=s[r]
                l+=1
                r+=1
        else:
            r+=1
    return ''.join(s[:l])

if __name__=='__main__':
    s = ' the   sky   is  blue  '
    print(removeExtraSpace(s))