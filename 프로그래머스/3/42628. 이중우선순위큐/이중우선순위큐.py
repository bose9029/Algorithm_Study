def solution(operations):
    answer = []

    # operations에 있는 명령어를 하나씩 확인
    for operation in operations:
        # 명령어와 숫자를 공백 기준으로 분리
        # split함수를 사용하여, 문자열을 분리하여 리스트형태로 저장 
        command, num = operation.split()

        # 문자열 형태로 저장된 숫자를 int로 변환
        num = int(num)

        # 삽입 명령어인 경우
        if command == "I":
            answer.append(num)

        # 삭제 명령어인 경우
        elif command == "D":

            # 큐가 비어있으면 삭제 명령은 무시
            if len(answer) == 0:
                continue

            # D 1이면 최댓값 삭제
            if num == 1:
                answer.remove(max(answer))

            # D -1이면 최솟값 삭제
            elif num == -1:
                answer.remove(min(answer))

    # 모든 연산이 끝난 후 큐가 비어있으면 [0, 0] 반환
    if len(answer) == 0:
        return [0, 0]

    # 큐가 비어있지 않으면 [최댓값, 최솟값] 반환
    return [max(answer), min(answer)]