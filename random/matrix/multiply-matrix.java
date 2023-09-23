
import java.io.*;

class GFG {
	public static void main (String[] args) {
	    int m1[][] = {{ 1, 2 },
                      { 3, 4 } };
 
        int m2[][] = { { 1, 1,  },
                      { 1, 1, } };
        multiply(m1,m2);              
		System.out.println("GfG!");
	}
	
	
	static int[][] multiply(int mat1[][], int mat2[][]){
	    int r1 = mat1.length, c1 = mat1[0].length;
	    int r2 = mat2.length, c2 = mat2[0].length;
	    
	    if(r2 !=c1){
	        System.out.println("multiplication not allowed");
	        int empty[][]={};
	        return empty;
	    }
	    
	    int newMat[][]= new int[r1][c2];
	    
	    for (int a=0; a<r1;a++){
	        for(int b=0; b<c2; b++){
	            for (int c=0; c<r2; c++){
	                newMat[a][b]+= mat1[a][c] * mat2[c][b];
	            }
	        }
	    }
	    System.out.println(newMat[0][0]);
	    return newMat;
	    
	}
}