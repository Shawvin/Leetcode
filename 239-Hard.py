## 239. Sliding Window Maximum

## You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
## Each time the sliding window moves right by one position.
## 
## Return the max sliding window.

def maxSlidingWindow(nums, k):
    res=[]
    st=[]
    for num in nums[:k]:
        if len(st)==0 or num<=st[-1]:
            st.append(num)
            continue
        while len(st)>0 and num>st[-1]:
            st.pop()
        st.append(num)
    res.append(st[0])
    for i in range(k,len(nums)):
        if st[0]==nums[i-k]:
            st.pop(0)
        while len(st)>0 and nums[i]>st[-1]:
            st.pop()
        st.append(nums[i])
        res.append(st[0])
    return res

if __name__=='__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(maxSlidingWindow(nums,k))