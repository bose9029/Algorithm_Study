import heapq

def solution(scoville, K):

    # 스코빌 변수를 힙 형태로 변환
    heapq.heapify(scoville)

    # 섞은 횟수는 0으로 지정 
    count = 0

    # 가장 작은 스코빌 지수가 K보다 작을 동안 반복
    while scoville[0] < K:

        # 음식이 1개뿐이면 더 이상 섞을 수 없으므로 실패
        if len(scoville) < 2:
            return -1

        # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2) 적용
        heapq.heappush(
            scoville,
            heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        )

        # 섞은 횟수 증가
        count += 1

    # 모든 음식의 스코빌 지수가 K 이상이면 횟수 반환
    return count
