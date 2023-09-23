class Solution {
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        Set<Integer> rowSet = new HashSet<Integer> ();
        Set<Integer> colSet = new HashSet<Integer> (); 

        for (int i=0; i<row; i++){
            for (int j=0; j<col; j++){
                // System.out.println(matrix[i][j]);
                if (matrix[i][j]==0){
                    rowSet.add(i);
                    colSet.add(j);
                }
                    
                
            }
        }
        // System.out.println(rowSet);
        // System.out.println(colSet);

        //update all columns with zeros
        for (int i=0; i<row;i++){
            for( int j: colSet){
                matrix[i][j]=0;
            }
        }
        //update all columns with zeros
        for (int i=0; i<row;i++){
            if (rowSet.contains(i)){
                for (int j=0; j<col; j++){
                    matrix[i][j]=0;
                }
            }
            
        }
        
            
        
        
        
    }
}