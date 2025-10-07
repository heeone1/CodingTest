#한 번에 한 명의 유저를 신고
#한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리
#게시판 이용 정지를 시키면서 정지 메일을 발송 / k번 이상 신고된 유저는 게시판 이용이 정지
#해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송 / 


def solution(id_list, report, k):
    # 중복 제거
    report = set(report)

    # 신고 기록 분리(초기화)
    reports = {user: [] for user in id_list}  # 각 유저가 누구를 신고했는지
    counts = {user: 0 for user in id_list}    # 각 유저가 신고당한 횟수

    for r in report:
        a, b = r.split()     # "신고자 피신고자"
        reports[a].append(b)
        counts[b] += 1

    # 정지된 사람들
    stopped = {user for user, c in counts.items() if c >= k}
    
    # stopped = set() # 빈 집합 만들기 = set
    # for user, c in counts.items():
    #     if c >= k:
    #         stopped.add(user)
    
    # 각 유저별 메일 개수 계산
    answer = []
    for user in id_list:
        total = 0
        for target in reports[user]:
            if target in stopped:
                total += 1
        answer.append(total)

    return answer
