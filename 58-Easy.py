## 58. Length of Last Word

## Given a string s consisting of words and spaces, return the length of the last word in the string.

## A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s):
    count=0
    last_count=0
    for ch in s:
        if ch==' ':
            if count!=0:
                last_count=count
            count=0
        else:
            count+=1
    return count if count!=0 else last_count

def lengthOfLastWord2(s):
    count=0
    last_count=0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            count+=1
        else:
            if count!=0:
                last_count=count
                count=0
        if last_count and not count:
            break
    return last_count if last_count else count

if __name__=='__main__':
    s="Hello World"
    print(lengthOfLastWord(s))