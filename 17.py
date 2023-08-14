## 17. Letter Combinations of a Phone Number
## Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

## 0 <= digits.length <= 4
## digits[i] is a digit in the range ['2', '9'].
import string
alphanumericmap={}
for i in range(2,10):
    if i!=9:
        alphanumericmap[str(i)]=string.ascii_lowercase[(i-2)*3:(i-1)*3]
    else:
        alphanumericmap[str(i)]=string.ascii_lowercase[-4:]

def letterCombinations(digits):
    result=[]
    if len(digits)==0:
        return result
    for char in alphanumericmap[digits[0]]:
        sublevel=letterCombinations(digits[1:])
        if len(sublevel)==0:
            result.append(char)
            continue
        for sub in sublevel:
            result.append((char+sub))
    return result


if __name__=='__main__':
    digits = "2334"
    print(letterCombinations(digits))