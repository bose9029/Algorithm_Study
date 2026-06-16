from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    
    # 다리 위 상태: 길이를 bridge_length만큼 유지
    bridge = deque([0] * bridge_length)
    current_weight = 0
    
    while trucks:
        time += 1
        
        # 다리에서 맨 앞 위치의 트럭이 빠져나감
        current_weight -= bridge.popleft()
        
        # 다음 트럭이 올라갈 수 있으면 올림
        if current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 못 올라가면 빈 공간 추가
            bridge.append(0)
    
    # 마지막 트럭이 다리를 완전히 빠져나가는 시간 추가
    return time + bridge_length