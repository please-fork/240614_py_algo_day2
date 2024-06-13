# 첫 번째 줄에서 N과 M 값을 읽어와 정수로 변환
N, M = map(int, input().split())

# 포켓몬 이름을 키로, 포켓몬 번호를 값으로 가지는 dictionary 생성
str_to_int = {}
    
# 포켓몬 번호를 키로, 포켓몬 이름을 값으로 가지는 dictionary 생성
int_to_str = {}
    
# N개의 줄에 걸쳐 포켓몬 이름을 입력받아 두 dictionary에 저장
for i in range(1, N + 1):
    name = input()
    str_to_int[name] = str(i)
    int_to_str[str(i)] = name

# 결과 출력을 위한 리스트
result = []
    
# M개의 줄에 걸쳐 문제를 입력받아 정답을 결과 리스트에 저장
for j in range(N + 1, N + 1 + M):
    key = input()    
       
    # 입력이 포켓몬 이름인 경우
    if key in str_to_int:
        result.append(str_to_int[key])
    # 입력이 포켓몬 번호인 경우
    else:
        result.append(int_to_str[key])
    
# 결과 리스트 출력
for r in result:
    print(r)