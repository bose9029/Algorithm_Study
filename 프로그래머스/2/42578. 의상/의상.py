def solution(clothes):
    # 종류별 옷 개수를 저장하고 관리하기 위해 딕셔너리형태로 저장 
    clothes_dict = {}

    # 옷 종류별 개수 세기
    for name, kind in clothes:
        # 해당 옷 종류가 이미 딕셔너리에 있으면 기존 개수에 1을 더함
        # 새로운 옷 종류가 추가될시 0에서 시작해서 1을 더함
        clothes_dict[kind] = clothes_dict.get(kind, 0) + 1

    #곱셉을 해야하기 때문에 초기 값은 1로 지정 
    answer = 1

    # 각 종류마다 선택 경우의 수 계산
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 아무것도 안 입는 경우 1개 제외
    return answer - 1
