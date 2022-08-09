def solution(triangle):
    result = [[0,triangle[0][0],0]]
    for i in range(1,len(triangle)):
        triangle[i].insert(0,0)
        result.append([0])

        for j in range(1,len(triangle[i])):
            result[i].append(max(result[i-1][j]+triangle[i][j],result[i-1][j-1]+triangle[i][j]))
        result[i].append(0)
    answer = max(result[-1])
    return answer
