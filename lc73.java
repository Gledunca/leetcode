import java.util.Arrays;


class Solution {
    public void setZeroes(int[][] matrix) {
        int i = 0;
        int j = 0;
        boolean firstRowZero=false;
        boolean firstColZero=false;
        for (i = 0; i < matrix.length; ++i){
            for (j = 0; j < matrix[0].length; ++j){
                if (matrix[i][j] == 0) {
                    System.out.println("Zero at " + i + " " + j);
                    if (j == 0) {
                        firstColZero=true;
                    }
                    matrix[0][j] = 0;
                    if (i > 0) {
                        matrix[i][0] = 0;
                    }
                    else {
                        firstRowZero=true;
                    }
                }
            }
        }
        System.out.println(firstRowZero);
        

        for (j=1; j<matrix[0].length; ++j){
            if (matrix[0][j] == 0) {
                for (int x=0; x<matrix.length;++x){
                    matrix[x][j] = 0;
                }
            }
        }

        for (i=1; i < matrix.length; ++i){
            if (matrix[i][0] == 0) {
                Arrays.fill(matrix[i], 0);
            }
        }

        if (firstRowZero) {
            Arrays.fill(matrix[0], 0);
        }
        if (firstColZero) {
            for (int x=0; x<matrix.length;++x){
                matrix[x][0] = 0;
            }
        }



        return;
    }
}