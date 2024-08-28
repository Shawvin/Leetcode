## 624. Maximum Distance in Arrays

def maxDistance(arrays):
    max_2=[]
    min_2=[]
    for i in range(len(arrays)):
        if len(max_2)<1:
            max_2.append((arrays[i][-1],i))
            min_2.append((arrays[i][0],i))
        elif len(max_2)<2:
            if arrays[i][-1]>max_2[0][0]:
                max_2.insert(0, (arrays[i][-1],i))
            else:
                max_2.append((arrays[i][-1],i))
            if arrays[i][0]<min_2[0][0]:
                min_2.insert(0, (arrays[i][0],i))
            else:
                min_2.append((arrays[i][0],i))
        else:
            if arrays[i][-1]>max_2[0][0]:
                max_2[0],max_2[1]=(arrays[i][-1],i), max_2[0]
            elif arrays[i][-1]>max_2[1][0]:
                max_2[1]=(arrays[i][-1],i)
            if arrays[i][0]<min_2[0][0]:
                min_2[0],min_2[1]=(arrays[i][0],i), min_2[0]
            elif arrays[i][0]<min_2[1][0]:
                min_2[1]=(arrays[i][0],i)
    if min_2[0][1]!=max_2[0][1]:
        return abs(max_2[0][0]-min_2[0][0])
    else:
        return max(abs(max_2[1][0]-min_2[0][0]), abs(max_2[0][0]-min_2[1][0]))
    
if __name__=='__main__':
    arrays = [[1,2,3],[4,5],[1,2,3]]
    print(maxDistance(arrays))