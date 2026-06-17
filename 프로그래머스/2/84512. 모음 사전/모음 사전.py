def solution(word):
    #알파벳 모음을 배열에 저장
    vowels = ['A', 'E', 'I', 'O', 'U']

    # 가중치 계산
    weights = []
    for i in range(5):
        weight = 0
        for j in range(5 - i):
            weight += 5 ** j
        weights.append(weight)

    answer = 0

    for i, ch in enumerate(word):
        answer += vowels.index(ch) * weights[i] + 1

    return answer
