package com.treetrunks;


import java.util.*;

public class Solution {

    public int solution(int[] priorities, int location) {
        int answer = 1;

        LinkedList<Integer> printList = new LinkedList<>();

        for (int i = 0; i < priorities.length; i++) {
            printList.add(i);
        }

        while (!printList.isEmpty()) {
            int loc = printList.removeFirst();

            if (hasMorePriorityPaper(priorities[loc], printList.iterator(), priorities)) {

                printList.addLast(loc);

            } else {
                if (loc == location) {
                    break;
                } else {
                    answer++;
                }
            }
        }

        return answer;
    }

    private boolean hasMorePriorityPaper(int priority, Iterator<Integer> iter, int[] priorities) {
        boolean result = false;

        while (iter.hasNext()) {
            Integer loc = iter.next();
            if (priorities[loc] > priority) {
                result = true;
            }
        }

        return result;
    }
}
