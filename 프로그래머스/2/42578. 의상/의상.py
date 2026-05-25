def solution(clothes):
    clothes_dict = {}

    # 옷 종류별 개수 세기
    for name, kind in clothes:
        clothes_dict[kind] = clothes_dict.get(kind, 0) + 1

    answer = 1

    # 각 종류마다 선택 경우의 수 계산
    for count in clothes_dict.values():
        answer *= (count + 1)

    # 아무것도 안 입는 경우 1개 제외
    return answer - 1