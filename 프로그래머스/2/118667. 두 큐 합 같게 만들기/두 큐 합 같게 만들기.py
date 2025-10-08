from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
        
    q1l = len(queue1)
    q2l = len(queue2)
    
    m = 2*(q1l+q2l)
    
    q1_sum = 0
    q2_sum = 0

    sum = 0
    c = 0
    
    #전체 합
    for i in range(q1l):
        sum += queue1[i] + queue2[i]
        q1_sum += queue1[i]
        q2_sum += queue2[i]
    sum = sum//2
    
    if q1_sum == sum:
        return 0
    
    while c <= m:
        if q1_sum > q2_sum:
            x = q1.popleft()
            q1_sum -= x
            q2_sum += x
            q2.append(x)
        else:
            x = q2.popleft()
            q1_sum += x
            q2_sum -= x
            q1.append(x)
        c += 1
        
        if q1_sum == sum:
            return c
    
    if q1_sum == sum:
        answer = c
    else:
        answer = -1
    
    return answer