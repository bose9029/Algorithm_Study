from collections import deque

def solution(priorities, location):

    # (우선순위,인덱스) 형태로 큐 생성
    queue = deque(
        [(priority, idx) for idx, priority in enumerate(priorities)]
    )

    # 실행 순서 카운트 초기화
    order = 0

    while queue:

        # 큐의 맨 앞 프로세스 꺼내기
        current = queue.popleft()

        # 현재 프로세스보다 우선순위가 높은 프로세스가 존재하는지 확인
        if any(current[0] < process[0] for process in queue):

            # 더 높은 우선순위가 있으면 다시 큐의 뒤로 이동
            queue.append(current)

        else:
            # 실행
            order += 1

            # 찾고자 하는 프로세스라면 실행 순서 반환
            if current[1] == location:
                return order