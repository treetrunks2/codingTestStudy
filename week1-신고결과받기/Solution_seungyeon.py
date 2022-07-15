def solution(id_list, report, k):
    # 몇번씩 신고당했나 -> 배열
    report_cnt_list = [0 for x in range(len(id_list))] 
    reporter_list = ['' for x in range(len(id_list))] 

    for x in set(report):
        reporter = x.split()[0]
        target_index = id_list.index(x.split()[1])
        report_cnt_list[target_index] += 1
        reporter_list[target_index] += reporter+' '

    answer = [0 for x in range(len(id_list))]
    idx = -1
    for y in report_cnt_list:
        idx += 1
        if y >= k:
            for reciever in reporter_list[idx].split():
                answer[id_list.index(reciever)] += 1
        else:
            continue
    return answer
