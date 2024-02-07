## 49. Group Anagrams

## Given an array of strings strs, group the anagrams together. You can return the answer in any order.

## An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
    result_dict={}
    for string in strs:
        sorted_str=''.join(sorted(string))
        if sorted_str in result_dict:
            result_dict[sorted_str].append(string)
        else:
            result_dict[sorted_str]=[string]
    return list(result_dict.values())

if __name__=='__main__':
    strs=["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))