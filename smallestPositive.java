// This is a demo task.
// 
// Write a function:
// 
// class Solution { public int solution(int[] A); }
// 
// that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
// 
// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
// 
// Given A = [1, 2, 3], the function should return 4.
// 
// Given A = [−1, −3], the function should return 1.
// 
// Write an efficient algorithm for the following assumptions:
// 
// N is an integer within the range [1..100,000];
// each element of array A is an integer within the range [−1,000,000..1,000,000].

import java.util.Arrays;

class Solution {
    public int solution(int[] A) {
        
        // variable resultado
        int result = 1;

        // se ordena el array de forma ascendente
        Arrays.sort(A);

        // se recorre el array
        for (int number : A) {

            // número más bajo encontrado
            if (number > result) {
                return result;
            }
            
            // el número más bajo que se guarda en result está en la lista
            if (number == result) {
                result++;
                continue;
            }
        }

        return result;
    }
}
