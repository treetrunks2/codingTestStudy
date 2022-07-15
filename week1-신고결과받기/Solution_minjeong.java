package com.treetrunks;

import java.util.*;

public class Solution {
    public int[] solution(String[] id_list, String[] reports, int k) {
        int[] answer = new int[id_list.length];

        Map<String, HashSet<Integer>> reportedUserMap = new HashMap<>();

        for (String report : reports) {

            String[] chunk = report.split(" ");

            String reporter = chunk[0];
            String reportedUser = chunk[1];

            int reporterIndex = -1;

            for (int i =0; i<id_list.length;i++) {
                if (reporter.equals(id_list[i]))
                    reporterIndex = i;
            }

            if (reportedUserMap.containsKey(reportedUser)) {

                reportedUserMap.get(reportedUser).add(reporterIndex);

            } else {

                HashSet<Integer> reporterSet = new HashSet<>();
                reporterSet.add(reporterIndex);

                reportedUserMap.put(reportedUser, reporterSet);
            }

        }

        for (String user: reportedUserMap.keySet()) {
            Set<Integer> reporterSet = reportedUserMap.get(user);

            if (reporterSet.size() >= k) {

                Iterator<Integer> iterator = reporterSet.iterator();

                while (iterator.hasNext()) {

                    int index = iterator.next();

                    answer[index]++;
                }

            }
        }

        return answer;
    }
}
