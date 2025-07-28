## 1233. Remove Sub-Folders from the Filesystem

def removeSubfolders(folder):
    res=[]
    folder.sort()
    res.append(folder[0])
    for i in range(1,len(folder)):
        temp_len=len(res[-1])
        if res[-1]!=folder[i][:temp_len]:
            res.append(folder[i])
        elif folder[i][temp_len]!='/':
            res.append(folder[i])
    return res

def removeSubfolders2(folder):
    res=[]
    folder.sort()
    res.append(folder[0])
    for i in range(1,len(folder)):
        temp=res[-1]+'/'
        temp_len=len(temp)
        if temp!=folder[i][:temp_len]:
            res.append(folder[i])
    return res

if __name__=='__main__':
    folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    print(removeSubfolders(folder))