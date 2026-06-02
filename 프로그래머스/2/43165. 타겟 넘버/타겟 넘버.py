def solution(numbers, target):
    answer = 0

    # DFS 함수 사용
    def dfs(index, total):
        nonlocal answer

        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 계산 결과가 target과 같으면 방법 수 증가
            if total == target:
                answer += 1
            return

        # 현재 숫자를 더하는 경우
        dfs(index + 1, total + numbers[index])

        # 현재 숫자를 빼는 경우
        dfs(index + 1, total - numbers[index])

    # 0번째 숫자부터 시작, 초기 합계는 0
    dfs(0, 0)

    return answer