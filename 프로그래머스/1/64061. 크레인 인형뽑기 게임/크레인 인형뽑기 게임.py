def solution(board, moves):
    answer = 0
    anw = []
    ar = 0
    r = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                anw.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
        if len(anw) >= 2:
            if anw[-2] == anw[-1]:
                answer += 2
                anw.pop()
                anw.pop()
                
    return answer