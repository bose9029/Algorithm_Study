#sorting(정렬)알고라즘을 사용 
def solution(s):
    sorted_chars = sorted(s, reverse=True)# 문자열의 각 문자를 내림차순으로 정렬
    answer = ''.join(sorted_chars) # 정렬된 문자들을 하나의 문자열로 통합 
    return answer