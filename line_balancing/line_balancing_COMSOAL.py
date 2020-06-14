import math
from random import *
time = [17,9,9,14,11,12,10,3]
task = 8
NIP =[]
NIPW = []
TK=[]
WIP=[]
for j in range(task):
    TK.append(j+1)

matrix = [[0,	0	,0	,0	,1	,0	,0	,0],
[0	,0	,0	,0	,0,	0,	0,	0],
[1	,0	,0	,0	,0	,0	,0	,0],
[0,	0	,0	,0	,0,	0	,0	,0],
[0	,0,	0	,0	,0	,0	,0,	0],
[0	,1	,1,	0,	0,	0,	0,	0],
[0	,0	,0	,1	,0,	0	,0,	0],
[0	,0	,0	,0	,0,	1	,0	,0]]

for j in range(task):
    total = 0
    for column in range(task):
        total += matrix[j][column]
    NIP.append(total)

for j in range(task):
    list=[]
    WIP.append(list)

for i in range(task):
    for j in range(task):
        if matrix[j][i] == 1:
            WIP[i].append(j+1)

X = 999
UB = math.inf
cycletime = 35
t = 0
o = 0
optimum = []

for x in range(X):
    soft_time = time
    IDLE = 0    #step 2 start   
    c = cycletime
    t = 1
    A = TK
    NIPW = NIP
    S = []     
    B = []
    S.append([])
       #step 2 end
    while len(A) != 0 and IDLE<=UB :
        F = []  
        for j in range(len(A)): #step 3 start
            if NIPW[A[j]-1] == 0:
                B.append(A[j])   #step 3 end
        for j in range(len(B)): #step 4 start
            for k in range(t):
                if 2 in S[k] and 1 in A:
                    soft_time[0] = 12
                if 1 in S[k] and 2 in A:
                    soft_time[1] = 5
                if 4 in S[k] and 3 in A:
                    soft_time[2] = 5
                if 3 in S[k] and 4 in A:
                    soft_time[3] = 8
                if time[B[j]-1] <= c :
                    if B[j] not in A:
                        pass
                    else:
                        F.append(B[j])   #step 4 end
        if len(F) == 0: #step 5
            IDLE = IDLE + c
            c  = cycletime
            t += 1
            S.append([])
        else:   #step 6
            istar = math.ceil(random()*len(F))
            sel_task = F[istar-1]
            for j in range(task):
                if j+1 in WIP[sel_task-1]:
                    NIPW[j] = NIPW[j] - 1
            F.remove(sel_task)
            S[t-1].append(sel_task)
            A.remove(sel_task)
            B.remove(sel_task)
            c -= time[sel_task-1]
        if len(A) == 0: #step 7
            IDLE += c
            if IDLE <= UB:
                UB = IDLE
                optimum = S
                o = t
                soft_time_op = soft_time
print('Number of opened stations is {}'.format(o) )
print('Final assignments: {}'.format(optimum))
print('Task times: {}'.format(soft_time_op))
print('Idle time is {}'.format(UB))
for k in range(o):
    z = 0
    for l in range(len(optimum[k])):
        z += soft_time_op[optimum[k][l] -1 ] 
    print('Total time of station {}: {}'.format(k+1, z))