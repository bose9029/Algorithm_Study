from collections import Counter
# 테이블(Dictionary) 을 이용한 빈도수 카운팅 알고리즘을 사용하면되며
# python 에서는 collections 모듈 내 Counter 함수를 사용하면 손쉽게 풀이가 가능함.
def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]