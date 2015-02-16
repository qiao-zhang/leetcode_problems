package algorithms._062_unique_paths;

public class SolutionDP {
	public long uniquePaths(int row, int col) {
		int[][] table = new int[row][col];
		
		for (int down = 0; down < row; down++) {
			table[down][0] = 1;
		}
		for (int right = 1; right < col; right++) {
			table[0][right] = 1;
		}
		for (int down = 1; down < row; down++) {
			for (int right = 1; right < col; right++) {
				table[down][right] = table[down-1][right] + table[down][right-1];
			}
		}
		
		return table[row-1][col-1];
	}
}
