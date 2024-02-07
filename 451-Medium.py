## 451. Sort Characters By Frequency

## Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

## Return the sorted string. If there are multiple answers, return any of them

def frequencySort(s):
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char,0)+1
    value_dict={}
    for key in char_dict:
        value_dict[char_dict[key]]=value_dict.get(char_dict[key],'')+(key*char_dict[key])
    sort_freq=sorted(value_dict.keys(),reverse=True)
    result=''
    for i in sort_freq:
        result+=value_dict[i]
    return result

def frequencySort2(s):
    char_dict={}
    for char in s:
        char_dict[char]=char_dict.get(char,0)+1
    print(char_dict)
    char_dict=dict(sorted(char_dict.items(), key=lambda x:-x[1]))
    print(char_dict)
    result=''
    for i in char_dict:
        result+=(i*char_dict[i])
    return result
if __name__=='__main__':
    s='Aabb'
    print(frequencySort2(s))