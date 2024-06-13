def solution(id_list, report, k):
    # 각 유저가 받은 메일 수를 저장할 딕셔너리 초기화
    mail = {}
    # 각 유저가 신고된 횟수를 저장할 딕셔너리 초기화
    reported = {}
    
    # 신고 기록을 처리하여 각 유저별로 신고한 유저 리스트를 저장
    for r in report:
        id1, id2 = r.split()  # 신고자 id1과 신고된 유저 id2를 분리
        tmp = reported.get(id2, [])  # id2가 신고된 기록을 가져오고, 없으면 빈 리스트 반환
        if id1 not in tmp:  # id1이 이미 id2를 신고한 적이 없으면
            tmp.append(id1)  # 신고한 유저 리스트에 id1을 추가
        reported[id2] = tmp  # 갱신된 리스트를 다시 저장
    
    # 신고된 유저가 k번 이상 신고된 경우 메일을 보낼 유저를 카운트
    for v in reported.values():
        if len(v) >= k:  # 신고된 횟수가 k 이상인 경우
            for id in v:  # 해당 유저를 신고한 모든 유저에게
                mail[id] = mail.get(id, 0) + 1  # 메일 수를 1 증가
    
    # 결과를 저장할 리스트 초기화
    answer = []
    # 각 유저가 받은 메일 수를 결과 리스트에 저장
    for id in id_list:
        answer.append(mail.get(id, 0))  # 메일 수가 없으면 0을 반환하여 추가
    
    return answer  # 최종 결과 반환
