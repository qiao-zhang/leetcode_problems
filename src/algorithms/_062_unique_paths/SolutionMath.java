package algorithms._062_unique_paths;

public class SolutionMath {
    public long uniquePaths(int row, int col) {
    	int down = row - 1;
    	int right = col - 1;
    	if (down == 0 || right == 0) return 1;
    	int total = down + right;
    	
    	int small = right < down ? right : down;
    	
    	return combination(total, small) / factorial(small);
    }
    
    private long factorial(int n) {
    	if (n <= 1) {
    		return 1;
    	}
    	return factorial(n - 1) * n;
    }
    
    private long combination(int t, int s) {
    	if (s == 0 || s == t) return 1;
    	if ((t - s) < s) return combination(t, t - s);
    	long result = 1;
    	for (int i = 0; i < s; i++) {
    		result = result * (t - i) / (s - i);
    	}
    	return result;
    }
}