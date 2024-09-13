//The pseudocode for finding the maximum element in an arry

/*
FUNCTION FindMax(A, n)
    max = A[0]  // this is where i set max to the first element in the array

    FOR i = 1 TO n-1
        IF A[i] > max THEN
            max = A[i]  //loop through the array from the second element to the last and make updates 
            //in case the the greatest is found.
            END IF
    END FOR

    RETURN max  // Return the maximum value found
END FUNCTION
*/

//The algorithm for finding the maximum element in an array

#include <stdio.h>

int FindMax(int A[], int n) {
    int max = A[0];  // this is where i set max to the first element in the array


    for (int i = 1; i < n; i++) {
        if (A[i] > max) {
            max = A[i];  // Update max if current element is greater
        }
    }

    return max;  // Return the maximum value found
}

int main() {
    int A[] = {10, 5, 8, 12, 3, 7};
    int n = sizeof(A) / sizeof(A[0]);

    int max = FindMax(A, n);
    printf("The maximum element in the array is: %d\n", max);

    return 0;
}
