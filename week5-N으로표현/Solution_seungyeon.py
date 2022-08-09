# 시간 초과 해결 방법! 각 단계에서 ()안에 들어가는 값은 미리 계산해서 배열에 입력한다. 어차피 ()있으면 concat연산이 안 되기 때문
def cross(answer_list, trial, a, b):
    temp_answer = []
    for val1 in answer_list[a]:
        for val2 in answer_list[b]:
            if val1.isdigit() and val2.isdigit():
                temp_answer.append(val1+val2) #concat
            
            #덧셈
            temp_answer.append('('+str(eval(val1+'+'+val2))+')') #temp_answer.append('('+val1+'+'+val2+')') <- 시간 초과 된 코드
            #뺄셈
            if val1 > val2:
                temp_answer.append('('+str(eval(val1+'-'+val2))+')')
            #곱셈
            temp_answer.append('('+str(eval(val1+'*'+val2))+')')
            #나눗셈
            if eval(val2) != 0:
                temp_answer.append('('+str(eval(val1+'//'+val2))+')') 
            
    temp_answer = set(temp_answer)
    return temp_answer
def solution(N, number):
    answer = -1
    ans_arr = [[],[str(N)]]
    
    if(N==number):
        answer=1
    else:
        for trial in range(2,9): # 8초과
            if answer != -1:
                break
            temp_ans_arr = []
            print('trial no: ',trial)
            for x in range(1,trial):
                # 1) 우선 trial 번호 안의 몇번째 리스트를 서로 붙일 것인지 확인
                cross_result = cross(ans_arr, trial, x, trial-x)
                if number in list(map(lambda x: eval(x), cross_result)) :
                    answer = trial
                    break
                temp_ans_arr += cross_result
            ans_arr.append(set(temp_ans_arr))
            
            
    return answer

solution(4,5800)
#solution(4,31)
