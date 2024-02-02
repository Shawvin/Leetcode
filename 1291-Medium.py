## 1291. Sequential Digits

## An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
## Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

def sequentialDigits(low, high):
    lo=len(str(low))
    hi=len(str(high))
    digit='123456789'
    result=[]
    for i in range(lo,hi+1):
        for j in range(10-i):
            num=int(digit[j:j+i])
            if num>=low and num<=high:
                result.append(num)
    return result


def sequentialDigits2(low, high):
    lo=len(str(low))
    hi=len(str(high))
    digit='123456789'
    result=[]
    for i in range(lo,hi+1):
        for j in range(10-i):
            num=int(digit[j:j+i])
            if num<low:
                continue
            if num>high:
                break
            result.append(num)
    return result

if __name__=='__main__':
    low=1000
    high=13000
    print(sequentialDigits(low, high))