package algorithms._023_merge_k_sorted_lists;

/*
 * Solution to 23 - merge k sorted lists
 * Using PriorityQueue of Java
 */

import java.util.List;

public class SecondSolution {
    public ListNode mergeKLists(List<ListNode> lists) {
    	if (lists.isEmpty()) {
    		return null;
    	}
    	
    	while (lists.size() > 1) {
    		int size = lists.size();
    		for (int i = 0; i < size - 1; i = i + 2) {
    			ListNode node1 = lists.remove(0);
    			ListNode node2 = lists.remove(0);
    			lists.add(merge2Lists(node1, node2));
    		}
    	}
    	
    	return lists.get(0);
    }
    
    private static ListNode merge2Lists(ListNode node1, ListNode node2) {
    	ListNode dummyNode = new ListNode(Integer.MIN_VALUE);
    	ListNode head = dummyNode;
    	while (node1 != null && node2 != null) {
    		if (node1.val < node2.val) {
    			dummyNode.next = node1;
    			dummyNode = node1;
    			node1 = node1.next;
    		} else {
    			dummyNode.next = node2;
    			dummyNode = node2;
    			node2 = node2.next;
    		}
    	}
    	
    	if (node1 == null) {
    		dummyNode.next = node2;
    	}
    	
    	if (node2 == null) {
    		dummyNode.next = node1;
    	}
    	
    	return head.next;
    }
}