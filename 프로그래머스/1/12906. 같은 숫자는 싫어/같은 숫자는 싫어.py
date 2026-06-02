def solution(arr):
    answer = []

    for num in arr:
        # 마지막으로 넣은 숫자와 현재 숫자가 다르면 추가
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer