## 97. Interleaving String
## Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
def isInterleave(s1, s2, s3):
    if (s2==''):
        return s1==s3
    if (s1==''):
        return s2==s3
    if (len(s2)+len(s1)!=len(s3)):
        return False
    result=[]       
    for j in range(len(s2)):
        result.append(s2[:j+1]==s3[:j+1])
    for i in range(len(s1)):
        for j in range(len(s2)):
            if j==0:
                result[j]=(s1[:i+1]==s3[:i+1] and s2[j]==s3[i+j+1]) or (result[j] and s1[i]==s3[i+j+1])
            else:
                result[j]=(result[j-1] and s2[j]==s3[i+j+1]) or (result[j] and s1[i]==s3[i+j+1])
    print(result)
    return result[-1] 

if __name__=='__main__':
    s1 = "aabcc"
    s2 = "dbbca" 
    s3 = "aadbbcbcac"
    isInterleave(s1,s2,s3)