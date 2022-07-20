def solution(participant, completion):
    p_dict = {key: 0 for key in dict.fromkeys(participant).keys()}
    for i in participant:
        p_dict[i] += 1 

    for j in completion:
        p_dict[j] -= 1
    answer = list(p_dict.keys())[list(p_dict.values()).index(1)]
    return answer
    
participant=["mislav", "stanko", "mislav", "ana"]	
completion=["stanko", "ana", "mislav"]	
solution(participant, completion)



# def solution(participant, completion):
#     for p in participant:
#         if p in completion and completion.index(p)>-1:
#             completion[completion.index(p)] = ''
#         else:
#             answer = p
#             break
#     return answer
