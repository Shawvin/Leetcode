## 948. Bag of Tokens

## You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, 
## where each tokens[i] donates the value of tokeni.

## Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
## Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
## Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
## Return the maximum possible score you can achieve after playing any number of tokens.

def bagOfTokensScore(tokens, power):
    left=0
    right=len(tokens)-1
    max_score=0
    cur=power
    tokens.sort()
    cur_score=0
    while left<=right:
        if cur>=tokens[left]:
            cur_score+=1
            cur-=tokens[left]
            left+=1
            max_score=max(max_score,cur_score)
        elif cur<tokens[left] and cur_score>0:
            cur_score-=1
            cur+=tokens[right]
            right-=1
        else:
            break
    return max_score

if __name__=='__main__':
    tokens = [100,200,300,400]
    power = 200
    print(bagOfTokensScore(tokens, power))