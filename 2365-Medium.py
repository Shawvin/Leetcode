## 2365. Task Scheduler II

## You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.
## 
## You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.
## 
## Each day, until all tasks have been completed, you must either:
## 
## Complete the next task from tasks, or Take a break.
## Return the minimum number of days needed to complete all tasks.

def taskSchedulerII(tasks, space):
    breakdays=0
    rec_task={}
    for i,task in enumerate(tasks):
        if task in rec_task and i+breakdays-rec_task[task]-1<space:
            breakdays+=(space-i-breakdays+rec_task[task]+1)
        rec_task[task]=i+breakdays
    return len(tasks)+breakdays

if __name__=='__main__':
    tasks = [1,2,1,2,3,1]
    space = 3
    print(taskSchedulerII(tasks, space))