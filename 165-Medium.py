## 165. Compare Version Numbers

def compareVersion(version1, version2):
    v1=version1.split('.')
    v2=version2.split('.')
    n=max(len(v1),len(v2))
    for i in range(n):
        if i>=len(v1):
            v1.append('0')
        if i>=len(v2):
            v2.append('0')
        if int(v1[i])>int(v2[i]):
            return 1
        elif int(v1[i])<int(v2[i]):
            return -1
    return 0

if __name__=='__main__':
    version1 = "1.01"
    version2 = "1.001"
    print(compareVersion(version1, version2))