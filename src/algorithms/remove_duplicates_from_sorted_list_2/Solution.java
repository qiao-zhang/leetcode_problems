package algorithms.remove_duplicates_from_sorted_list_2;

/*
 * Solution for 82 - Remove Duplicates from Sorted Array II
 * https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	
    	if (head == null) {
    		return null;
    	}
    	
    	ListNode dummyNode = new ListNode(Integer.MIN_VALUE);
    	ListNode tailNode = dummyNode;
    	dummyNode.next = head;
    	
    	ListNode lastNode = head;
    	ListNode currentNode = head.next;
    	int lastVal = lastNode.val;
    	boolean duplicated = false;
    	while (currentNode != null) {
    		if (currentNode.val == lastVal) {
    			duplicated = true;
    		} else {
    			if (!duplicated) { // not duplicated, then update lastNode
    				tailNode.next = lastNode;
    				tailNode = lastNode;
    			}
    			duplicated = false;
    			lastVal = currentNode.val;
    		}
    		lastNode = currentNode;
    		currentNode = currentNode.next;
    	}
    	
    	tailNode = duplicated ? null : lastNode;

    	return dummyNode.next;
    }
}