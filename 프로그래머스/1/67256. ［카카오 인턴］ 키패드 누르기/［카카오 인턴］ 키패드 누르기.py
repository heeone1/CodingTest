#1, 4, 7을 입력할 때는 왼손 엄지손가락
#3, 6, 9를 입력할 때는 오른손 엄지손가락
#2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
#약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용

#순서대로 누를 번호가 담긴 배열 numbers
#왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand

def solution(numbers, hand):
    l = '*'
    r = '#'
    h = 'R'
    
    if (hand == "left"):
        h = 'L'
        
    answer = ''
    
    keypad = {
        1: (0, 3), 2: (1, 3), 3: (2, 3),
        4: (0, 2), 5: (1, 2), 6: (2, 2),
        7: (0, 1), 8: (1, 1), 9: (2, 1),
        '*': (0, 0), 0: (1, 0), '#': (2, 0),
    }
    
    for i in numbers:
        
        if i in [1, 4, 7]:
            answer += 'L'
            l = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r = i
        else:
#             rx = (keypad[i][0] - keypad[r][0])*(keypad[i][0] - keypad[r][0])
#             ry = (keypad[i][1] - keypad[r][1])*(keypad[i][1] - keypad[r][1])
#             rd = rx + ry 

#             lx = (keypad[i][0] - keypad[l][0])*(keypad[i][0] - keypad[l][0])
#             ly = (keypad[i][1] - keypad[l][1])*(keypad[i][1] - keypad[l][1])
#             ld = lx + ly 

            rx = abs(keypad[i][0] - keypad[r][0])
            ry = abs(keypad[i][1] - keypad[r][1])
            rd = rx + ry 
            
            lx = abs(keypad[i][0] - keypad[l][0])
            ly = abs(keypad[i][1] - keypad[l][1])
            ld = lx + ly 

            if (rd == ld):
                if (h == 'R'):
                    answer += h
                    r = i
                else:
                    answer += h
                    l = i
            elif (rd < ld):
                answer += 'R'
                r = i
            else:
                answer += 'L'
                l = i
                
    
    # for i in numbers:
    #     if i in [1, 4, 7]:
    #         answer += 'L'
    #         l = i
    #     elif i in [3, 6, 9]:
    #         answer += 'R'
    #         r = i
    #     else:
    #         if (i == 2):
    #             if (r == 3):
    #                 if (l == 1):
    #                     answer += h
    #                     if (h == 'R'):
    #                         answer += h
    #                         r = i
    #                     else:
    #                         answer += h
    #                         l = i
    #                 else:
    #                     answer += 'R'
    #                     r = i
    #         elif (i == 5):
    #             if (r == 6):
    #                 if (l == 4):
    #                     answer += h
    #                     if (h == 'R'):
    #                         answer += h
    #                         r = i
    #                     else:
    #                         answer += h
    #                         l = i
    #                 else:
    #                     answer += 'R'
    #                     r = i
    #         elif (i == 8):
    #             if (r == 9):
    #                 if (l == 7):
    #                     answer += h
    #                     if (h == 'R'):
    #                         answer += h
    #                         r = i
    #                     else:
    #                         answer += h
    #                         l = i
    #                 else:
    #                     answer += 'R'
    #                     r = i    
    #         else:
    #             if (r == '#'):
    #                 if (l == '*'):
    #                     answer += h
    #                     if (h == 'R'):
    #                         answer += h
    #                         r = i
    #                     else:
    #                         answer += h
    #                         l = i
    #                 else:
    #                     answer += 'R'
    #                     r = i  
                
    return answer