def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]

    answer = 0

    for i in range(len(word)):
        answer += vowels.index(word[i]) * weights[i] + 1

    return answer