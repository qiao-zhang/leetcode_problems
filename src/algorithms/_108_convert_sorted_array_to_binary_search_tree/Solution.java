/*
 * Solution to 108 - Convert Sorted Array to Binary Search Tree
 */
package algorithms._108_convert_sorted_array_to_binary_search_tree;

import java.util.Arrays;

public class Solution {
	public TreeNode sortedArrayToBST(int[] arr) {
		if (arr.length == 0) {
			return null;
		}

		int medianVal = arr[arr.length / 2];
		TreeNode root = new TreeNode(medianVal);
		int[] leftHalf = Arrays.copyOfRange(arr, 0, arr.length / 2);
		int[] rightHalf = Arrays.copyOfRange(arr, arr.length / 2 +1, arr.length);
		root.left = sortedArrayToBST(leftHalf);
		root.right = sortedArrayToBST(rightHalf);
		
		return root;
	}
}