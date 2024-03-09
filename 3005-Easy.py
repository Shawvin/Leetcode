## 3005. Count Elements With Maximum Frequency

## You are given an array nums consisting of positive integers.
## Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
## The frequency of an element is the number of occurrences of that element in the array.

def maxFrequencyElements(nums):
    total=0
    freq=dict()
    max_freq=0
    for num in nums:
        freq[num]=freq.get(num,0)+1
        if freq[num]==max_freq:
            total+=max_freq
        if freq[num]>max_freq:
            max_freq=freq[num]
            total=freq[num]
    return total

if __name__=='__main__':
    nums = [1,2,2,3,1,4]
    print(maxFrequencyElements(nums))