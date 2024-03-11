## 791. Custom Sort String

## You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
## Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before 
## a character y in order, then x should occur before y in the permuted string.
## Return any permutation of s that satisfies this property.

def customSortString(order,s):
    c_dict={}
    for char in s:
        c_dict[char]=c_dict.get(char,0)+1
    result=''
    for ch in order:
        if ch in c_dict:
            result+=(ch*c_dict.pop(ch))
    for ch in c_dict:
        result+=(ch*c_dict[ch])
    return result

if __name__=='__main__':
    order = "bcafg"
    s = "abcd"
    print(customSortString(order,s))