## 1750. Minimum Length of String After Deleting Similar Ends

## Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

## Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
## Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
## The prefix and the suffix should not intersect at any index.
## The characters from the prefix and suffix must be the same.
## Delete both the prefix and the suffix.
## Return the minimum length of s after performing the above operation any number of times (possibly zero times).

## two pointer
def minimumLength(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            break
        else:
            while left<right and s[left]==s[left+1]:
                left+=1
            left+=1
            while right>left and s[right]==s[right-1]:
                right-=1
            right-=1
    return max(0, right-left+1)

def minimumLength2(s):
    left=0
    right=len(s)-1
    while left<right and s[left]==s[right]:
        ch=s[left]
        while left<=right and s[left]==ch:
            left+=1
        while right>left and s[right]==ch:
            right-=1
    return max(0, right-left+1)

if __name__=='__main__':
    s = "aabccabba"
    print(minimumLength(s))