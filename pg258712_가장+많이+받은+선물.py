def solution(friends, gifts):
    d = {}  # 각 친구가 서로 주고 받은 선물의 순차적 차이를 저장할 딕셔너리

    # 선물 교환 내역을 처리
    for g in gifts:
        f1, f2 = g.split()
        d[f1] = d.get(f1, {})
        d[f1][f2] = d[f1].get(f2, 0) + 1  # f1이 f2에게 선물한 횟수 증가
        d[f2] = d.get(f2, {})
        d[f2][f1] = d[f2].get(f1, 0) - 1  # f2가 f1에게 받은 횟수는 감소

    score = {}  # 각 친구별 총 선물 순위를 저장할 딕셔너리
    for f in friends:
        if f in d:  # 친구 f가 선물 교환에 참여한 경우에만
            score[f] = sum(d[f].values())  # 각 친구의 총 선물 순위를 계산
        else:
            score[f] = 0  # 선물 교환에 참여하지 않은 경우 점수는 0

    result = []  # 각 친구별로 점수를 계산하여 저장할 리스트

    for f1 in friends:
        tmp = 0
        for f2 in friends:
            if f1 == f2:
                continue
            net = d.get(f1, {}).get(f2, 0)  # f1이 f2에게 선물한 순차적 차이
            if net > 0:
                tmp += 1  # f1이 f2에게 더 많이 선물한 경우
            elif net == 0 and score[f1] > score[f2]:
                tmp += 1  # 선물 횟수가 동일하고 f1의 총 선물 순위가 더 높은 경우

        result.append(tmp)

    return max(result)  # 최대 점수를 반환