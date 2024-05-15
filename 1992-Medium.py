## 1992. Find All Groups of Farmland

def findFarmland(land):
    m=len(land)
    n=len(land[0])
    res=[]
    q=[]
    for i in range(m):
        for j in range(n):
            if land[i][j]==1:
                q.append([i,j])
                land[i][j]=0
                rec=[i,j,i,j]
                while len(q)>0:
                    cur_i,cur_j=q.pop(0)
                    rec[2]=max(cur_i,rec[2])
                    rec[3]=max(cur_j,rec[3])
                    if cur_i<m-1 and land[cur_i+1][cur_j]==1:
                        land[cur_i+1][cur_j]=0
                        q.append([cur_i+1,cur_j])
                    if cur_j<n-1 and land[cur_i][cur_j+1]==1:
                        land[cur_i][cur_j+1]=0
                        q.append([cur_i,cur_j+1])
                res.append(rec)
    return res

if __name__=='__main__':
    land=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]]
    print(findFarmland(land))