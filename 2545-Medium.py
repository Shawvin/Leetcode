## 2545. Sort the Students by Their Kth Score

## There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, 
## where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. 
## The matrix score contains distinct integers only.
## You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.
## Return the matrix after sorting it.

def sortTheStudents(score, k):
    result=[]
    k_score=[]
    for i in range(len(score)):
        k_score.append((score[i][k],i))
    k_score.sort(key=lambda x:-x[0])
    for _,idx in k_score:
        result.append(score[idx])
    return result

if __name__=='__main__':
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    k=2
    print(sortTheStudents(score, k))