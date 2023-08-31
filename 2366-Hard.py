## 2366. Minimum Replacements to Sort the Array

def minimumReplacement(nums):
        upper_limit=nums[-1]
        count=0
        for num in nums[::-1]:
            if num>upper_limit:
                operation=((num-1)//upper_limit)
                count+=operation
                if num%upper_limit!=0:
                    upper_limit=num//(operation+1)
            else:
                upper_limit=num
        return count

if __name__=='__main__':
    nums = [12,9,7,6,17,19,21]
    print(minimumReplacement(nums))