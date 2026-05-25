
# Set을 이용한 중복을 제거한 개수 구하는 문제. 
def solution(nums):
    # 선택할 수 있는 폰켓몬 수 = 전체 마릿수의 절반
    max_pick = len(nums) // 2

    # 중복을 제거한 폰켓몬 종류 개수
    kind_count = len(set(nums))

    # 고를 수 있는 수보다 종류가 많으면 max_pick까지만 가능
    # 종류가 더 적으면 kind_count까지만 가능
    return min(max_pick, kind_count)