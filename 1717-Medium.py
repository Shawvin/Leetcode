## 1717. Maximum Score From Removing Substrings

def maximumGain(s ,x, y):
    st=[]
    if x>y:
        upper_score,lower_score=x,y
        upper,lower='ab','ba'
    else:
        upper_score,lower_score=y,x
        upper,lower='ba','ab'
    res=0
    for i in range(len(s)):
        st.append(s[i])
        while len(st)>1 and st[-2]==upper[0] and st[-1]==upper[1]:
            res+=upper_score
            st.pop()
            st.pop()
    t=''.join(st)
    st=[]
    for i in range(len(t)):
        st.append(t[i])
        while len(st)>1 and st[-2]==lower[0] and st[-1]==lower[1]:
            res+=lower_score
            st.pop()
            st.pop()
    return res

if __name__=='__main__':
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(maximumGain(s ,x, y))