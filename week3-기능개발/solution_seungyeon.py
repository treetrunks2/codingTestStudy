def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        # 맨 앞 요소 100넘으려면 몇일 걸리는지 계산
        days = math.ceil((100-progresses[0])/speeds[0])
        
        progresses.pop(0)
        speeds.pop(0)
        done_task_aday = 1
        
        # 다음차례 하나씩 보면서 100 넘으면 pop
        while  len(progresses) != 0 and  progresses[0]+speeds[0]*days >=100:
            progresses.pop(0)
            speeds.pop(0)
            done_task_aday += 1
        answer.append(done_task_aday)
        
    return answer
