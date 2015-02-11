/*
 * Solution to 57 - Insert Interval
 * https://oj.leetcode.com/problems/insert-interval/
 */
import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        int headIdx = 0;
        while (headIdx < intervals.size() && intervals.get(headIdx).end < newInterval.start) {
            headIdx++;
        }
        if (headIdx >= intervals.size()) {
            intervals.add(newInterval);
            return intervals;
        }
        int tailIdx = intervals.size() - 1;
        while (tailIdx >= 0 && intervals.get(tailIdx).start > newInterval.end) {
            tailIdx--;
        }
        if (tailIdx < 0) {
            intervals.add(0, newInterval);
            return intervals;
        }
        if (intervals.get(headIdx).start < newInterval.start) {
            newInterval.start = intervals.get(headIdx).start;
        }
        if (intervals.get(tailIdx).end > newInterval.end) {
            newInterval.end = intervals.get(tailIdx).end;
        }
        List<Interval> retIntervals = new ArrayList<Interval>();
        for (int i = 0; i < headIdx; i++) {
        	retIntervals.add(intervals.get(i));
        }
        retIntervals.add(newInterval);
        for (int i = tailIdx+1; i < intervals.size(); i++) {
        	retIntervals.add(intervals.get(i));
        }
        return retIntervals;
    }
}
