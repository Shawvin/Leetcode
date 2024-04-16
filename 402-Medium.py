## 402. Remove K Digits

## Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

def removeKdigits(num, k):
    if k==len(num):
        return '0'
    res=[]
    count=0
    flag=False
    for i, char in enumerate(num):
        if len(res)>0 and char<res[-1]:
            while len(res)>0 and res[-1]>char:
                res.pop()
                count+=1
                if count==k:
                    flag=True
                    break
        if flag:
            res+=num[i:]
            break
        else:
            res.append(char)
    while count<k:
        res.pop()
        count+=1
    res=''.join(res).lstrip("0")
    return res if len(res)>0 else '0'
    
def removeKdigits2(num, k):
    n=len(num)
    if n==k:
        return '0'
    st=[]
    count=0
    result=''
    done=False
    for idx,i in enumerate(num):
        if not st or i>st[-1]:
            st.append(i)
        else:
            while st and i<st[-1]:
                st.pop()
                count+=1
                if count==k:
                    result=''.join(st)+num[idx:]
                    done=True
                    break
            if done:
                break
            st.append(i)
    if len(st)>n-k:
        while len(st)>n-k:
            st.pop()
        result=''.join(st)
    if len(result.lstrip('0'))>0:
        return result.lstrip('0')
    else:
        return '0'

if __name__=='__main__':
    num='1432219'
    k=3
    print(removeKdigits(num,k))