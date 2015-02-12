package algorithms._023_merge_k_sorted_lists;

/*
 * Solution to 23 - merge k sorted lists
 * Using PriorityQueue of Java
 */

import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class Solution2 {
    public ListNode mergeKLists(List<ListNode> lists) {
    	
    	if (numOfUnexausted(lists) == 0) {
    		return null;
    	}
    	
    	if (numOfUnexausted(lists) == 1) {
    		for (ListNode list : lists) {
    			if (list != null) return list;
    		}
    	}
    	
    	PriorityQueue<ListNode> mins = new PriorityQueue<>(numOfUnexausted(lists),
    			new ListNodeComparator());
    	
    	for (ListNode list : lists) {
    		if (list != null) {
    			mins.add(list);
    		}
    	}
    	
    	ListNode dummyNode = new ListNode(Integer.MIN_VALUE);
    	ListNode currentNode = dummyNode;
    	while (mins.size() > 1) {
    		ListNode min = mins.poll();
    		currentNode.next = min;
    		currentNode = min;
    		if (min.next != null) mins.add(min.next);
    	}
    	
    	currentNode.next = mins.poll();
    	
    	return dummyNode.next;
    }

    
    private int numOfUnexausted(List<ListNode> lists) {
    	int num = 0;
    	for (ListNode list : lists) {
    		if (list != null) num++;
    	}
    	return num;
	}
}

class ListNodeComparator implements Comparator<ListNode> {

	@Override
	public int compare(ListNode node1, ListNode node2) {
		return node1.val - node2.val;
	}
	
}