## 76. Minimum Window Substring

## Given two strings s and t of lengths m and n respectively, return the minimum window 
## substring of s such that every character in t (including duplicates) is included in the window. 
## If there is no such substring, return the empty string "".

# sliding window
def minWindow(s,t):
    m=len(s)
    n=len(t)
    left=0
    right=n
    dict_t={}
    dict_s={}
    for i in t:
        dict_t[i]=dict_t.get(i,0)+1
    for j in s[:n+1]:
        dict_s[j]=dict_s.get(j,0)+1
    min_str=''
    min_len=m
    check=False
    while right<=m:
        if dict_s.get(s[right],0)<dict_t.get(s[right],0):
            check=False
            right+=1
            if right<m:
                dict_s[s[right]]=dict_s.get(s[right],0)+1
            check=False
        else:
            check=True
            min_str=s[left:right]
            min_len=right-left
        while left<right and check:
            if s[left] not in dict_t or dict_s[s[left]]>dict_t[s[left]]:
                dict_s[s[left]]-=1
                left+=1
                if min_len>right-left+1:
                    min_str=s[left:right+1]
                    min_len=right-left+1
            elif dict_s[s[left]]==dict_t[s[left]]:
                if min_len>=right-left+1:
                    min_str=s[left:right+1]
                    min_len=right-left+1
                dict_s[s[left]]-=1
                left+=1
                break
            else:
                dict_s[s[left]]-=1
                left+=1
                break
    return min_str

def minWindow2(s,t):
    if not s or not t or len(s)<len(t):
        return ""
    dict_t={}
    count=len(t)
    left=0
    right=0
    min_len=float('inf')
    start_index=0
    for char in t:
        dict_t[char]=dict_t.get(char,0)+1
    
    while right<len(s):
        if dict_t.get(s[right],0)>0:
            count-=1
        dict_t[s[right]]=dict_t.get(s[right],0)-1
        right+=1
        while count==0:
            if right-left<min_len:
                start_index=left
                min_len=right-left
            if dict_t[s[left]]==0:
                count+=1
            dict_t[s[left]]+=1
            left+=1
    return "" if min_len==float('inf') else s[start_index:start_index+min_len]    
        
if __name__=='__main__':
    s='ab'
    t='b'
    print(minWindow(s,t))