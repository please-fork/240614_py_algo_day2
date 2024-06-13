def solution(clothes):
    items = {}
    for name, category in clothes:
        # 각 의류의 카테고리별 개수를 셈
        items[category] = items.get(category, 0) + 1
    
    # 모든 조합의 수를 계산
    answer = 1
    for v in items.values():
        # 각 카테고리에서 안 입는 경우를 포함해 +1 후 곱함
        answer *= (v + 1)
    
    # 아무 것도 안 입는 경우를 하나 제외함
    answer -= 1
    
    return answer