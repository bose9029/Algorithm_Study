def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(fatigue, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            need, cost = dungeons[i]

            # 아직 방문하지 않았고, 현재 피로도가 최소 필요 피로도 이상이면 탐험 가능
            if not visited[i] and fatigue >= need:
                visited[i] = True
                dfs(fatigue - cost, count + 1)
                visited[i] = False

    dfs(k, 0)
    return answer