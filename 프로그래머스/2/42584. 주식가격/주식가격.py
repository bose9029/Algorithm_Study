def solution(prices):
    #초 단위로 기록된 주식가격이 담긴 배열
    answer = [0] * len(prices)

    #모든 주식 가격을 배열을 For문으로 순회 
    for i in range(len(prices)):
        #현재 시점(i) 이후의 가격들을 확인
        for j in range(i + 1, len(prices)):
            # 주식가격이 유지되면 시간을 1초 증가 
            answer[i] += 1

            #현재가격보다 낮은가격이 되면 탐색을 종료 
            if prices[j] < prices[i]:
                break

    return answer