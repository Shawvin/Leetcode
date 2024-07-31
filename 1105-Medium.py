## 1105. Filling Bookcase Shelves

def minHeightShelves(books, shelfWidth):
    dp=[0]*(len(books)+1)
    dp[0]=0
    for i in range(len(books)):
        t,h=books[i]
        j=i
        cur_w=0
        local_h=h
        shelf_h=dp[i]+h
        while j>=0 and cur_w+books[j][0]<=shelfWidth:
            cur_w+=books[j][0]
            local_h=max(local_h,books[j][1])
            shelf_h=min(dp[j]+local_h,shelf_h)
            j-=1
        dp[i+1]=shelf_h
    return dp[-1]

if __name__=='__main__':
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    print(minHeightShelves(books, shelfWidth))