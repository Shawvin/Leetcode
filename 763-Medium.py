## 763. Partition Labels

## You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
## Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s. 
## Return a list of integers representing the size of these parts.

def partitionLabels(s):
    char_dict={}
    for idx,char in enumerate(s):
        if char in char_dict:
            char_dict[char][1]=idx
        else:
            char_dict[char]=[idx,idx]
    intervals=list(char_dict.values())
    intervals.sort()
    cur=intervals[0]
    res=[]
    for s,e in intervals[1:]:
        if cur[1]<s:
            res.append(cur)
            cur=[s,e]
        else:
            cur[0]=min(cur[0],s)
            cur[1]=max(cur[1],e)
    res.append(cur)
    print(res)
    result=[]
    for i1,i2 in res:
        result.append(i2-i1+1)
    return result

def partitionLabels2(s):
    char_dict={}
    for idx,char in enumerate(s):
        char_dict[char]=idx
    res=[]
    left,right=0,0
    for idx,char in enumerate(s):
        right=max(right,char_dict[char])
        if idx==right:
            res.append(right-left+1)
            left=right+1
            right+=1
    return res

if __name__=='__main__':
    s="ababcbacadefegdehijhklij"
    print(partitionLabels(s))