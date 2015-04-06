package algorithms._041_first_missing_positive;

import java.util.Arrays;

public class Solution {
    public int firstMissingPositive(int[] A) {
        int val = 0;
        int i = 0;
        while (i < A.length) {
            val = A[i];
            if (val <= 0 || val > A.length || A[val-1] == val) {
                i++;
                continue;
            }
            A[i] = A[val-1];
            A[val-1] = val;
        }

        for (i = 0; i <= A.length; i++) {
            if (i <= 0)
                continue;
            if (i != A[i-1])
                return i;
        }
        return i;
    }
    
    public static void main(String[] args) {
        int[] A = {3, 4, -1, 1};
        Solution sol = new Solution();
        int i = sol.firstMissingPositive(A);
        System.out.println(i);
        System.out.println(Arrays.toString(A));
    }
}