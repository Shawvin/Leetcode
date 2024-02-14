## 647. Palindromic Substrings

## Given a string s, return the number of palindromic substrings in it.
## A string is a palindrome when it reads the same backward as forward.
## A substring is a contiguous sequence of characters within the string.

def countSubstrings(s):
    pre=set()
    pre.add(s[0])
    count=1
    for i in range(1,len(s)):
        cur=set()
        cur.add(s[i])
        for p in pre:
            if (p+s[i])==(p+s[i])[::-1]:
                cur.add(p+s[i])
            if len(p)>=i:
                continue
            elif s[i-len(p)-1]==s[i]:
                new_p=s[i-len(p)-1]+p+s[i]
                cur.add(new_p)
        pre=cur
        count+=len(cur)
    return count

if __name__=='__main__':
    s=''
    print(countSubstrings(s))