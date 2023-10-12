## 1095. Find in Mountain Array

## Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

class MountainArray:
    array=None
    def __init__(self, array):
        self.array=array
    def get(self, index):
        return self.array[index]
    def length(self):
        return len(self.array)
    
def findInMountainArray(target, mountain_arr):
    n=mountain_arr.length()
    lo=0
    hi=n-1
    peak=0
    while lo<hi:
        med=(lo+hi)//2
        cur=mountain_arr.get(med)
        left=mountain_arr.get(med-1)
        right=mountain_arr.get(med+1)
        if cur>left and cur>right:
            peak=med
            break
        if cur>left and cur<right:
            lo=med
        if cur<left and cur>right:
            hi=med
    print(peak)
    result=[-1,-1]
    lo=0
    hi=peak
    while lo<=hi:
        med=(lo+hi)//2
        cur=mountain_arr.get(med)
        if cur==target:
            result[0]=med
            break
        if cur>target:
            hi=med-1
        if cur<target:
            lo=med+1
    if result[0]!=-1:
        return result[0]                                          
    lo=peak
    hi=n-1
    while lo<=hi:
        med=(lo+hi)//2
        cur=mountain_arr.get(med)
        if cur==target:
            result[1]=med
            break
        if cur<target:
            hi=med-1
        if cur>target:
            lo=med+1
    return result[1]

if __name__=='__main__':
    array=[1,5,2]
    target=2
    mountain_arr=MountainArray(array)
    print(findInMountainArray(target, mountain_arr))