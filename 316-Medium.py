## 316. Remove Duplicate Letters

## Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
## the smallest in lexicographical order among all possible results.

def removeDuplicateLetters(s):
    result=''
    last_occur={}
    for i,char in enumerate(s):
        last_occur[char]=i
    for i,char in enumerate(s):
        if char not in result:
            temp=str(result)
            for ch in temp[::-1]:
                if ch>char and last_occur[ch]>i:
                    result=result.replace(ch,'')
                else:
                    break
            result+=char
    return result

if __name__=='__main__':
    s="cbacdcbc"
    print(removeDuplicateLetters(s))