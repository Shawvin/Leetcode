## 767. Reorganize String

## Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

## Return any possible rearrangement of s or return "" if not possible.

def reorganizeString(s):
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char, 0)+1
    char_dict=dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))
    if list(char_dict.values())[0]>(len(s)+1)//2:
        return ''
    result=['']*len(s)
    index=0
    for key in char_dict:
        while char_dict[key]>0:
            if (index>=len(s)):
                index=1
            result[index]=key
            char_dict[key]-=1
            index+=2
    return ''.join(result)

if __name__=='__main__':
    s='asdfasdfasf'
    print(reorganizeString(s))