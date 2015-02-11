/*
 * Solution to 57 - Insert Interval
 * https://oj.leetcode.com/problems/insert-interval/
 */

package algorithms.insert_interval;

import java.util.List;
import java.util.ArrayList;

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    	// Find the idx of the first interval whose end is larger than new.Interval.
    	// It can be 0 or interval.size() at edges cases.
        int headIdx = 0;
        while (headIdx < intervals.size() && intervals.get(headIdx).end < newInterval.start) {
            headIdx++;
        }
        // If the idx is intervals.size(), then just add the new one at the end.
        if (headIdx >= intervals.size()) {
            intervals.add(newInterval);
            return intervals;
        }
        
        // Symmetrically, ...
        int tailIdx = intervals.size() - 1;
        while (tailIdx >= 0 && intervals.get(tailIdx).start > newInterval.end) {
            tailIdx--;
        }
        if (tailIdx < 0) {
            intervals.add(0, newInterval);
            return intervals;
        }
        
        // Update the ends of the new interval
        if (intervals.get(headIdx).start < newInterval.start) {
            newInterval.start = intervals.get(headIdx).start;
        }
        if (intervals.get(tailIdx).end > newInterval.end) {
            newInterval.end = intervals.get(tailIdx).end;
        }
        
        // Make the new list.
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
