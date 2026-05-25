import heapq

def solution(jobs):
    # 요청 시간 기준으로 정렬
    jobs.sort()

    heap = []          
    time = 0           
    total = 0          
    index = 0          
    count = 0          

    while count < len(jobs):

        # 현재 시간까지 요청된 작업들을 heap에 넣음
        while index < len(jobs) and jobs[index][0] <= time:
            request, duration = jobs[index]

            # 소요시간이 짧은 작업이 먼저 나오도록 duration을 앞에 둠
            heapq.heappush(heap, (duration, request))
            index += 1

        # 처리할 수 있는 작업이 있다면
        if heap:
            duration, request = heapq.heappop(heap)

            # 작업을 수행한 뒤 현재 시간 증가
            time += duration

            # 반환 시간 = 작업 종료 시간 - 요청 시간
            total += time - request

            count += 1

        # 아직 처리할 작업이 없으면 다음 작업 요청 시점으로 이동
        else:
            time = jobs[index][0]

    # 평균 반환 시간의 정수 부분 반환
    return total // len(jobs)