class Solution {
    private int[][] memo;
    
    public int solution(int[][] triangle) {
        
        memo = new int[triangle.length][triangle.length];
        
        return getMaxCost(0,0, triangle); //top node of triangle
    }
    
    private int getMaxCost(int row, int col, int[][] triangle) {

        if (isLeafNode(row, triangle.length)) {

            return triangle[row][col];

        } else {

            int left = hasMemo(row+1, col)? 
                    memo[row+1][col] : getMaxCost(row+1, col, triangle);

            int right = hasMemo(row+1, col+1)?
                    memo[row+1][col+1] : getMaxCost(row+1, col+1, triangle);

            int totalCost = triangle[row][col] + Math.max(left, right);

            memo[row][col] = totalCost;
            
            return totalCost;
        }
    }

    private boolean isLeafNode(int rowIndex, int rowLength) {
        return rowIndex == rowLength - 1;
    }

    private boolean hasMemo(int row, int col) {
        return (memo[row][col] != 0);
    }
}