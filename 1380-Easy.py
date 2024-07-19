## 1380. Lucky Numbers in a Matrix

def luckyNumbers (matrix):
    n=len(matrix[0])
    row_Min=[min(x) for x in matrix]
    col_Max=[max([x[i] for x in matrix]) for i in range(n)]
    res=[]
    for x in row_Min:
        for y in col_Max:
            if x==y:
                res.append(x)
    return res

if __name__=='__main__':
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    print(luckyNumbers (matrix))