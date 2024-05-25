## 1255. Maximum Score Words Formed by Letters

def maxScoreWords(words, letters, score):
    l_dict={}
    for ch in letters:
        l_dict[ch]=l_dict.get(ch,0)+1
    def backtrack(i, words, l_dict, score, cur_score):
        if i==len(words):
            return cur_score
        j=0
        included=True
        while j>=0 and j<len(words[i]):
            if included and l_dict.get(words[i][j],0)>0:
                l_dict[words[i][j]]-=1
                cur_score+=score[ord(words[i][j])-ord('a')]
                j+=1
            else:
                included=False
                j-=1
                if j>=0:
                    l_dict[words[i][j]]+=1
                    cur_score-=score[ord(words[i][j])-ord('a')]
        if included:
            max_score=backtrack(i+1, words, l_dict, score, cur_score)
            for ch in words[i]:
                l_dict[ch]+=1
                cur_score-=score[ord(ch)-ord('a')]
            return max(max_score, backtrack(i+1, words, l_dict, score, cur_score))
        else:
            return backtrack(i+1, words, l_dict, score, cur_score)
    cur_score=0
    return backtrack(0, words, l_dict, score, cur_score)

if __name__=='__main__':
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    print(maxScoreWords(words, letters, score))
