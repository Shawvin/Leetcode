## 496. Next Greater Element I

from collections import defaultdict

def nextGreaterElement(nums1, nums2):
    map=defaultdict(lambda: -1)
    st=[]
    for num in nums2[::-1]:
        while len(st)>0 and num>st[-1]:
            st.pop()
        if len(st)==0:
            map[num]=-1
        else:
            map[num]=st[-1]
        st.append(num)
    return [map[num] for num in nums1]

if __name__=='__main__':
    nums1=[4,1,2]
    nums2=[1,3,4,2]
    print(nextGreaterElement(nums1, nums2))