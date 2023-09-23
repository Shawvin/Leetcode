## 1048. Longest String Chain

## wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without 
## changing the order of the other characters to make it equal to wordB.

## Return the length of the longest possible word chain with words chosen from the given list of words.

def longestStrChain(words):
    length_word={}
    max_length=0
    words=sorted(words, key=lambda x: len(x))
    for word in words:
        length_word[word]=1
        for i in range(len(word)):
            if i+1<len(word):
                sub_word=word[0:i]+word[i+1:]
            else:
                sub_word=word[0:i]
            length_word[word]=max(length_word[word], length_word.get(sub_word,0)+1)
        if length_word[word]>max_length:
            max_length=length_word[word]
    return max_length

if __name__=='__main__':
    words=["a","b","ba","bca","bda","bdca"]
    print(longestStrChain(words))