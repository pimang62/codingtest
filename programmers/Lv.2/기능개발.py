def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution(progresses=[93, 30, 55], speeds=[1, 30, 5]))
print(solution(progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1]))