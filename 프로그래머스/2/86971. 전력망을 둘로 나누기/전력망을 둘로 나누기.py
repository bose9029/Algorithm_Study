from collections import deque

def solution(n, wires):
    answer = n

    for cut in wires:
        graph = [[] for _ in range(n + 1)]

        # cut 전선을 제외하고 그래프 생성
        for a, b in wires:
            if [a, b] == cut:
                continue
            graph[a].append(b)
            graph[b].append(a)

        # BFS로 한쪽 전력망 개수 세기
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        count = 1

        while queue:
            now = queue.popleft()

            for next_node in graph[now]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        other = n - count
        answer = min(answer, abs(count - other))

    return answer