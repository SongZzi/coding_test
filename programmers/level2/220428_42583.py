def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length  # 다리를 건너는 트럭 list
    end = []  # 다리를 지난 트럭 list
    length = len(truck_weights)
    while True:
        if len(end) == length:  # 모든 트럭이 다리를 지난 경우
            break
        else:
            if queue[0] != 0:
                end.append(queue[0])
            queue.pop(0)
            if len(truck_weights) > 0:
                num = truck_weights[0]
                if sum(queue) + num <= weight:  # 다리를 건너는 트럭의 경우
                    if len(queue) < bridge_length - 1:
                        for i in range(1, bridge_length - len(queue)):
                            queue.append(0)
                    queue.append(num)
                    truck_weights.pop(0)
            answer += 1

    return answer