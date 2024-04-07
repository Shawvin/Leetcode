## 1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s):
    count=0
    max_count=0
    for ch in s:
        if ch=='(':
            count+=1
        elif ch==')':
            max_count=max(max_count,count)
            count-=1
    return max_count

if __name__=='__main__':
    s="(1+(2*3)+((8)/4))+1"
    print(maxDepth(s))