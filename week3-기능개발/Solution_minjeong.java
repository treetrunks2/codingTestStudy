import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();

        int q_size = progresses.length;

        int front = 0;

        while (isQueueNotEmpty(front, q_size)) {

            for (int i=0; i< progresses.length; i++) {
                progresses[i] += speeds[i];
            }

            int doneProgressCount = 0;
            while ( isQueueNotEmpty(front, q_size) 
                    && isProgressDone(progresses[front])) {

                doneProgressCount++; 
                front++; //pop
            }

            if (doneProgressCount > 0) {
                answer.add(doneProgressCount);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    private boolean isQueueNotEmpty(int frontIndex, int lastIndex) {
        return (frontIndex < lastIndex);
    }

    private boolean isProgressDone(int progress) {
        return progress >= 100;
    }
}