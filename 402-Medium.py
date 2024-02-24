## 402. Remove K Digits

## Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

def removeKdigits(num, k):
    if len(num)==k:
        return '0'
    cur=[]
    for i in range(len(num)):
        cur.append(num[:i+1])
    pre=cur.copy()
    for i in range(1,k+1):
        cur[i-1]=''
        for j in range(i,len(num)):
            cur[j]=min(pre[j-1],cur[j-1]+num[j])
        cur,pre=pre,cur
    if len(pre[-1].lstrip('0'))>0:
        return pre[-1].lstrip('0')
    else:
        return '0'
    
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